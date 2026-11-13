# Liuzhou Realistic 3D City (柳州市中心真实三维城市数字孪生)

**Project**: Liuzhou Realistic 3D City  
**Target**: 5 km × 5 km digital twin of Liuzhou city center (Guangxi, China), centered on Wuxing Street (五星街 / 五星商业步行街).  
**Use cases**: Game environments (Unity URP/HDRP), CAD inspection, visualization, urban analysis.  
**License of this repo**: Documentation and scripts under MIT unless otherwise noted. Source data retains original licenses (ODbL for OSM, etc.).

**Repository**: https://github.com/haojunnong57-arch/liuzhou-city-3d  
**Status (2026-11-13)**: **Phase 3 complete** – 1×1 km Wuxing prototype meshes generated from real OSM + DEM.

---

## 1. Geographic Scope

### Core point
- **Wuxing Pedestrian Street (五星商业步行街)** center ≈ **24.3127°N, 109.4125°E**

### Full project extent (5 km × 5 km)
| Edge   | Coordinate   |
|--------|--------------|
| South  | 24.290242    |
| North  | 24.335158    |
| West   | 109.387857   |
| East   | 109.437143   |

### Prototype extent (1 km × 1 km) – Phase 3 delivered
| Edge   | Coordinate   |
|--------|--------------|
| South  | 24.308208    |
| North  | 24.317192    |
| West   | 109.407571   |
| East   | 109.417429   |

---

## 2. Phase 3 Prototype Results (real geometry)

Generated from Geofabrik Guangxi OSM (clipped with osmium) + Copernicus GLO-30 DEM (cropped with GDAL).

| Asset | File | Size | Triangles / Notes |
|-------|------|------|-------------------|
| Terrain | Terrain.stl | ~103 KB | 2108 tris, real DEM elevations |
| Buildings | Buildings.stl | ~254 KB | 5188 tris, 152 footprints (height estimated) |
| Roads | Roads.stl | ~39 KB | 802 tris, 65 segments, ~15.2 km total length |
| Combined | Liuzhou_Prototype.stl | ~396 KB | 8098 tris |
| Combined | Liuzhou_Prototype.obj | ~810 KB | 24294 verts, groups: Terrain/Buildings/Roads |

**Validation**: STL binary headers match triangle counts; OBJ is valid Wavefront text. No Blender available in environment – geometry checks via structure + size only. GLB not produced (no glTF writer).

**Height note**: Almost all building heights are type-based estimates (OSM `height` / `building:levels` sparse in extract). Marked as estimated in report.

Scripts: `Scripts/generate_prototype.py`, `Scripts/clip_bounds.py`  
Report: `Documentation/Reports/prototype_report.txt`

Model binaries currently live in the agent workspace (`artifacts/Models/Prototype/`). Upload to GitHub Releases / LFS in a follow-up commit if required for download.

---

## 3. Data Sources

See `Documentation/DATA_SOURCES.md`.

- OSM: Geofabrik `guangxi-latest.osm.pbf` (ODbL)
- DEM: Copernicus GLO-30 tile N24 E109 (Copernicus Licence)

---

## 4. Roadmap

1. ~~Data collection~~
2. ~~1×1 km prototype geometry~~ (Phase 3)
3. Full 5×5 km geometry + height enrichment (GBA / GABLE)
4. PBR wet roads + lighting presets
5. Unity URP package + LOD / streaming
6. CAD chunked STL + Releases

---

## 5. Progress Log

- 2026-11-13 Phase 1–2: bounds, OSM/DEM acquired, repo + docs.
- 2026-11-13 Phase 3: osmium clip → GeoJSON + DEM XYZ → pure-Python extrusion → Terrain/Buildings/Roads STL + combined OBJ/STL. Report + generator committed.

**Contact**: GitHub Issues.
