"""Response type for ListEvents API (Catalog)."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class CatalogEvent(BaseModel):
    """Catalog event information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    event_id: Optional[str] = None
    event_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None


class ListEventsResponse(BaseModel):
    """Response from ListEvents API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    events: Optional[list[CatalogEvent]] = None
