from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class Address(BaseModel):
    """付替IPアドレス情報"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    public_ip: Optional[str] = None
    domain: Optional[str] = None
    instance_id: Optional[str] = None
    association_id: Optional[str] = None
    network_interface_id: Optional[str] = None
    network_interface_owner_id: Optional[str] = None
    private_ip_address: Optional[str] = None
    allocation_id: Optional[str] = None
    association_is_main: Optional[bool] = None


class DescribeAddressesResponse(BaseModel):
    """付替IPアドレス一覧レスポンス"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    addresses: Optional[list[Address]] = None
    request_id: Optional[str] = None
    response_metadata: Optional[Dict[str, Any]] = None
