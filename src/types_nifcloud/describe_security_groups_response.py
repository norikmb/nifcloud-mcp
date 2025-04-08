from pydantic import BaseModel
from datetime import datetime


class InstanceUniqueId(BaseModel):
    instance_unique_id: str


class InstanceId(BaseModel):
    instance_id: str


class IpRange(BaseModel):
    cidr_ip: str


class Group(BaseModel):
    group_name: str
    user_id: str


class IpPermission(BaseModel):
    add_datetime: datetime
    description: str
    from_port: int
    groups: list[Group] | None = None
    in_out: str
    ip_protocol: str
    ip_ranges: list[IpRange] | None = None
    to_port: int


class Router(BaseModel):
    router_id: str
    router_name: str


class VpnGateway(BaseModel):
    nifty_vpn_gateway_name: str
    vpn_gateway_id: str


class SecurityGroupInfo(BaseModel):
    availability_zone: str
    group_description: str
    group_log_filter_broadcast: bool
    group_log_filter_net_bios: bool
    group_log_limit: int
    group_name: str
    group_rule_limit: int
    group_status: str
    instance_unique_ids_set: list[InstanceUniqueId]
    instances_set: list[InstanceId]
    ip_permissions: list[IpPermission]
    owner_id: str
    router_set: list[Router] | None = None
    vpn_gateway_set: list[VpnGateway] | None = None


class DescribeSecurityGroupsResponse(BaseModel):
    request_id: str
    security_group_info: list[SecurityGroupInfo]
