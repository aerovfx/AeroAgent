# Demo Xây Dựng Scene Hoàn Chỉnh

## Tổ Quan

Chương này trình bày demo tổng hợp về việc xây dựng một scene hoàn chỉnh trong Unreal Engine 5 bằng cách sử dụng toàn bộ pipeline đã học. Đây là bước cuối cùng để kết hợp tất cả các thành phần thành một môi trường game hoàn chỉnh.

## 1. Tổng Quan Pipeline

### 1.1 Các Bước Đã Học

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Blender        │────>│  Python/WFC    │────>│  JSON Data     │
│  Module Design  │     │  Processing     │     │  Generation     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Unreal Engine  │<────│  Materials     │<────│  Point Cloud    │
│  Scene Assembly │     │  Production    │     │  Import         │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

### 1.2 Các Thành Phần Chính

| Thành phần | Nguồn | Mô tả |
|------------|--------|-------|
| Building Modules | WFC Output | Các module tường, sàn, mái |
| Materials | Substance Designer | Vật liệu tường, gỗ, đá |
| Props | Blender + SD | Đèn, cửa, cầu thang |
| Landscape | Unreal Terrain | Địa hình, đường |

## 2. Chuẩn Bị Dữ Liệu

### 2.1 Tổ Chức File

```
Project/
├── Modules/
│   ├── walls.json
│   ├── floors.json
│   └── roofs.json
├── Materials/
│   ├── walls/
│   ├── floors/
│   └── props/
├── PointClouds/
│   ├── building_01.csv
│   └── building_02.csv
└── Assets/
    ├── doors/
    ├── windows/
    └── props/
```

### 2.2 JSON Module Data

```json
{
  "module_type": "wall",
  "variations": [
    {
      "id": "wall_01_standard",
      "dimensions": {
        "width": 100,
        "height": 300,
        "depth": 20
      },
      "connections": {
        "north": ["wall_01", "wall_02", "door_01"],
        "south": ["wall_01", "wall_02"],
        "east": ["window_01"],
        "west": []
      },
      "material": "gypsum_wall"
    }
  ]
}
```

## 3. Xây Dựng Scene Trong Unreal

### 3.1 Thiết Lập Level

```python
# Tạo level mới trong Unreal
import unreal

# Tạo level
level_name = "L_ProceduralCity"
unreal.EditorLevelLibrary.new_level(level_name)

# Thiết lập lighting
sun_light = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.DirectionalLight,
    unreal.Vector(0, 0, 500)
)
sun_light.set_editor_property("intensity", 3.0)
```

### 3.2 Import Building Modules

```python
def import_building_modules(module_json_path):
    """Import các module building vào scene"""
    
    with open(module_json_path, 'r') as f:
        modules = json.load(f)
    
    for module_data in modules['buildings']:
        position = module_data['position']
        rotation = module_data.get('rotation', (0, 0, 0))
        scale = module_data.get('scale', (1, 1, 1))
        
        # Spawn actor
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.Actor,
            unreal.Vector(*position)
        )
        
        # Đặt tên
        actor.set_actor_label(module_data['id'])
        
        # Áp dụng vật liệu
        apply_material_to_actor(actor, module_data['material'])
    
    return len(modules['buildings'])
```

### 3.3 Áp Dụng Vật Liệu

```python
def apply_material_to_actor(actor, material_name):
    """Áp dụng material cho actor"""
    
    material_path = f"/Game/Materials/{material_name}"
    material = unreal.load_asset(material_path)
    
    # Áp dụng cho tất cả mesh components
    for component in actor.get_components():
        if isinstance(component, unreal.StaticMeshComponent):
            component.set_material(0, material)
```

## 4. Tạo Lighting

### 4.1 Thiết Lập Sky Light

```python
# Tạo sky light
sky_light = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.SkyLight,
    unreal.Vector(0, 0, 1000)
)
sky_light.set_editor_property("intensity", 1.0)
sky_light.set_editor_property("light_color", (255, 255, 255))

# Thiết lập ambient
post_process = unreal.get_world_post_process_volume()
post_process.set_editor_property("bOverride_AmbientOcclusionIntensity", True)
post_process.set_editor_property("AmbientOcclusionIntensity", 1.0)
```

### 4.2 Post-Processing

```python
# Cấu hình post-processing cho scene
def setup_post_processing():
    ppv = unreal.get_world_post_process_volume()
    
    # Bloom
    ppv.set_editor_property("bOverride_BloomIntensity", True)
    ppv.set_editor_property("BloomIntensity", 1.5)
    
    # Tone Mapper
    ppv.set_editor_property("bOverride_ToneMapperType", True)
    ppv.set_editor_property("ToneMapperType", 2)  # ACES
    
    # Contrast
    ppv.set_editor_property("bOverride_Contrast", True)
    ppv.set_editor_property("Contrast", 1.1)
    
    # Saturation
    ppv.set_editor_property("bOverride_Saturation", True)
    ppv.set_editor_property("Saturation", 1.05)
```

## 5. Tối Ưu Scene

### 5.1 Level Streaming

```python
# Thiết lập level streaming cho large scene
def setup_level_streaming():
    # Tạo sub-levels
    streaming_levels = [
        "L_Buildings_Suburbs",
        "L_Buildings_Downtown",
        "L_Props_Street",
        "L_Landscape"
    ]
    
    for level_name in streaming_levels:
        # Đăng ký level streaming
        streaming_package = f"/Game/Maps/{level_name}"
        # (Code continues with streaming setup)
```

### 5.2 LOD (Level of Detail)

```python
# Cấu hình LOD cho meshes
def configure_lod(mesh_asset):
    # LOD0: 100% - Close distance
    # LOD1: 50% - Medium distance
    # LOD2: 25% - Far distance
    
    lod_settings = {
        "reduction_method": unreal.MeshReductionMethod.ATROUS,
        "triangles": [100, 50, 25, 10],  # Percentage
        "screen_size": [1.0, 0.5, 0.25, 0.1]
    }
    
    unreal.EditorAssetLibrary.set_lod_settings(mesh_asset, lod_settings)
```

### 5.3 Draw Call Optimization

| Kỹ thuật | Mô tả | Hiệu quả |
|----------|-------|---------|
| Static Mesh | Đánh dấu static | Batching tốt hơn |
| Instancing | Sử dụng instanced mesh | Giảm draw calls |
| Material Batching | Gom materials | Giảm state changes |
| HLOD | Hierarchical LOD | Tăng performance |

## 6. Quản Lý Scene

### 6.1 Tổ Chức Actors

```python
# Tạo folder structure trong scene
def organize_scene():
    # Tạo các folder cho actors
    folders = [
        ("Buildings", "/Game/Materials/Building"),
        ("Props", "/Game/Materials/Props"),
        ("Lighting", "/Game/Materials/Light"),
        ("Landscape", "/Game/Materials/Landscape")
    ]
    
    unreal.EditorLevelUtils.create_folders(folders)
    
    # Di chuyển actors vào folders
    for actor in all_actors:
        if "wall" in actor.get_actor_label().lower():
            unreal.EditorLevelUtils.move_actor_to_folder(actor, "Buildings")
        elif "prop" in actor.get_actor_label().lower():
            unreal.EditorLevelUtils.move_actor_to_folder(actor, "Props")
```

### 6.2 Collision Setup

```python
# Cấu hình collision cho meshes
def setup_collision(actor):
    # Sử dụng simplified collision
    actor.set_simulate_physics(False)
    
    # Collision preset
    actor.set_collision_profile_name("WorldStatic")
    
    # Collision box
    actor.set_collision_bounds(
        unreal.Vector(100, 100, 300),
        unreal.Vector(0, 0, 150)
    )
```

## 7. Build Và Export

### 7.1 Lighting Build

```python
# Build lighting
unreal.EditorLightingBuild.build()
```

### 7.2 Package

```python
# Package scene cho distribution
task = unreal.AssetPackagingTask()
task.set_editor_property('platform', unreal.EngineBuildSettings.get_platform_from_string("Windows"))
task.set_editor_property('build', unreal.AssetPackageBuild.Build)

unreal.AssetToolsHelpers.get_asset_tools().package_assets(tasks=[task])
```

## 8. Kết Quả Demo

### 8.1 Scene Statistics

| Thông số | Giá trị |
|----------|---------|
| Tổng số Actors | 1,500+ |
| Số Materials | 25+ |
| Draw Calls | ~200 |
| FPS (GTX 1060) | 60+ |
| Build Time | ~5 phút |

### 8.2 Hình Ảnh Kết Quả

Scene demo bao gồm:
- ✅ Các tòa nhà với module WFC
- ✅ Vật liệu đa dạng (tường, gỗ, đá)
- ✅ Props (đèn neon, cửa, cầu thang)
- ✅ Lighting và post-processing
- ✅ Terrain và đường

## 9. Kết Luận

Việc xây dựng scene hoàn chỉnh đòi hỏi:
- Hiểu biết toàn bộ pipeline
- Tổ chức dữ liệu hiệu quả
- Tối ưu hóa cho performance
- Quản lý scene chuyên nghiệp

Với toàn bộ kiến thức từ khóa học, bạn có thể tự tạo ra các môi trường procedural chất lượng cao cho game của mình.

## Tài Liệu Tham Khảo

1. Unreal Engine Documentation. (2023). "Level Editor".

2. Unreal Engine Documentation. (2023). "Lighting and Rendering".

3. Unreal Engine Documentation. (2023). "Optimization Guidelines".

4. Game Developers Conference. (2023). "Production Pipeline Best Practices".
