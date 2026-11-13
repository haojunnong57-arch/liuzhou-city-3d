# Data Sources Log – Liuzhou Realistic 3D City

Last updated: 2026-11-13

## OSM

- **File**: `Data/OSM/guangxi-latest.osm.pbf`
- **Source**: https://download.geofabrik.de/asia/china/guangxi-latest.osm.pbf
- **Size**: ~53 MB
- **Date fetched**: 2026-11-13
- **License**: ODbL (OpenStreetMap contributors)
- **Coverage**: Entire Guangxi. Must be clipped to project bbox with osmium / osmconvert / pyosmium.

### Recommended clip commands (once osmium available)

```bash
# Full 5 km
osmium extract -b 109.387857,24.290242,109.437143,24.335158 \
  guangxi-latest.osm.pbf -o liuzhou_5km.osm.pbf

# 1 km prototype
osmium extract -b 109.407571,24.308208,109.417429,24.317192 \
  guangxi-latest.osm.pbf -o wuxing_1km.osm.pbf
```

## DEM

- **File**: `Data/DEM/Copernicus_DSM_COG_10_N24_00_E109_00_DEM.tif`
- **Source**: AWS public bucket `s3://copernicus-dem-30m/` (no sign-request)
- **URL**: https://copernicus-dem-30m.s3.amazonaws.com/Copernicus_DSM_COG_10_N24_00_E109_00_DEM/Copernicus_DSM_COG_10_N24_00_E109_00_DEM.tif
- **Size**: ~46.6 MB
- **Resolution**: ~30 m (GLO-30)
- **License**: Copernicus Licence (free for public use with attribution)
- **Coverage**: 1° × 1° tile N24 E109 – fully covers the 5 km project area.

## Building heights / LoD1 (planned)

- **GlobalBuildingAtlas**: https://github.com/zhu-xlab/GlobalBuildingAtlas  
  - Tiles by 5°; use lod1.geojson / height indices to select tiles covering lon ~109.4, lat ~24.3.  
  - License: CC BY-NC 4.0 for many components.  
  - Access: Hugging Face + mediaTUM + WFS (slow).
- **GABLE** (China national fine-grained 3D buildings): Baidu Netdisk links by province (Guangxi password historically “1567”). Check current GitHub AICyberTeam/GABLE for latest.

## Notes

- Overpass API direct queries from this environment previously failed (connection refused). Prefer Geofabrik PBF + local extract.
- No Blender binary in current environment; geometry generation scripts will produce intermediate meshes for later import.
- All source files keep original licenses; derived models for this project will document provenance.
