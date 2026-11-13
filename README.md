# Liuzhou Realistic 3D City (柳州市中心真实三维城市数字孪生)

**Project**: Liuzhou Realistic 3D City  
**Target**: 5 km × 5 km digital twin of Liuzhou city center (Guangxi, China), centered on Wuxing Street.  
**Repository**: https://github.com/haojunnong57-arch/liuzhou-city-3d  
**Status (2026-11-13)**: **Phase 4 complete** – full 5×5 km tiled geometry with UTM metric CRS and DEM-draped buildings/roads.

---

## Geographic Scope

Center ≈ **24.3127°N, 109.4125°E**  
Bounds: S 24.290242 / N 24.335158 / W 109.387857 / E 109.437143  
CRS for models: **EPSG:32649 (UTM zone 49N)**, local origin at SW corner.

---

## Phase 4 Results (full 5×5 km)

| Metric | Value |
|--------|-------|
| Buildings | **1746** (8 with OSM height/levels, 1738 type-estimated) |
| Road segments | **1075** |
| Road total length | **~252 km** |
| Water features | **139** |
| DEM elev range | **75.3 – 271.9 m** (mean 97.6) |
| Terrain triangles | **56 672** |
| Total triangles (all tiles) | **104 652** |
| Buildings draped on DEM | **1746 / 1746 (100%)** |
| Tiles | **25** (1×1 km each) |

**Main outputs** (agent workspace `artifacts/Models/Full5km/`):
- `Liuzhou_5km.stl` (~5.0 MB)
- `Liuzhou_5km.obj` (~11 MB)
- `Terrain_full.stl` (~2.8 MB)
- `tiles/tile_X_Y[_Terrain|_Buildings|_Roads].stl` (25 tiles)

Report: `Documentation/Reports/full5km_report.txt`  
Generator: `Scripts/generate_full5km.py`

**Validation**: STL binary headers match declared triangle counts. No Blender / GLB (environment limits). Heights remain mostly estimated pending GBA/GABLE ingestion.

---

## Phase 3 (1 km prototype)

Still available under `Models/Prototype/`. See earlier reports.

---

## Data Sources

- OSM: Geofabrik Guangxi PBF (ODbL) → osmium extract
- DEM: Copernicus GLO-30 (Copernicus Licence) → GDAL crop
- Heights: OSM tags preferred; type estimates otherwise (marked). GBA/GABLE not yet applied.

---

## Roadmap

1. ~~Data collection~~
2. ~~1×1 km prototype~~
3. ~~Full 5×5 km geometry + DEM draping + tiling~~
4. Height enrichment (GBA / GABLE) + water/bridge volumes
5. PBR materials (wet asphalt etc.) + lighting
6. Unity URP + LOD / streaming
7. GitHub Releases / LFS for large binaries + CAD packages

---

## Progress Log

- 2026-11-13 Phase 1–3: data, 1 km prototype.
- 2026-11-13 Phase 4: full 5 km UTM geometry, 25 tiles, 100% DEM-sampled bases, combined STL/OBJ generated. Report committed.

Large model files live in the build environment; upload to **GitHub Releases** for public download in a subsequent step.

**Contact**: GitHub Issues.
