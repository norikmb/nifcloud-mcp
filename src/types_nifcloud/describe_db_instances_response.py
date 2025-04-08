from datetime import datetime
from pydantic import BaseModel


class DBParameterGroup(BaseModel):
    db_parameter_group_name: str
    parameter_apply_status: str


class DBSecurityGroup(BaseModel):
    db_security_group_name: str
    status: str


class Endpoint(BaseModel):
    address: str
    nifty_private_address: str
    port: int


class ExternalReplicationInfo(BaseModel):
    external_master_address: str | None = None
    external_replication_message: str | None = None
    external_replication_status: str | None = None
    replication_addresses: list[str]
    replication_private_addresses: list[str]


class OptionGroupMembership(BaseModel):
    option_group_name: str
    status: str


class PendingModifiedValues(BaseModel):
    allocated_storage: int | None = None
    backup_retention_period: int | None = None
    db_instance_class: str | None = None
    db_instance_identifier: str | None = None
    engine_version: str | None = None
    master_user_password: str | None = None
    multi_az: bool | None = None
    port: int | None = None


class StatusInfo(BaseModel):
    message: str
    normal: bool
    status: str
    status_type: str


class DBInstance(BaseModel):
    accounting_type: str
    allocated_storage: int
    auto_minor_version_upgrade: bool
    availability_zone: str
    backup_retention_period: int
    binlog_retention_period: int | None = None
    ca_certificate_identifier: str | None = None
    db_instance_class: str
    db_instance_identifier: str
    db_instance_status: str
    db_name: str
    db_parameter_groups: list[DBParameterGroup]
    db_security_groups: list[DBSecurityGroup]
    endpoint: Endpoint
    engine: str
    engine_version: str
    external_replication_info: ExternalReplicationInfo | None = None
    instance_create_time: datetime
    latest_restorable_time: datetime | None = None
    license_model: str
    master_username: str
    multi_az: bool | None = None
    next_month_accounting_type: str
    nifty_master_private_address: str | None = None
    nifty_multi_az_type: str | None = None
    nifty_network_id: str | None = None
    nifty_slave_private_address: str | None = None
    nifty_storage_type: int
    option_group_memberships: list[OptionGroupMembership]
    pending_modified_values: PendingModifiedValues | None = None
    preferred_backup_window: str
    preferred_maintenance_window: str
    publicly_accessible: bool
    read_replica_db_instance_identifiers: list[str] | None = None
    read_replica_source_db_instance_identifier: str | None = None
    secondary_availability_zone: str | None = None
    status_infos: list[StatusInfo] | None = None
    vpc_security_groups: str


class DescribeDBInstancesResponse(BaseModel):
    db_instances: list[DBInstance]
    marker: str | None = None
