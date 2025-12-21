"""Response type for DescribeEventCalendar API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class EventDay(BaseModel):
    """Event day information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    date: Optional[str] = None
    event_count: Optional[int] = None


class DescribeEventCalendarResponse(BaseModel):
    """Response from DescribeEventCalendar API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    event_days: Optional[list[EventDay]] = None
    year_month: Optional[str] = None
