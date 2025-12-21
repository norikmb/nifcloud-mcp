from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class DescribeRemoteAccessVpnGatewayClientConfigResponse(BaseModel):
    """Response for DescribeRemoteAccessVpnGatewayClientConfig API"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request_id: Optional[str] = None
    client_config: Optional[Dict[str, Any]] = None
