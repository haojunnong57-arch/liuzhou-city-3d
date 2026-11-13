#!/usr/bin/env python3
"""
Liuzhou 3D City - bounding boxes and basic metadata.
Phase 2 helper script.
"""

# Full 5 km x 5 km (centered on Wuxing Street)
FULL_BBOX = {
    "south": 24.290242,
    "north": 24.335158,
    "west": 109.387857,
    "east": 109.437143,
    "name": "liuzhou_5km_full",
}

# 1 km x 1 km prototype (Wuxing Street core)
PROTO_BBOX = {
    "south": 24.308208,
    "north": 24.317192,
    "west": 109.407571,
    "east": 109.417429,
    "name": "wuxing_1km_prototype",
}

CENTER = {"lat": 24.3127, "lon": 109.4125, "name": "Wuxing Pedestrian Street"}

def bbox_str(b, order="swne"):
    """Return 'south,west,north,east' string for Overpass / osmium style."""
    return f"{b['south']},{b['west']},{b['north']},{b['east']}"

def osmium_bbox(b):
    """Return 'west,south,east,north' for osmium extract -b."""
    return f"{b['west']},{b['south']},{b['east']},{b['north']}"

if __name__ == "__main__":
    print("=== Liuzhou Realistic 3D City – Bounds ===")
    print(f"Center: {CENTER}")
    print("\nFull 5x5 km:")
    for k, v in FULL_BBOX.items():
        print(f"  {k}: {v}")
    print(f"  osmium -b: {osmium_bbox(FULL_BBOX)}")
    print("\n1x1 km prototype:")
    for k, v in PROTO_BBOX.items():
        print(f"  {k}: {v}")
    print(f"  osmium -b: {osmium_bbox(PROTO_BBOX)}")
