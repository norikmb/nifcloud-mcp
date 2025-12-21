from typing import Optional, Dict, Any, List
from pydantic import BaseModel, ConfigDict


class ResourceInfo(BaseModel):
    instance_item_set: Optional[List[Dict[str, Any]]] = None
    dynamic_ip_count: Optional[int] = None
    customize_image_count: Optional[int] = None
    add_disk_count: Optional[int] = None
    add_disk_total_size: Optional[int] = None
    router_item_set: Optional[List[Dict[str, Any]]] = None
    vpn_gateway_item_set: Optional[List[Dict[str, Any]]] = None
    network_flow_amount: Optional[int] = None
    security_group_count: Optional[int] = None
    load_balancer_count: Optional[int] = None
    elastic_ip_item_set: Optional[List[Dict[str, Any]]] = None
    ssl_cert_count: Optional[int] = None
    monitoring_rule_count: Optional[int] = None
    auto_scale_count: Optional[int] = None
    private_lan_count: Optional[int] = None
    private_lan_classic_count: Optional[int] = None
    premium_support_set: Optional[List[Dict[str, Any]]] = None
    nifty_multi_account_count: Optional[int] = None
    elastic_load_balancer_count: Optional[int] = None
    network_interface_item_set: Optional[List[Dict[str, Any]]] = None
    instance_backup_rule_count: Optional[int] = None
    remote_access_vpn_gateway_set: Optional[List[Dict[str, Any]]] = None
    multi_ip_address_item_set: Optional[List[Dict[str, Any]]] = None
    migration_hub_item_set: Optional[List[Dict[str, Any]]] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )


class DescribeResourcesResponse(BaseModel):
    request_id: Optional[str] = None
    resource_info: Optional[ResourceInfo] = None
    response_metadata: Optional[dict] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )
