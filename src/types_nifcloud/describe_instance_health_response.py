from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class DescribeInstanceHealthResponse(BaseModel):
    """Response for DescribeInstanceHealth API"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request_id: Optional[str] = None
    instance_states: Optional[Dict[str, Any]] = None
