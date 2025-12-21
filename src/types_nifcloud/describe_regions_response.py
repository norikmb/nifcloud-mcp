from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class Region(BaseModel):
    """リージョン情報"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    region_name: Optional[str] = None
    endpoint: Optional[str] = None
    status: Optional[str] = None


class DescribeRegionsResponse(BaseModel):
    """リージョン一覧レスポンス"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    regions: Optional[list[Region]] = None
    region_info: Optional[list[Region]] = None
    request_id: Optional[str] = None
    response_metadata: Optional[Dict[str, Any]] = None
