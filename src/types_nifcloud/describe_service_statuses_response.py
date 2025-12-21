"""Service Activity API Response Types - DescribeServiceStatuses"""

from typing import Any, Optional

from pydantic import BaseModel, Field


class ServiceStatus(BaseModel):
    """Service status information."""

    service_name: Optional[str] = Field(None, alias="ServiceName")
    status: Optional[str] = Field(None, alias="Status")
    last_update_time: Optional[str] = Field(None, alias="LastUpdateTime")

    class Config:
        populate_by_name = True
        extra = "allow"


class DescribeServiceStatusesResponse(BaseModel):
    """Response from DescribeServiceStatuses API."""

    service_statuses: Optional[list[ServiceStatus]] = Field(None, alias="ServiceStatuses")

    class Config:
        populate_by_name = True
        extra = "allow"
