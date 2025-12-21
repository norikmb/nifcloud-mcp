# FJcloud-V MCP Server

[![Actions status](https://github.com/norikmb/nifcloud-mcp/actions/workflows/ruff-action.yml/badge.svg)](https://github.com/norikmb/nifcloud-mcp/actions)

FJcloud-V の API と対話するためのモデル コンテキスト プロトコル (MCP) サーバーです。

## 概要

このプロジェクトは FJcloud-V 上のリソースを効率的に管理・検索するための MCP サーバーです。
Claude や GitHub Copilot などの AI アシスタントと統合して、自然言語でインフラを管理できます。

## 利用可能な Tool

現在は主要サービスの READ 操作（データ取得）に対応しています。全 77 ツール実装済み。

### Computing Service (31 ツール)

| Tool 名                                       | 説明                                       | ドキュメント                                                                                                      |
| --------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `get_server_list`                             | すべてのサーバーインスタンスのリストを取得 | [DescribeInstances](https://docs.nifcloud.com/cp/api/DescribeInstances.htm)                                       |
| `get_disk_list`                               | すべてのディスク/ボリュームのリストを取得  | [DescribeVolumes](https://docs.nifcloud.com/cp/api/DescribeVolumes.htm)                                           |
| `get_load_balancer_list`                      | すべてのロードバランサーのリストを取得     | [DescribeLoadBalancers](https://docs.nifcloud.com/cp/api/DescribeLoadBalancers.htm)                               |
| `get_firewall_list`                           | すべてのセキュリティグループのリストを取得 | [DescribeSecurityGroups](https://docs.nifcloud.com/cp/api/DescribeSecurityGroups.htm)                             |
| `get_router_list`                             | すべてのルーターのリストを取得             | [NiftyDescribeRouters](https://docs.nifcloud.com/cp/api/NiftyDescribeRouters.htm)                                 |
| `get_images_list`                             | すべての OS イメージのリストを取得         | [DescribeImages](https://docs.nifcloud.com/cp/api/DescribeImages.htm)                                             |
| `get_key_pairs_list`                          | すべての SSH キーペアのリストを取得        | [DescribeKeyPairs](https://docs.nifcloud.com/cp/api/DescribeKeyPairs.htm)                                         |
| `get_iso_images_list`                         | すべての ISO イメージのリストを取得        | [DescribeIsoImages](https://docs.nifcloud.com/cp/api/DescribeIsoImages.htm)                                       |
| `get_private_lans_list`                       | すべてのプライベート LAN のリストを取得    | [NiftyDescribePrivateLans](https://docs.nifcloud.com/cp/api/NiftyDescribePrivateLans.htm)                         |
| `get_usage`                                   | リソース利用状況（料金情報含む）を取得     | [DescribeUsage](https://docs.nifcloud.com/cp/api/DescribeUsage.htm)                                               |
| `get_resources`                               | リソース利用状況（ダッシュボード）を取得   | [DescribeResources](https://docs.nifcloud.com/cp/api/DescribeResources.htm)                                       |
| `get_event_calendar`                          | サービスイベント情報（カレンダー形式）     | [DescribeEventCalendar](https://docs.nifcloud.com/service-activity/api/)                                          |
| `get_event_attributes`                        | サービスイベント情報（リスト形式）         | [DescribeEventAttributes](https://docs.nifcloud.com/service-activity/api/)                                        |
| `get_addresses_list`                          | すべての付替 IP アドレスのリストを取得     | [DescribeAddresses](https://docs.nifcloud.com/cp/api/DescribeAddresses.htm)                                       |
| `get_network_interfaces_list`                 | すべてのネットワークインターフェースを取得 | [DescribeNetworkInterfaces](https://docs.nifcloud.com/cp/api/DescribeNetworkInterfaces.htm)                       |
| `get_multi_ip_address_groups_list`            | すべてのマルチ IP アドレスグループを取得   | [DescribeMultiIpAddressGroups](https://docs.nifcloud.com/cp/api/DescribeMultiIpAddressGroups.htm)                 |
| `get_availability_zones`                      | すべてのアベイラビリティゾーンを取得       | [DescribeAvailabilityZones](https://docs.nifcloud.com/cp/api/DescribeAvailabilityZones.htm)                       |
| `get_regions`                                 | すべてのリージョンを取得                   | [DescribeRegions](https://docs.nifcloud.com/cp/api/DescribeRegions.htm)                                           |
| `get_associated_users`                        | 共有アクセスを持つユーザー情報を取得       | [DescribeAssociatedUsers](https://docs.nifcloud.com/cp/api/DescribeAssociatedUsers.htm)                           |
| `get_instance_backup_rules`                   | バックアップルール設定情報を取得           | [DescribeInstanceBackupRules](https://docs.nifcloud.com/cp/api/DescribeInstanceBackupRules.htm)                   |
| `get_instance_backup_rule_activities`         | バックアップアクティビティログを取得       | [DescribeInstanceBackupRuleActivities](https://docs.nifcloud.com/cp/api/DescribeInstanceBackupRuleActivities.htm) |
| `get_instance_attribute`                      | サーバーの詳細情報を取得                   | [DescribeInstanceAttribute](https://docs.nifcloud.com/cp/api/DescribeInstanceAttribute.htm)                       |
| `get_uploads`                                 | アップロード中のタスク情報を取得           | [DescribeUploads](https://docs.nifcloud.com/cp/api/DescribeUploads.htm)                                           |
| `get_instance_health`                         | ロードバランサーのヘルスチェック結果を取得 | [DescribeInstanceHealth](https://docs.nifcloud.com/cp/api/DescribeInstanceHealth.htm)                             |
| `get_ssl_certificates`                        | すべての SSL 証明書のリストを取得          | [DescribeSslCertificates](https://docs.nifcloud.com/cp/api/DescribeSslCertificates.htm)                           |
| `get_ssl_certificate_attribute`               | SSL 証明書の詳細情報を取得                 | [DescribeSslCertificateAttribute](https://docs.nifcloud.com/cp/api/DescribeSslCertificateAttribute.htm)           |
| `get_load_balancer_ssl_policies`              | ロードバランサー SSL ポリシーを取得        | [NiftyDescribeLoadBalancerSSLPolicies](https://docs.nifcloud.com/cp/api/)                                         |
| `get_performance_chart`                       | パフォーマンスチャートデータを取得         | [NiftyDescribePerformanceChart](https://docs.nifcloud.com/cp/api/)                                                |
| `get_alarm_history`                           | アラーム履歴を取得                         | [NiftyDescribeAlarmHistory](https://docs.nifcloud.com/cp/api/)                                                    |
| `get_alarm_rules_activities`                  | 監視ルールのアクティビティログを取得       | [NiftyDescribeAlarmRulesActivities](https://docs.nifcloud.com/cp/api/)                                            |
| `get_user_activities`                         | API 利用履歴を取得                         | [DescribeUserActivities](https://docs.nifcloud.com/cp/api/DescribeUserActivities.htm)                             |
| `get_web_proxies`                             | ルーターの Web プロキシ設定を取得          | [NiftyDescribeWebProxies](https://docs.nifcloud.com/cp/api/)                                                      |
| `get_remote_access_vpn_gateway_client_config` | リモートアクセス VPN 設定ファイルを取得    | [DescribeRemoteAccessVpnGatewayClientConfig](https://docs.nifcloud.com/cp/api/)                                   |

### RDB Service (13 ツール)

| Tool 名                             | 説明                                        | ドキュメント                                                                                 |
| ----------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `get_db_list`                       | すべてのデータベースサーバーのリストを取得  | [DescribeDBInstances](https://docs.nifcloud.com/rdb/api/DescribeDBInstances.htm)             |
| `get_db_snapshots_list`             | すべてのデータベーススナップショットを取得  | [DescribeDBSnapshots](https://docs.nifcloud.com/rdb/api/DescribeDBSnapshots.htm)             |
| `get_db_parameter_groups_list`      | すべてのパラメーターグループのリストを取得  | [DescribeDBParameterGroups](https://docs.nifcloud.com/rdb/api/DescribeDBParameterGroups.htm) |
| `get_db_security_groups_list`       | すべての RDB ファイアウォールのリストを取得 | [DescribeDBSecurityGroups](https://docs.nifcloud.com/rdb/api/DescribeDBSecurityGroups.htm)   |
| `get_db_parameters`                 | DB パラメーターグループのパラメーター取得   | [DescribeDBParameters](https://docs.nifcloud.com/rdb/api/DescribeDBParameters.htm)           |
| `get_db_engine_versions`            | DB エンジンバージョン情報を取得             | [DescribeDBEngineVersions](https://docs.nifcloud.com/rdb/api/DescribeDBEngineVersions.htm)   |
| `get_db_event_categories`           | DB イベントカテゴリ情報を取得               | [DescribeEventCategories](https://docs.nifcloud.com/rdb/api/)                                |
| `get_orderable_db_instance_options` | オーダー可能な DB オプションを取得          | [DescribeOrderableDBInstanceOptions](https://docs.nifcloud.com/rdb/api/)                     |
| `get_db_certificates`               | CA 証明書情報を取得                         | [DescribeCertificates](https://docs.nifcloud.com/rdb/api/)                                   |
| `get_db_events`                     | DB イベント情報を取得                       | [DescribeEvents](https://docs.nifcloud.com/rdb/api/)                                         |
| `get_db_event_subscriptions`        | DB イベント通知サブスク情報を取得           | [DescribeEventSubscriptions](https://docs.nifcloud.com/rdb/api/)                             |
| `get_db_log_files`                  | DB ログファイル一覧を取得                   | [DescribeDBLogFiles](https://docs.nifcloud.com/rdb/api/)                                     |
| `get_engine_default_parameters`     | DB エンジンデフォルトパラメータを取得       | [DescribeEngineDefaultParameters](https://docs.nifcloud.com/rdb/api/)                        |

### DNS Service (4 ツール)

| Tool 名                    | 説明                                                 | ドキュメント                                                         |
| -------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------- |
| `get_hosted_zones_list`    | すべてのホストゾーン(DNS ゾーン)のリストを取得       | [ListHostedZones](https://docs.nifcloud.com/dns/api/)                |
| `get_resource_record_sets` | 指定したゾーンのすべてのリソースレコードセットを取得 | [ListResourceRecordSets](https://docs.nifcloud.com/dns/api/)         |
| `get_hosted_zone`          | 特定のホストゾーン情報を取得                         | [GetHostedZone](https://docs.nifcloud.com/dns/api/GetHostedZone.htm) |
| `get_dns_change`           | DNS 更新リクエスト情報を取得                         | [GetChange](https://docs.nifcloud.com/dns/api/GetChange.htm)         |

### NAS Service (2 ツール)

| Tool 名                        | 説明                                                | ドキュメント                                                    |
| ------------------------------ | --------------------------------------------------- | --------------------------------------------------------------- |
| `get_nas_instances_list`       | すべての NAS インスタンスのリストを取得             | [DescribeNASInstances](https://docs.nifcloud.com/nas/api/)      |
| `get_nas_security_groups_list` | すべての NAS ファイアウォールグループのリストを取得 | [DescribeNASSecurityGroups](https://docs.nifcloud.com/nas/api/) |

### ESS Service (6 ツール)

| Tool 名                                    | 説明                                            | ドキュメント                                                            |
| ------------------------------------------ | ----------------------------------------------- | ----------------------------------------------------------------------- |
| `get_ess_identities_list`                  | 登録済みの送信元アドレス/ドメインのリストを取得 | [ListIdentities](https://docs.nifcloud.com/ess/api/)                    |
| `get_ess_send_quota`                       | 現在の送信上限と送信状況を取得                  | [GetSendQuota](https://docs.nifcloud.com/ess/api/)                      |
| `get_ess_send_statistics`                  | メール送信統計情報を取得                        | [GetSendStatistics](https://docs.nifcloud.com/ess/api/)                 |
| `get_ess_identity_verification_attributes` | メールアドレス/ドメインの検証状態を取得         | [GetIdentityVerificationAttributes](https://docs.nifcloud.com/ess/api/) |
| `get_ess_identity_dkim_attributes`         | DKIM 設定情報を取得                             | [GetIdentityDkimAttributes](https://docs.nifcloud.com/ess/api/)         |
| `get_ess_delivery_log`                     | メール配信ログを取得                            | [GetDeliveryLog](https://docs.nifcloud.com/ess/api/)                    |

### Object Storage Service (1 ツール)

| Tool 名                           | 説明                           | ドキュメント                                                        |
| --------------------------------- | ------------------------------ | ------------------------------------------------------------------- |
| `get_object_storage_buckets_list` | すべてのバケットのリストを取得 | [GetService](https://docs.nifcloud.com/object-storage-service/api/) |

### Live Migration Service (4 ツール)

| Tool 名                        | 説明                                    | ドキュメント                                                                   |
| ------------------------------ | --------------------------------------- | ------------------------------------------------------------------------------ |
| `get_migration_hubs_list`      | すべてのマイグレーションハブを取得      | [DescribeMigrationHubs](https://docs.nifcloud.com/livemigration/api/)          |
| `get_migration_hub_networks`   | マイグレーション hub ネットワーク情報   | [DescribeMigrationHubNetworks](https://docs.nifcloud.com/livemigration/api/)   |
| `get_migration_hub_activities` | マイグレーション hub アクティビティ情報 | [DescribeMigrationHubActivities](https://docs.nifcloud.com/livemigration/api/) |
| （予約）                       |                                         |                                                                                |

### Catalog Service (5 ツール)

| Tool 名                            | 説明                               | ドキュメント                                                 |
| ---------------------------------- | ---------------------------------- | ------------------------------------------------------------ |
| `get_catalog_resource_groups_list` | すべてのリソースグループを取得     | [ListResourceGroups](https://docs.nifcloud.com/catalog/api/) |
| `get_catalog_templates_list`       | すべてのテンプレートのリストを取得 | [ListTemplates](https://docs.nifcloud.com/catalog/api/)      |
| `get_catalog_resource_group`       | 特定のリソースグループ情報を取得   | [GetResourceGroup](https://docs.nifcloud.com/catalog/api/)   |
| `get_catalog_events`               | Catalog イベント情報を取得         | [ListEvents](https://docs.nifcloud.com/catalog/api/)         |
| `get_catalog_activity_logs`        | Catalog アクティビティログを取得   | [ListActivityLogs](https://docs.nifcloud.com/catalog/api/)   |

### Service Activity (2 ツール)

| Tool 名                | 説明                                     | ドキュメント                                                               |
| ---------------------- | ---------------------------------------- | -------------------------------------------------------------------------- |
| `get_service_statuses` | すべてのサービスの稼働状況を取得         | [DescribeServiceStatuses](https://docs.nifcloud.com/service-activity/api/) |
| `get_event_calendar`   | サービスイベント（カレンダー形式）を取得 | [DescribeEventCalendar](https://docs.nifcloud.com/service-activity/api/)   |
| `get_event_attributes` | サービスイベント（リスト形式）を取得     | [DescribeEventAttributes](https://docs.nifcloud.com/service-activity/api/) |

### Resource & Support Information (1 ツール)

| Tool 名                  | 説明                                                          | 情報内容                                                     |
| ------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------ |
| `get_nifcloud_resources` | NIFCLOUD ドキュメント、サポートリソース、問い合わせ情報を取得 | ドキュメントリンク、サポートチャネル、連絡先、その他リソース |

### DevOps with GitLab Service (6 ツール)

| Tool 名                            | 説明                                               | ドキュメント                                                 |
| ---------------------------------- | -------------------------------------------------- | ------------------------------------------------------------ |
| `get_devops_instances_list`        | すべての DevOps サーバーインスタンスのリストを取得 | [ListInstances](https://docs.nifcloud.com/devops/api/)       |
| `get_devops_parameter_groups_list` | すべてのパラメーターグループのリストを取得         | [ListParameterGroups](https://docs.nifcloud.com/devops/api/) |
| `get_devops_firewall_groups_list`  | すべてのファイアウォールグループのリストを取得     | [ListFirewallGroups](https://docs.nifcloud.com/devops/api/)  |
| `get_devops_backups_list`          | すべてのバックアップファイルのリストを取得         | [ListBackups](https://docs.nifcloud.com/devops/api/)         |
| `get_devops_runners_list`          | すべての GitLab CI/CD ランナーのリストを取得       | [ListRunners](https://docs.nifcloud.com/devops/api/)         |
| `get_devops_instance_metrics`      | DevOps インスタンスメトリクス情報を取得            | [GetInstanceMetrics](https://docs.nifcloud.com/devops/api/)  |

### Support FAQ (2 ツール)

| Tool 名              | 説明                                    | 情報源                                                         |
| -------------------- | --------------------------------------- | -------------------------------------------------------------- |
| `get_faq_categories` | サポート FAQ カテゴリ一覧を取得         | [FAQ Categories](https://faq.support.nifcloud.com/)            |
| `get_faq_items`      | 指定カテゴリ内の FAQ アイテム一覧を取得 | [FAQ Items](https://faq.support.nifcloud.com/category/show/93) |

## セットアップ

### 前提条件

- Python 3.10 以上
- `uv` パッケージマネージャー（[インストール方法](https://docs.astral.sh/uv/getting-started/installation/)）
- FJcloud-V のアクセスキーとシークレットキー

### インストール

```bash
# リポジトリのクローン
git clone https://github.com/norikmb/nifcloud-mcp.git
cd nifcloud-mcp

# 依存関係のインストール
uv sync
```

### 環境設定

`.env` ファイルを作成して FJcloud-V の認証情報を設定します：

```env
NIFCLOUD_ACCESS_KEY_ID=your-access-key-id
NIFCLOUD_SECRET_ACCESS_KEY=your-secret-access-key
NIFCLOUD_DEFAULT_REGION=jp-east-1
```

## 使用方法

### Cline との統合

`cline_mcp_settings.json` に以下の内容を追加します：

```json
{
  "mcpServers": {
    "nifcloud_mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/nifcloud-mcp",
        "run",
        "mcp",
        "run",
        "src/server.py"
      ]
    }
  }
}
```

### GitHub Copilot Chat との統合

`.vscode/mcp.json` に以下の内容を追加します：

```json
{
  "servers": {
    "nifcloud_mcp": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/nifcloud-mcp",
        "run",
        "mcp",
        "run",
        "src/server.py"
      ]
    }
  }
}
```

## 開発

### テストの実行

```bash
# すべてのテストを実行
uv run pytest tests/ -v

# カバレッジレポート付きで実行
uv run pytest tests/ --cov=src --cov-report=html
```

### コードのフォーマット・リント

```bash
# Ruff でコードをリント
uv run ruff check src/

# Ruff で自動フォーマット
uv run ruff format src/
```

## アーキテクチャ

- `src/server.py`: MCP サーバーのエントリーポイントと Tool 定義
- `src/utils.py`: FJcloud-V API 呼び出しのヘルパー関数とキー変換
- `src/settings.py`: 環境変数からの設定読み込み
- `src/types_nifcloud/`: API レスポンスの型定義

## 改善履歴

### v0.4.0 (最新)

- ✅ **読み取り専用 Tool さらに拡張: 29 → 32 ツール (+3)**
  - Computing Service に 1 つの新 Tool を追加:
    - `get_private_lans_list`: プライベート LAN 情報取得
  - RDB Service に 2 つの新 Tool を追加:
    - `get_db_parameter_groups_list`: DB パラメーターグループ情報取得
    - `get_db_security_groups_list`: RDB ファイアウォール情報取得
- ✅ 新規 Pydantic 型定義 (3 ファイル)
  - `nifty_describe_private_lans_response.py`
  - `describe_db_parameter_groups_response.py`
  - `describe_db_security_groups_response.py`
- ✅ ドキュメント完全更新

### v0.3.0

- ✅ **読み取り専用 Tool 大幅拡張: 25 → 29 ツール**
  - Computing Service に 3 つの新 Tool を追加:
    - `get_images_list`: OS イメージ情報取得
    - `get_key_pairs_list`: SSH キーペア情報取得
    - `get_iso_images_list`: ISO イメージ情報取得
  - RDB Service に 1 つの新 Tool を追加:
    - `get_db_snapshots_list`: データベーススナップショット情報取得
- ✅ 新規 Pydantic 型定義 (4 ファイル)
  - `describe_images_response.py`
  - `describe_key_pairs_response.py`
  - `describe_iso_images_response.py`
  - `describe_db_snapshots_response.py`
- ✅ ドキュメント完全更新

### v0.2.0

- ✅ パッケージを最新バージョンに更新
  - mcp: 1.6.0 → 1.25.0
  - pydantic: 2.11.2 → 2.12.5
  - nifcloud: 1.16.0 → 1.17.0
  - ruff: 0.11.4 → 0.14.10
- ✅ コード重複排除（DRY 原則）
  - `call_nifcloud_api()` / `get_nifcloud_client()` ヘルパー関数を作成
  - Tool コードを 1 行に簡潔化
- ✅ エラーハンドリング強化
  - 全 API 呼び出しに try-except を追加
  - 詳細なエラーログを実装
- ✅ ロギング機能の追加
  - 構造化ログフォーマットで トラブルシューティングを容易に
- ✅ テストコードの追加
  - pytest で 23 個のテストを実装
  - utils と server の両モジュールをカバー
- ✅ ドキュメント完全更新

## ライセンス

MIT

## サポート

問題や機能リクエストは [GitHub Issues](https://github.com/norikmb/nifcloud-mcp/issues) で報告してください。
