from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class MultiIpAddressGroup(BaseModel):
    """マルチIPアドレスグループ情報"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    multi_ip_address_group_id: Optional[str] = None
    group_name: Optional[str] = None
    group_description: Optional[str] = None
    instance_id: Optional[str] = None
    network_interface_id: Optional[str] = None
    multi_ip_address_group_status: Optional[str] = None
    ip_address_list: Optional[list[str]] = None
    available_ip_count: Optional[int] = None
    tag_set: Optional[list[Dict[str, Any]]] = None
    create_time: Optional[str] = None


class DescribeMultiIpAddressGroupsResponse(BaseModel):
    """マルチIPアドレスグループ一覧レスポンス"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    multi_ip_address_groups: Optional[list[MultiIpAddressGroup]] = None
    multi_ip_address_group_set: Optional[list[MultiIpAddressGroup]] = None
    request_id: Optional[str] = None
    response_metadata: Optional[Dict[str, Any]] = None
