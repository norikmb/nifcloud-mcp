from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class NiftyDescribeLoadBalancerSSLPoliciesResponse(BaseModel):
    """Response for NiftyDescribeLoadBalancerSSLPolicies API"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request_id: Optional[str] = None
    ssl_policies: Optional[Dict[str, Any]] = None
