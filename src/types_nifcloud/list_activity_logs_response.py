"""Response type for ListActivityLogs API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class ActivityLog(BaseModel):
    """Activity log information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    log_id: Optional[str] = None
    timestamp: Optional[str] = None
    user_id: Optional[str] = None
    action: Optional[str] = None
    resource_id: Optional[str] = None
    resource_type: Optional[str] = None
    status: Optional[str] = None
    details: Optional[str] = None


class ListActivityLogsResponse(BaseModel):
    """Response from ListActivityLogs API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    activity_logs: Optional[list[ActivityLog]] = None
