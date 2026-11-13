# PHASE 6.1 完整资产打包与 GLB

**版本**: v0.6.1-city-model-assets  
**日期**: 2026-11-13

## 清点
- 25 组合瓦片 STL + 75 分层 STL + 25 瓦片 GLB
- 全域 Liuzhou_5km / Terrain STL+GLB
- Water/Sidewalks STL+GLB
- OBJ + 占位 MTL（无真实纹理）
- 1746 栋属性 CSV
- SHA256SUMS.txt + FILE_INDEX.txt

## GLB
- trimesh 5.2.1 导出全部 25 瓦片及全域；回读 faces 与 STL 一致
- ZIP 内抽取 tile_2_2.glb 再次验证通过

## 包路径（构建环境）
`artifacts/Delivery/v0.6.1-city-model-assets.zip` (~11 MB compressed)

## GitHub Release
**未自动上传**（无 Release API 工具）。请网页创建 tag `v0.6.1-city-model-assets` 并上传 ZIP。

## 未验证
Unity / CAD / Blender 实机打开仍标记未验证。
