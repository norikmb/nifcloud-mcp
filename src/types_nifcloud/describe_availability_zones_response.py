from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class AvailabilityZone(BaseModel):
    """アベイラビリティゾーン情報"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    zone_name: Optional[str] = None
    zone_state: Optional[str] = None
    region_name: Optional[str] = None
    messages: Optional[list[str]] = None


class DescribeAvailabilityZonesResponse(BaseModel):
    """アベイラビリティゾーン一覧レスポンス"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    availability_zones: Optional[list[AvailabilityZone]] = None
    availability_zone_info: Optional[list[AvailabilityZone]] = None
    request_id: Optional[str] = None
    response_metadata: Optional[Dict[str, Any]] = None
