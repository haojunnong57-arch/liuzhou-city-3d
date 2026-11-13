# PHASE 5 真实精度与交付报告

**日期**: 2026-11-13  
**范围**: 五星街核心参考库 + 1746 栋高度清单 + 简易水体/人行道实体  
**原则**: 不虚构精度；不覆盖既有 1 km / 5 km 模型。

---

## 1. 交付文件清单

| 文件 | 路径 | 说明 |
|------|------|------|
| 参考资料库 | `Documentation/References/Wuxing_Core_Reference.md` | 来源、链接、许可、置信度 |
| 高度清单 CSV | `Data/Processed/phase5/building_heights_inventory.csv` | 1746 行：height / source / confidence |
| 高度统计 | `Data/Processed/phase5/height_stats.json` | 汇总 |
| 水体简易网格 | `Models/Phase5_Core/Water_surface_simple.stl` | OSM 多边形平面，z≈85 m |
| 人行道简易条带 | `Models/Phase5_Core/Sidewalks_simple.stl` | 道路中心线偏移，米级 |
| 本报告 | `Documentation/Reports/phase5_accuracy_report.md` | |
| 脚本 | `Scripts/phase5_height_inventory_and_extras.py` | 可复现 |

**未覆盖**: `Models/Prototype/`、`Models/Full5km/` 保持原样。

---

## 2. 建筑高度统计（1746 栋）

| 来源 | 数量 | 置信度 |
|------|------|--------|
| public_landmark_crosschecked | 10 | high |
| osm_height | 6 | medium |
| osm_levels_x3 | 4 | medium |
| type_estimate | 1726 | low |
| **合计** | **1746** | |

- High: 10 | Medium: 10 | Low: 1726

地王大厦公开建筑高度 **303 m** 经 CTBUH / 英中维基 / 百科交叉验证。

---

## 3. 实际精度（对照建议目标）

| 项目 | 建议目标 | 本阶段实际 | 判定 |
|------|----------|------------|------|
| 核心建筑位置 | 10–20 cm | OSM 约 **2–5 m** | 未达标 |
| 核心建筑高度 | 20–50 cm | 公开地标高度可用；位置仍米级 | 高度数字可用 ≠ 测绘位置 |
| 普通建筑位置 | 20–50 cm | **约 2–5 m** | 未达标 |
| 普通建筑高度 | 0.5–1 m | 类型估算，误差常数米 | 未达标 |
| 道路边界 | 10–20 cm | **约 1–3 m** | 未达标 |
| 车道标线 | 5–10 cm | **未建模** | 未达标 |
| 桥梁结构 | 10–20 cm | **未精细建模** | 未达标 |
| 地形高程 | 0.2–0.5 m | GLO-30 米级及以上 | 未达标 |
| 地标外观 5–10 cm | — | **未达到** | 未达标 |

人行道与水体为程序化米级几何，明确标注。

---

## 4. 下一阶段建议

1. 无授权高分影像/点云前，保持米级几何与诚实标注。  
2. 厘米级需航测/激光+控制点。  
3. GBA 高度使用前确认许可。  
4. Phase5_Core 与清单可打包 GitHub Release。

*PHASE 5（A 路径）完成记录。*
