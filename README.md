# Liuzhou Realistic 3D City (柳州市中心真实三维城市数字孪生)

**Project**: Liuzhou Realistic 3D City  
**Target**: 5 km × 5 km digital twin of Liuzhou city center (Guangxi, China), centered on Wuxing Street (五星街 / 五星商业步行街).  
**Use cases**: Game environments (Unity URP/HDRP), CAD inspection, visualization, urban analysis.  
**License of this repo**: Documentation and scripts under MIT unless otherwise noted. Source data retains original licenses (ODbL for OSM, etc.).

**Repository**: https://github.com/haojunnong57-arch/liuzhou-city-3d  
**Status (2026-11-13)**: Phase 1 – data sources locked, bounds defined, repo initialized. Phase 2 in progress (OSM/DEM acquisition + 1×1 km prototype).

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

Covers: Wuxing Street & pedestrian area, People’s Square vicinity, Jiefang North Rd, Zhongshan Middle Rd, Wenhui Rd, commercial blocks, Liu River section through the city, bridges, riverside buildings, surrounding residential and public facilities.

### Prototype extent (1 km × 1 km validation)
| Edge   | Coordinate   |
|--------|--------------|
| South  | 24.308208    |
| North  | 24.317192    |
| West   | 109.407571   |
| East   | 109.417429   |

Prototype is only for pipeline validation; final deliverable remains the full 5×5 km.

Coordinate system for modeling: metric projected CRS (UTM zone or local equivalent). Source data usually WGS84 / EPSG:4326 or EPSG:3857.

---

## 2. Data Sources (verified)

| Layer              | Source                          | Notes / License                  | Status |
|--------------------|---------------------------------|----------------------------------|--------|
| Buildings, roads, water, POI | OpenStreetMap via Geofabrik Guangxi extract | ODbL                             | Primary |
| Terrain (DEM)      | Copernicus GLO-30 / SRTM / NASADEM | Free public (Copernicus licence / public domain equivalents) | Primary |
| Building heights / LoD1 | GlobalBuildingAtlas (TUM), GABLE (China national) | CC BY-NC 4.0 (GBA), check GABLE terms | Supplement |
| Reference imagery  | Public satellite / basemaps     | Attribution required             | Support |

**Existing commercial 3D city models of Liuzhou** (ArtStation / 3DOcean etc.) were reviewed. They are low-poly, mostly flat, partly AI-generated, and do not meet the requirements for real elevation, Wuxing Street detail, PBR wet roads, or open Unity/CAD pipeline. They are **not** used as source geometry.

No free high-fidelity ready-made Liuzhou digital twin covering the required area was found on GitHub or open GIS portals.

---

## 3. Tools & Pipeline

- **GIS / data**: OSMnx / GeoPandas / Shapely / PyProj / Rasterio / Trimesh (Python)
- **Blender**: BlenderGIS, Blosm (Blender-OSM) for import + procedural buildings when available
- **Mesh**: Trimesh / Open3D for repair, LOD, export
- **Engine**: Unity (URP preferred; HDRP optional for high-quality demos)
- **CAD**: STL (chunked) for common viewers
- **Formats**: STL, OBJ, FBX, GLB/glTF, BLEND, Unity package, textures (BaseColor / Normal / Roughness / Metallic)

Current Agent environment notes:
- No interactive Blender binary.
- Some external APIs (Overpass) may be restricted; prefer Geofabrik PBF + local clipping.
- Scripts and intermediate GeoJSON / mesh files are produced first; full textured renders require local Blender/Unity later.

---

## 4. Project Roadmap

1. **Data collection** (current) – OSM extract, DEM tiles, height layers for the 5×5 km bbox; document sources & licenses.
2. **1×1 km prototype** – Wuxing Street core: buildings + roads + terrain + Liu River snippet → STL / OBJ / GLB samples + CAD check.
3. **Full 5×5 km geometry** – Extrude buildings, generate road network, drape on DEM, chunk by districts.
4. **PBR & lighting** – Asphalt (dry/wet with controlled reflections), building materials, day/overcast/rain/night presets.
5. **Unity & performance** – URP materials, LOD, occlusion, streaming / district loading, collision.
6. **CAD & delivery** – Chunked STL, validation, GitHub Releases / LFS for large assets, full documentation.

Every phase commits real files and progress notes. No fabricated “complete model” claims.

---

## 5. Directory Layout (target)

```
liuzhou-city-3d/
├── README.md
├── Data/
│   ├── OSM/
│   ├── DEM/
│   └── References/
├── Models/
│   ├── STL/
│   ├── FBX/
│   ├── GLB/
│   └── OBJ/
├── Blender/
├── Unity/
├── Textures/
├── Materials/
├── Scripts/
├── Documentation/
└── Skills/   # notes on tools used
```

Large binaries → Git LFS or Releases.

---

## 6. Attribution & Legal

- OpenStreetMap data © OpenStreetMap contributors (ODbL).
- Copernicus DEM © ESA / DLR / Airbus (Copernicus licence).
- GlobalBuildingAtlas / GABLE – follow their stated licenses (often CC BY-NC).
- This reconstruction does not claim official endorsement by Liuzhou municipal authorities.

---

## 7. Current Progress Log

- 2026-11-13: Repository created. Geographic bounds calculated. Existing commercial models evaluated and rejected for fidelity. Tool stack and data sources locked. README published.
- Next commits: Guangxi OSM PBF reference + clipping scripts, DEM tile acquisition notes, 1×1 km prototype geometry when data is available in environment.

---

**Contact / issues**: Use GitHub Issues on this repository.
