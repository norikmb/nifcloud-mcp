from pydantic import BaseModel
from datetime import datetime


class BackupInformation(BaseModel):
    expiration_date: datetime | None = None
    is_backup: bool


class Group(BaseModel):
    group_id: str


class NetworkInterface(BaseModel):
    cidr_block: str | None = None
    description: str | None = None
    device_index: str
    dhcp: bool | None = None
    dhcp_config_id: str | None = None
    dhcp_options_id: str | None = None
    ip_address: str
    network_id: str
    network_name: str


class Tag(BaseModel):
    key: str
    value: str


class VersionInformation(BaseModel):
    is_latest: bool
    version: str


class Router(BaseModel):
    accounting_type: str
    availability_zone: str
    backup_information: BackupInformation
    created_time: datetime
    description: str
    group_set: list[Group]
    nat_table_association_id: str | None = None
    nat_table_id: str | None = None
    network_interface_set: list[NetworkInterface]
    next_month_accounting_type: str
    route_table_association_id: str | None = None
    route_table_id: str | None = None
    router_id: str
    router_name: str
    state: str
    tag_set: list[Tag]
    type: str
    version_information: VersionInformation


class NiftyDescribeRoutersResponse(BaseModel):
    request_id: str
    router_set: list[Router]
