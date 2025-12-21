"""Response type for DescribeEventAttributes API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class EventAttribute(BaseModel):
    """Event attribute information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    event_id: Optional[str] = None
    event_type: Optional[str] = None
    event_date: Optional[str] = None
    title: Optional[str] = None
    message: Optional[str] = None
    service: Optional[str] = None


class DescribeEventAttributesResponse(BaseModel):
    """Response from DescribeEventAttributes API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    event_attributes: Optional[list[EventAttribute]] = None
