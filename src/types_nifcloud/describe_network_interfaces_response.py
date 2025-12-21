from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class NetworkInterface(BaseModel):
    """ネットワークインターフェース情報"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    network_interface_id: Optional[str] = None
    subnet_id: Optional[str] = None
    vpc_id: Optional[str] = None
    status: Optional[str] = None
    mac_address: Optional[str] = None
    private_ip_address: Optional[str] = None
    description: Optional[str] = None
    attachment: Optional[Dict[str, Any]] = None
    groups: Optional[list[Dict[str, Any]]] = None
    private_ip_addresses: Optional[list[Dict[str, Any]]] = None
    source_dest_check: Optional[bool] = None
    tag_set: Optional[list[Dict[str, Any]]] = None
    owner_id: Optional[str] = None


class DescribeNetworkInterfacesResponse(BaseModel):
    """ネットワークインターフェース一覧レスポンス"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    network_interfaces: Optional[list[NetworkInterface]] = None
    network_interface_set: Optional[list[NetworkInterface]] = None
    request_id: Optional[str] = None
    response_metadata: Optional[Dict[str, Any]] = None
