# NIFCLOUD MCP Server

## Clineで動かす場合

以下の内容をcline_mcp_settings.jsonに記載
```
{
  "mcpServers": {
    "nifcloud_mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/home/kambe/workspace/nifcloud-mcp",　 <!-- ←ここはgit clone 先のディレクトリを指定-->
        "run",
        "mcp",
        "run",
        "server.py"
      ]
    }
  }
}
```