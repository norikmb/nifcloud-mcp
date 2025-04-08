# FJcloud-V MCP Server
[![Actions status](https://github.com/norikmb/nifcloud-mcp/actions/workflows/ruff-action.yml/badge.svg)](https://github.com/norikmb/nifcloud-mcp/actions)

FJcloud-V の API と対話するためのモデル コンテキスト プロトコル (MCP) サーバー

## 利用可能なTool

| Tool 名 | 説明 | 必須パラメータ |
|-----------|-------------|---------------------|
| `get_server_list` | すべてのサーバーのリストを取得します | None |
| `get_disk_list` | すべてのディスクのリストを取得します | None |
| `get_load_balancers_list` | すべてのLBのリストを取得します | None |
| `get_firewall_list` | すべてのFWのリストを取得します | None |
| `get_router_list` | すべてのルーターのリストを取得します | None |
| `get_db_list` | すべてのRDBのリストを取得します | None |

## Clineとの統合

以下の内容をcline_mcp_settings.jsonに記載する

```
{
  "mcpServers": {
    "nifcloud_mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/home/kambe/nifcloud-mcp",　 <!-- ←ここはgit clone 先のディレクトリを指定-->
        "run",
        "mcp",
        "run",
        "server.py"
      ]
    }
  }
}
```
