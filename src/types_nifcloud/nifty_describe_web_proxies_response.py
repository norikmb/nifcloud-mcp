from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class NiftyDescribeWebProxiesResponse(BaseModel):
    """Response for NiftyDescribeWebProxies API"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request_id: Optional[str] = None
    web_proxies: Optional[Dict[str, Any]] = None
