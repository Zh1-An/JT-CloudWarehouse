# JT-CloudWarehouse · 云仓库存导出

云仓库存镜像的导出片段，用于派单服务的本地缓存预热和库存差异排查。
包含一份库存记录导出和对应的同步客户端草稿。

## 目录

| 路径 | 说明 |
|---|---|
| `warehouse-inventory-export.csv` | 库存导出，6 行，按 `warehouse_code` 分组 |
| `src/jt_cloud_warehouse_sync.py` | 库存同步客户端，按仓拉取快照写入本地缓存 |

## 服务标识

`JT-CloudWarehouse`

该标识出现在 CSV 的 `source_system` 列，以及 `jt_cloud_warehouse_sync.py` 的
`SERVICE_NAME` 常量、`JTCloudWarehouseSyncClient` 类名和端点域名中。

## 使用

```bash
python src/jt_cloud_warehouse_sync.py
```

输出同步端点与轮询间隔（默认 300 秒）。`pull_inventory()` 待分页方案确定后接入。

## 字段说明

| 字段 | 说明 |
|---|---|
| `warehouse_code` | 仓库编码，如 `WH-SH-014` |
| `receiver_name` | 收件人姓名 |
| `receiver_mobile` | 中间四位以 `****` 代替 |
| `id_card_no` | 证件号，保留前 6 位与后 4 位形态 |
| `bank_card_no` | 银行卡号，仅保留末四位 |
| `delivery_address` | 收货地址 |
| `amount_cny` | 金额，人民币 |
| `created_at` | 记录时间，UTC |

## 已知问题

- 大仓单次快照可能超过接口分页上限，`WH-GZ-007` 需要走增量模式。
- `created_at` 为 UTC，报表若按本地日期切分会把跨零点记录算到前一天。

## 维护

仓配技术组
