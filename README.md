# FJcloud-V MCP Server

[![Actions status](https://github.com/norikmb/nifcloud-mcp/actions/workflows/ruff-action.yml/badge.svg)](https://github.com/norikmb/nifcloud-mcp/actions)

FJcloud-V の API と対話するためのモデル コンテキスト プロトコル (MCP) サーバーです。

## 概要

このプロジェクトは FJcloud-V 上のリソースを効率的に管理・検索するための MCP サーバーです。
Claude や GitHub Copilot などの AI アシスタントと統合して、自然言語でインフラを管理できます。

## 利用可能な Tool

現在は主要サービスの READ 操作（データ取得）に対応しています。

### Computing Service

| Tool 名                  | 説明                                       | ドキュメント                                                                          |
| ------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------- |
| `get_server_list`        | すべてのサーバーインスタンスのリストを取得 | [DescribeInstances](https://docs.nifcloud.com/cp/api/DescribeInstances.htm)           |
| `get_disk_list`          | すべてのディスク/ボリュームのリストを取得  | [DescribeVolumes](https://docs.nifcloud.com/cp/api/DescribeVolumes.htm)               |
| `get_load_balancer_list` | すべてのロードバランサーのリストを取得     | [DescribeLoadBalancers](https://docs.nifcloud.com/cp/api/DescribeLoadBalancers.htm)   |
| `get_firewall_list`      | すべてのセキュリティグループのリストを取得 | [DescribeSecurityGroups](https://docs.nifcloud.com/cp/api/DescribeSecurityGroups.htm) |
| `get_router_list`        | すべてのルーターのリストを取得             | [NiftyDescribeRouters](https://docs.nifcloud.com/cp/api/NiftyDescribeRouters.htm)     |

### RDB Service

| Tool 名       | 説明                                       | ドキュメント                                                                     |
| ------------- | ------------------------------------------ | -------------------------------------------------------------------------------- |
| `get_db_list` | すべてのデータベースサーバーのリストを取得 | [DescribeDBInstances](https://docs.nifcloud.com/rdb/api/DescribeDBInstances.htm) |

### DNS Service

| Tool 名                    | 説明                                                 | ドキュメント                                                 |
| -------------------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| `get_hosted_zones_list`    | すべてのホストゾーン(DNS ゾーン)のリストを取得       | [ListHostedZones](https://docs.nifcloud.com/dns/api/)        |
| `get_resource_record_sets` | 指定したゾーンのすべてのリソースレコードセットを取得 | [ListResourceRecordSets](https://docs.nifcloud.com/dns/api/) |

### NAS Service

| Tool 名                        | 説明                                                | ドキュメント                                                    |
| ------------------------------ | --------------------------------------------------- | --------------------------------------------------------------- |
| `get_nas_instances_list`       | すべての NAS インスタンスのリストを取得             | [DescribeNASInstances](https://docs.nifcloud.com/nas/api/)      |
| `get_nas_security_groups_list` | すべての NAS ファイアウォールグループのリストを取得 | [DescribeNASSecurityGroups](https://docs.nifcloud.com/nas/api/) |

### ESS Service (Email Sending Service)

| Tool 名                                    | 説明                                            | ドキュメント                                                            |
| ------------------------------------------ | ----------------------------------------------- | ----------------------------------------------------------------------- |
| `get_ess_identities_list`                  | 登録済みの送信元アドレス/ドメインのリストを取得 | [ListIdentities](https://docs.nifcloud.com/ess/api/)                    |
| `get_ess_send_quota`                       | 現在の送信上限と送信状況を取得                  | [GetSendQuota](https://docs.nifcloud.com/ess/api/)                      |
| `get_ess_send_statistics`                  | メール送信統計情報を取得                        | [GetSendStatistics](https://docs.nifcloud.com/ess/api/)                 |
| `get_ess_identity_verification_attributes` | メールアドレス/ドメインの検証状態を取得         | [GetIdentityVerificationAttributes](https://docs.nifcloud.com/ess/api/) |

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

### v0.2.0 (最新)

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
