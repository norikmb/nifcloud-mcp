from pydantic import BaseModel
from datetime import datetime


class GroupSet(BaseModel):
    group_id: str


class Autoscaling(BaseModel):
    auto_scaling_group_name: str
    expire_time: datetime


class Ebs(BaseModel):
    attach_time: str
    delete_on_termination: str
    status: str
    volume_id: str
    volume_unique_id: str


class BlockDeviceMapping(BaseModel):
    device_name: str
    ebs: Ebs


class InstanceBackupRule(BaseModel):
    instance_backup_rule_id: str | None = None
    instance_backup_rule_name: str | None = None


class InstanceState(BaseModel):
    code: int
    name: str


class IsoImage(BaseModel):
    iso_image_id: str
    iso_image_name: str


class Loadbalancing(BaseModel):
    instance_port: int
    load_balancer_name: str
    load_balancer_port: int
    state: str


class Monitoring(BaseModel):
    state: str


class MultiIpAddressGroup(BaseModel):
    multi_ip_address_group_id: str | None = None
    multi_ip_address_group_name: str | None = None


class Association(BaseModel):
    ip_owner_id: str
    public_dns_name: str
    public_ip: str
    public_ip_v6: str


class Attachment(BaseModel):
    attach_time: str | None = None
    attachment_id: str | None = None
    delete_on_termination: str
    device_index: str
    status: str


class PrivateIpAddressesSet(BaseModel):
    association: Association
    primary: bool
    private_dns_name: str
    private_ip_address: str


class MultiIpAddressesSet(BaseModel):
    ip_address: str


class NetworkInterface(BaseModel):
    association: Association | None = None
    attachment: Attachment | None = None
    description: str
    group_set: list[GroupSet]
    mac_address: str
    multi_ip_addresses_set: list[MultiIpAddressesSet]
    network_interface_id: str | None = None
    nifty_network_id: str | None = None
    nifty_network_name: str | None = None
    owner_id: str
    private_dns_name: str
    private_ip_address: str
    private_ip_address_v6: str
    private_ip_addresses_set: list[PrivateIpAddressesSet]
    source_dest_check: str
    status: str
    subnet_id: str
    vpc_id: str


class NiftyElasticLoadBalancing(BaseModel):
    elastic_load_balancer_id: str
    elastic_load_balancer_name: str
    elastic_load_balancer_port: int
    instance_port: int
    protocol: str


class NiftySnapshotting(BaseModel):
    state: str


class Placement(BaseModel):
    availability_zone: str


class ProductCode(BaseModel):
    product_code: str


class StateReason(BaseModel):
    code: str
    message: str


class VmTools(BaseModel):
    state: str
    version: str


class InstanceSet(BaseModel):
    accounting_type: str
    ami_launch_index: str
    architecture: str
    autoscaling: Autoscaling | None = None
    block_device_mapping: list[BlockDeviceMapping]
    copy_info: str | None = None
    description: str
    dns_name: str
    hot_add: str
    image_id: str
    image_name: str
    instance_backup_rule: InstanceBackupRule
    instance_id: str
    instance_lifecycle: str
    instance_state: InstanceState
    instance_type: str
    instance_unique_id: str
    ip_address: str
    ip_address_v6: str
    ip_type: str
    is_gpu_configurable: bool
    iso_image_set: list[IsoImage]
    kernel_id: str
    key_name: str
    launch_time: datetime
    loadbalancing: list[Loadbalancing]
    monitoring: Monitoring
    multi_ip_address_group: MultiIpAddressGroup
    network_interface_set: list[NetworkInterface]
    next_month_accounting_type: str
    nifty_elastic_load_balancing: list[NiftyElasticLoadBalancing]
    nifty_private_ip_type: str
    nifty_private_network_type: str
    nifty_snapshotting: list[NiftySnapshotting] | None = None
    placement: Placement
    platform: str
    private_dns_name: str
    private_ip_address: str
    private_ip_address_v6: str
    product_codes: list[ProductCode]
    ramdisk_id: str
    reason: str
    root_device_name: str
    root_device_type: str
    spot_instance_request_id: str
    state_reason: StateReason
    subnet_id: str
    tenancy: str
    vm_tools: VmTools
    vpc_id: str


class ReservationSet(BaseModel):
    group_set: list[GroupSet]
    instances_set: list[InstanceSet]
    owner_id: str
    reservation_id: str


class DescribeInstancesResponse(BaseModel):
    request_id: str
    reservation_set: list[ReservationSet]
