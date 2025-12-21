from typing import Optional, List, Dict, Any
from pydantic import BaseModel, ConfigDict


class DescribeUsageResponse(BaseModel):
    request_id: Optional[str] = None
    year_month: Optional[str] = None
    instance_info: Optional[Dict[str, Any]] = None
    image_info: Optional[Dict[str, Any]] = None
    volume_info: Optional[Dict[str, Any]] = None
    network_info: Optional[Dict[str, Any]] = None
    security_group_info: Optional[Dict[str, Any]] = None
    load_balancer_info: Optional[Dict[str, Any]] = None
    elastic_ip_info: Optional[Dict[str, Any]] = None
    auto_scale_info: Optional[Dict[str, Any]] = None
    ssl_cert_info: Optional[Dict[str, Any]] = None
    private_lan_info: Optional[Dict[str, Any]] = None
    charge_detail_info: Optional[Dict[str, Any]] = None
    premium_support_info: Optional[Dict[str, Any]] = None
    multi_account_info: Optional[Dict[str, Any]] = None
    pattern_auth_info: Optional[Dict[str, Any]] = None
    os_option_charge_info: Optional[Dict[str, Any]] = None
    extra_charge_info: Optional[Dict[str, Any]] = None
    license_info: Optional[Dict[str, Any]] = None
    option_common_info: Optional[Dict[str, Any]] = None
    option_info: Optional[Dict[str, Any]] = None
    internet_vpn_info: Optional[Dict[str, Any]] = None
    snapshot_info: Optional[Dict[str, Any]] = None
    private_network_info: Optional[Dict[str, Any]] = None
    router_info: Optional[Dict[str, Any]] = None
    vpn_gateway_info: Optional[Dict[str, Any]] = None
    elastic_load_balancer_info: Optional[Dict[str, Any]] = None
    network_interface_info: Optional[Dict[str, Any]] = None
    instance_backup_info: Optional[Dict[str, Any]] = None
    remote_access_vpn_gateway_info: Optional[Dict[str, Any]] = None
    multi_ip_address_info: Optional[Dict[str, Any]] = None
    live_migration_info: Optional[Dict[str, Any]] = None
    response_metadata: Optional[dict] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )
