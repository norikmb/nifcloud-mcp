"""Response type for DescribeEventCategories API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class EventCategory(BaseModel):
    """Event category information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    category_id: Optional[str] = None
    category_name: Optional[str] = None
    description: Optional[str] = None


class DescribeEventCategoriesResponse(BaseModel):
    """Response from DescribeEventCategories API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    event_categories: Optional[list[EventCategory]] = None
