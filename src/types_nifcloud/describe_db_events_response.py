"""Response type for DescribeEvents API (RDB)."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class DBEvent(BaseModel):
    """DB event information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_identifier: Optional[str] = None
    source_type: Optional[str] = None
    message: Optional[str] = None
    event_categories: Optional[list[str]] = None
    date: Optional[str] = None


class DescribeDBEventsResponse(BaseModel):
    """Response from DescribeEvents API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    events: Optional[list[DBEvent]] = None
