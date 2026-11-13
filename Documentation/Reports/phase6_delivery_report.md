# PHASE 6 交付与验证报告

**版本**: v0.6.0-city-model-assets  
**日期**: 2026-11-13

## 实际文件
- Liuzhou_5km.stl ~5.0 MB (104652 tris)
- Liuzhou_5km.obj ~11 MB + MTL placeholder
- Terrain_full.stl ~2.8 MB
- Water / Sidewalks Phase5 STL
- tiles_sample (center tile)
- building_heights_inventory.csv (1746 rows)

## 格式
- STL / OBJ+MTL：已提供
- GLB / FBX / BLEND：**未生成**（无 Blender/glTF 管线）

## 验证
- STL 二进制头与面数一致（脚本）
- Unity / AutoCAD / FreeCAD / Blender：**未在本环境运行** → **未验证**

## 高度源调查
- Evolving Cityscape **含柳州**（预测栅格）— 未合并
- MS/Google 足迹中国不可用

## 未解决
GLB、Unity 实机、完整 25 瓦片 Release 附件、预测高度匹配
