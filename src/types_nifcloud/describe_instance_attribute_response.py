from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class DescribeInstanceAttributeResponse(BaseModel):
    """Response for DescribeInstanceAttribute API"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request_id: Optional[str] = None
    instance_id: Optional[str] = None
    instance_unique_id: Optional[str] = None
    instance_type: Optional[Dict[str, Any]] = None
    disable_api_termination: Optional[Dict[str, Any]] = None
    block_device_mapping: Optional[Dict[str, Any]] = None
    accounting_type: Optional[Dict[str, Any]] = None
    next_month_accounting_type: Optional[Dict[str, Any]] = None
    loadbalancing: Optional[Dict[str, Any]] = None
    copy_info: Optional[Dict[str, Any]] = None
    autoscaling: Optional[Dict[str, Any]] = None
    ip_type: Optional[Dict[str, Any]] = None
    nifty_private_ip_type: Optional[Dict[str, Any]] = None
    group_id: Optional[Dict[str, Any]] = None
    description: Optional[Dict[str, Any]] = None
    network_interface_set: Optional[Dict[str, Any]] = None
    nifty_elastic_load_balancing: Optional[Dict[str, Any]] = None
