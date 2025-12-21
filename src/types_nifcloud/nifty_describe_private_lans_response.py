from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class Tag(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    key: Optional[str] = None
    value: Optional[str] = None


class PrivateLanInstance(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    instance_unique_id: Optional[str] = None
    instance_id: Optional[str] = None
    device_index: Optional[str] = None
    ip_address: Optional[str] = None


class PrivateLanRouter(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    router_id: Optional[str] = None
    router_name: Optional[str] = None
    device_index: Optional[str] = None
    ip_address: Optional[str] = None


class VpnGateway(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    vpn_gateway_id: Optional[str] = None
    nifty_vpn_gateway_name: Optional[str] = None
    device_index: Optional[str] = None
    ip_address: Optional[str] = None


class NetworkInterface(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    network_interface_id: Optional[str] = None
    ip_address: Optional[str] = None


class RemoteAccessVpnGateway(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    remote_access_vpn_gateway_id: Optional[str] = None
    remote_access_vpn_gateway_name: Optional[str] = None
    device_index: Optional[str] = None
    ip_address: Optional[str] = None


class PrivateLan(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    network_id: Optional[str] = None
    private_lan_name: Optional[str] = None
    state: Optional[str] = None
    cidr_block: Optional[str] = None
    availability_zone: Optional[str] = None
    tag_set: Optional[List[Tag]] = None
    accounting_type: Optional[str] = None
    next_month_accounting_type: Optional[str] = None
    description: Optional[str] = None
    instances_set: Optional[List[PrivateLanInstance]] = None
    router_set: Optional[List[PrivateLanRouter]] = None
    vpn_gateway_set: Optional[List[VpnGateway]] = None
    network_interface_set: Optional[List[NetworkInterface]] = None
    remote_access_vpn_gateway_set: Optional[List[RemoteAccessVpnGateway]] = None
    created_time: Optional[str] = None
    sharing_status: Optional[str] = None


class NiftyDescribePrivateLansResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    request_id: Optional[str] = None
    private_lan_set: Optional[List[PrivateLan]] = None
