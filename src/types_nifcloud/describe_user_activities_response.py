from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class DescribeUserActivitiesResponse(BaseModel):
    """Response for DescribeUserActivities API"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request_id: Optional[str] = None
    user_activities: Optional[Dict[str, Any]] = None
