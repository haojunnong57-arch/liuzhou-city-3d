# Liuzhou Realistic 3D City (柳州市中心真实三维城市数字孪生)

**Repository**: https://github.com/haojunnong57-arch/liuzhou-city-3d  
**Status (2026-11-13)**: **Phase 5 (path A) complete** – reference library, 1746-building height inventory with confidence, simple water/sidewalk meshes, **honest accuracy vs cm-level targets**.

---

## Geographic Scope

Center ≈ **24.3127°N, 109.4125°E**  
Bounds: S 24.290242 / N 24.335158 / W 109.387857 / E 109.437143  
CRS: **EPSG:32649 (UTM 49N)** for Phase 4 meshes.

---

## Phase 5 (accuracy honesty)

- Reference library: `Documentation/References/Wuxing_Core_Reference.md`  
  (Diwang **303 m** cross-checked CTBUH/Wikipedia; Wuxing street ~903 m; licenses listed)
- Height inventory: 1746 rows → `Data/Processed/phase5/building_heights_inventory.csv`  
  - high: 10 | medium: 10 | low (type estimate): 1726
- Extra meshes (do not overwrite Phase 3/4):  
  - `Models/Phase5_Core/Water_surface_simple.stl`  
  - `Models/Phase5_Core/Sidewalks_simple.stl` (procedural, metre-level)
- Accuracy report: `Documentation/Reports/phase5_accuracy_report.md`  
  **Cm-level targets (10–50 cm position/height, 5–10 cm markings) are NOT met** with OSM + GLO-30. Documented explicitly.

---

## Phase 4 (full 5×5 km geometry)

1746 buildings, ~252 km roads, 25 tiles, DEM-draped bases, UTM. See `Documentation/Reports/full5km_report.txt`.

---

## Phase 3 (1 km prototype)

Preserved under `Models/Prototype/`.

---

## Data & licenses

OSM (ODbL), Copernicus DEM, public landmark heights (cite sources). GBA not bulk-used (license).

---

## Roadmap

1–4. ~~Data → prototype → 5 km geometry → Phase 5 reference/inventory~~  
5. Survey-grade data or photogrammetry if cm targets required  
6. PBR / Unity when geometry authority is sufficient  
7. Releases / LFS for large binaries

**Contact**: GitHub Issues.
