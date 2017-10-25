# scops
ops admin ui.

## Design

#### 仓库界面(images列表)
字段：仓库名，Tags
1.请求_catalog
2.分别请求每个image的tags获取tags信息，包含数量

#### Image界面（Tags列表）
字段：id,Tag,Created,Size,Delete,OS
1.请求tags
2.分别请求每个tag的manifests
