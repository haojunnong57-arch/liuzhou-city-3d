#!/usr/bin/env python3
"""
Liuzhou Wuxing 1x1 km prototype mesh generator.
Pure Python (minimal deps). Reads GeoJSON + XYZ DEM, writes STL/OBJ.
Origin: SW corner of prototype bbox in local metric approx.
"""
import json
import math
import struct
import os
from collections import defaultdict

# --- Bounds (fixed) ---
SOUTH, NORTH = 24.308208, 24.317192
WEST, EAST = 109.407571, 109.417429
ORIGIN_LON, ORIGIN_LAT = WEST, SOUTH

# Approximate meters per degree at ~24.3N
M_PER_DEG_LAT = 111320.0
M_PER_DEG_LON = 111320.0 * math.cos(math.radians(24.3127))

OUT_DIR = "/home/workdir/artifacts/Models/Prototype"
DATA_DIR = "/home/workdir/artifacts/Data/Processed"
os.makedirs(OUT_DIR, exist_ok=True)


def lonlat_to_local(lon, lat):
    x = (lon - ORIGIN_LON) * M_PER_DEG_LON
    y = (lat - ORIGIN_LAT) * M_PER_DEG_LAT
    return x, y


def write_stl_binary(path, triangles):
    """triangles: list of ((x,y,z),(x,y,z),(x,y,z))"""
    with open(path, "wb") as f:
        f.write(b"\0" * 80)
        f.write(struct.pack("<I", len(triangles)))
        for t in triangles:
            ax, ay, az = t[0]
            bx, by, bz = t[1]
            cx, cy, cz = t[2]
            nx = (by - ay) * (cz - az) - (bz - az) * (cy - ay)
            ny = (bz - az) * (cx - ax) - (bx - ax) * (cz - az)
            nz = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
            ln = math.sqrt(nx * nx + ny * ny + nz * nz) or 1.0
            nx, ny, nz = nx / ln, ny / ln, nz / ln
            f.write(struct.pack("<3f", nx, ny, nz))
            for v in t:
                f.write(struct.pack("<3f", *v))
            f.write(struct.pack("<H", 0))
    return len(triangles)


def write_obj(path, vertices, faces, groups=None):
    with open(path, "w") as f:
        f.write("# Liuzhou Wuxing 1km prototype\n")
        f.write(f"# vertices: {len(vertices)}\n")
        for v in vertices:
            f.write(f"v {v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")
        if groups:
            for name, face_list in groups.items():
                f.write(f"g {name}\n")
                for face in face_list:
                    f.write("f " + " ".join(str(i) for i in face) + "\n")
        else:
            for face in faces:
                f.write("f " + " ".join(str(i) for i in face) + "\n")


def load_dem_xyz(path):
    pts = []
    with open(path) as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 3:
                continue
            lon, lat, elev = float(parts[0]), float(parts[1]), float(parts[2])
            x, y = lonlat_to_local(lon, lat)
            pts.append((x, y, elev))
    return pts


def dem_to_terrain_tris(pts, cols=35, rows=32):
    if len(pts) != cols * rows:
        print(f"Warning: expected {cols*rows} pts, got {len(pts)}")
    tris = []
    xs = sorted(set(round(p[0], 3) for p in pts))
    ys = sorted(set(round(p[1], 3) for p in pts))
    grid = {}
    for x, y, z in pts:
        ix = min(range(len(xs)), key=lambda i: abs(xs[i] - x))
        iy = min(range(len(ys)), key=lambda i: abs(ys[i] - y))
        grid[(ix, iy)] = (xs[ix], ys[iy], z)
    for iy in range(len(ys) - 1):
        for ix in range(len(xs) - 1):
            if (ix, iy) not in grid or (ix + 1, iy) not in grid:
                continue
            if (ix, iy + 1) not in grid or (ix + 1, iy + 1) not in grid:
                continue
            a = grid[(ix, iy)]
            b = grid[(ix + 1, iy)]
            c = grid[(ix + 1, iy + 1)]
            d = grid[(ix, iy + 1)]
            tris.append((a, b, c))
            tris.append((a, c, d))
    return tris


def parse_buildings(geojson_path):
    with open(geojson_path) as f:
        data = json.load(f)
    buildings = []
    for ft in data["features"]:
        props = ft.get("properties") or {}
        geom = ft.get("geometry") or {}
        gtype = geom.get("type")
        coords = geom.get("coordinates")
        if not coords:
            continue
        rings = []
        if gtype == "Polygon":
            rings = coords
        elif gtype == "MultiPolygon":
            for poly in coords:
                rings.extend(poly)
        elif gtype == "LineString":
            if len(coords) >= 3 and coords[0] == coords[-1]:
                rings = [coords]
            elif len(coords) >= 3:
                rings = [coords + [coords[0]]]
        else:
            continue
        for ring in rings:
            if len(ring) < 3:
                continue
            local = []
            for c in ring:
                if len(c) < 2:
                    continue
                lon, lat = c[0], c[1]
                if not (WEST - 0.001 <= lon <= EAST + 0.001 and SOUTH - 0.001 <= lat <= NORTH + 0.001):
                    continue
                x, y = lonlat_to_local(lon, lat)
                local.append((x, y))
            if len(local) < 3:
                continue
            if local[0] != local[-1]:
                local.append(local[0])
            h = None
            est = False
            if "height" in props:
                try:
                    h = float(str(props["height"]).replace("m", "").strip())
                except Exception:
                    pass
            if h is None and "building:levels" in props:
                try:
                    levels = float(props["building:levels"])
                    h = levels * 3.0
                    est = True
                except Exception:
                    pass
            if h is None:
                btype = str(props.get("building", "yes")).lower()
                if btype in ("commercial", "retail", "office"):
                    h = 18.0
                elif btype in ("apartments", "residential"):
                    h = 24.0
                else:
                    h = 12.0
                est = True
            buildings.append({
                "ring": local,
                "height": h,
                "estimated": est,
                "tags": {k: props[k] for k in list(props)[:12]},
            })
    return buildings


def extrude_building(ring, height, ground_z=85.0):
    if len(ring) < 4:
        return []
    pts = ring[:-1] if ring[0] == ring[-1] else ring
    n = len(pts)
    if n < 3:
        return []
    tris = []
    for i in range(n):
        j = (i + 1) % n
        a = (pts[i][0], pts[i][1], ground_z)
        b = (pts[j][0], pts[j][1], ground_z)
        c = (pts[j][0], pts[j][1], ground_z + height)
        d = (pts[i][0], pts[i][1], ground_z + height)
        tris.append((a, b, c))
        tris.append((a, c, d))
    center_xy = (sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n)
    top_c = (center_xy[0], center_xy[1], ground_z + height)
    for i in range(n):
        j = (i + 1) % n
        a = (pts[i][0], pts[i][1], ground_z + height)
        b = (pts[j][0], pts[j][1], ground_z + height)
        tris.append((a, b, top_c))
    bot_c = (center_xy[0], center_xy[1], ground_z)
    for i in range(n):
        j = (i + 1) % n
        a = (pts[i][0], pts[i][1], ground_z)
        b = (pts[j][0], pts[j][1], ground_z)
        tris.append((b, a, bot_c))
    return tris


def parse_roads(geojson_path, default_width=8.0):
    with open(geojson_path) as f:
        data = json.load(f)
    roads = []
    width_map = {
        "motorway": 16, "trunk": 14, "primary": 12, "secondary": 10,
        "tertiary": 8, "residential": 6, "service": 4, "footway": 2,
        "path": 1.5, "pedestrian": 4,
    }
    for ft in data["features"]:
        props = ft.get("properties") or {}
        if "highway" not in props:
            continue
        geom = ft.get("geometry") or {}
        if geom.get("type") != "LineString":
            continue
        coords = geom.get("coordinates") or []
        if len(coords) < 2:
            continue
        local = []
        for c in coords:
            lon, lat = c[0], c[1]
            if not (WEST - 0.002 <= lon <= EAST + 0.002 and SOUTH - 0.002 <= lat <= NORTH + 0.002):
                continue
            local.append(lonlat_to_local(lon, lat))
        if len(local) < 2:
            continue
        hw = props.get("highway", "residential")
        w = width_map.get(hw, default_width)
        if "width" in props:
            try:
                w = float(props["width"])
            except Exception:
                pass
        roads.append({"pts": local, "width": w, "highway": hw})
    return roads


def road_to_tris(pts, width, ground_z=85.0):
    if len(pts) < 2:
        return []
    half = width / 2.0
    left, right = [], []
    for i in range(len(pts)):
        if i == 0:
            dx = pts[1][0] - pts[0][0]
            dy = pts[1][1] - pts[0][1]
        elif i == len(pts) - 1:
            dx = pts[i][0] - pts[i - 1][0]
            dy = pts[i][1] - pts[i - 1][1]
        else:
            dx = pts[i + 1][0] - pts[i - 1][0]
            dy = pts[i + 1][1] - pts[i - 1][1]
        ln = math.sqrt(dx * dx + dy * dy) or 1.0
        nx, ny = -dy / ln, dx / ln
        left.append((pts[i][0] + nx * half, pts[i][1] + ny * half, ground_z + 0.15))
        right.append((pts[i][0] - nx * half, pts[i][1] - ny * half, ground_z + 0.15))
    tris = []
    for i in range(len(pts) - 1):
        a, b = left[i], left[i + 1]
        c, d = right[i + 1], right[i]
        tris.append((a, b, c))
        tris.append((a, c, d))
    return tris


def main():
    report = []
    report.append("=== Liuzhou Wuxing 1km Prototype Generation Report ===\n")
    dem_xyz = os.path.join(DATA_DIR, "wuxing_1km_dem.xyz")
    dem_pts = load_dem_xyz(dem_xyz)
    report.append(f"DEM points: {len(dem_pts)}")
    terrain_tris = dem_to_terrain_tris(dem_pts)
    report.append(f"Terrain triangles: {len(terrain_tris)}")
    terrain_path = os.path.join(OUT_DIR, "Terrain.stl")
    n = write_stl_binary(terrain_path, terrain_tris)
    report.append(f"Wrote {terrain_path} ({os.path.getsize(terrain_path)} bytes, {n} tris)")
    gj = os.path.join(DATA_DIR, "wuxing_1km.geojson")
    buildings = parse_buildings(gj)
    report.append(f"Buildings parsed: {len(buildings)}")
    est_count = sum(1 for b in buildings if b["estimated"])
    report.append(f"  of which height estimated: {est_count}")
    b_tris = []
    for b in buildings:
        b_tris.extend(extrude_building(b["ring"], b["height"], ground_z=85.0))
    report.append(f"Building triangles: {len(b_tris)}")
    b_path = os.path.join(OUT_DIR, "Buildings.stl")
    n = write_stl_binary(b_path, b_tris)
    report.append(f"Wrote {b_path} ({os.path.getsize(b_path)} bytes, {n} tris)")
    roads = parse_roads(gj)
    report.append(f"Road segments: {len(roads)}")
    total_len = 0.0
    for r in roads:
        for i in range(len(r["pts"]) - 1):
            dx = r["pts"][i + 1][0] - r["pts"][i][0]
            dy = r["pts"][i + 1][1] - r["pts"][i][1]
            total_len += math.sqrt(dx * dx + dy * dy)
    report.append(f"Approx road total length: {total_len:.1f} m")
    r_tris = []
    for r in roads:
        r_tris.extend(road_to_tris(r["pts"], r["width"]))
    report.append(f"Road triangles: {len(r_tris)}")
    r_path = os.path.join(OUT_DIR, "Roads.stl")
    n = write_stl_binary(r_path, r_tris)
    report.append(f"Wrote {r_path} ({os.path.getsize(r_path)} bytes, {n} tris)")
    all_verts = []
    groups = {"Terrain": [], "Buildings": [], "Roads": []}
    def add_tris(tris, group_name):
        base = len(all_verts)
        for t in tris:
            for v in t:
                all_verts.append(v)
            groups[group_name].append((base + 1, base + 2, base + 3))
            base += 3
    add_tris(terrain_tris, "Terrain")
    add_tris(b_tris, "Buildings")
    add_tris(r_tris, "Roads")
    obj_path = os.path.join(OUT_DIR, "Liuzhou_Prototype.obj")
    write_obj(obj_path, all_verts, [], groups)
    report.append(f"Wrote {obj_path} ({os.path.getsize(obj_path)} bytes, verts={len(all_verts)})")
    all_tris = terrain_tris + b_tris + r_tris
    comb_path = os.path.join(OUT_DIR, "Liuzhou_Prototype.stl")
    n = write_stl_binary(comb_path, all_tris)
    report.append(f"Wrote {comb_path} ({os.path.getsize(comb_path)} bytes, {n} tris)")
    report.append("\nNotes:")
    report.append("- Ground elevation fixed ~85m for buildings/roads (DEM mean ~88m); terrain uses real DEM.")
    report.append("- Building heights: from OSM height/levels when present, else type-based estimate (marked).")
    report.append("- Roads are flat ribbons; no curb/markings yet.")
    report.append("- No Blender; geometry verified by file size and triangle counts only.")
    report.append("- GLB not generated (no gltf lib); OBJ+STL are primary.")
    report_text = "\n".join(report)
    print(report_text)
    with open(os.path.join(OUT_DIR, "../..", "Documentation", "Reports", "prototype_report.txt"), "w") as f:
        f.write(report_text)
    return report_text


if __name__ == "__main__":
    main()
