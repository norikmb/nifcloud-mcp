"""DNS API Response Types - ListHostedZones"""

from typing import Any, Optional

from pydantic import BaseModel, Field


class HostedZoneConfig(BaseModel):
    """Configuration for a hosted zone."""

    private_zone: Optional[bool] = Field(None, alias="PrivateZone")

    class Config:
        populate_by_name = True
        extra = "allow"


class HostedZone(BaseModel):
    """Hosted zone information."""

    id: Optional[str] = Field(None, alias="Id")
    name: Optional[str] = Field(None, alias="Name")
    caller_reference: Optional[str] = Field(None, alias="CallerReference")
    config: Optional[HostedZoneConfig] = Field(None, alias="Config")
    resource_record_set_count: Optional[int] = Field(None, alias="ResourceRecordSetCount")

    class Config:
        populate_by_name = True
        extra = "allow"


class ListHostedZonesResponse(BaseModel):
    """Response from ListHostedZones API."""

    hosted_zones: Optional[list[HostedZone]] = Field(None, alias="HostedZones")
    marker: Optional[str] = Field(None, alias="Marker")
    is_truncated: Optional[bool] = Field(None, alias="IsTruncated")
    next_marker: Optional[str] = Field(None, alias="NextMarker")
    max_items: Optional[str] = Field(None, alias="MaxItems")

    class Config:
        populate_by_name = True
        extra = "allow"
