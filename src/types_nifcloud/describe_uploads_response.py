from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class DescribeUploadsResponse(BaseModel):
    """Response for DescribeUploads API"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request_id: Optional[str] = None
    uploads: Optional[Dict[str, Any]] = None
