"""DNS API Response Types - ListResourceRecordSets"""

from typing import Any, Optional

from pydantic import BaseModel, Field


class ResourceRecord(BaseModel):
    """A resource record value."""

    value: Optional[str] = Field(None, alias="Value")

    class Config:
        populate_by_name = True
        extra = "allow"


class ResourceRecordSet(BaseModel):
    """A resource record set."""

    name: Optional[str] = Field(None, alias="Name")
    type: Optional[str] = Field(None, alias="Type")
    set_identifier: Optional[str] = Field(None, alias="SetIdentifier")
    weight: Optional[int] = Field(None, alias="Weight")
    region: Optional[str] = Field(None, alias="Region")
    ttl: Optional[int] = Field(None, alias="TTL")
    resource_records: Optional[list[ResourceRecord]] = Field(None, alias="ResourceRecords")
    alias_target: Optional[dict[str, Any]] = Field(None, alias="AliasTarget")

    class Config:
        populate_by_name = True
        extra = "allow"


class ListResourceRecordSetsResponse(BaseModel):
    """Response from ListResourceRecordSets API."""

    resource_record_sets: Optional[list[ResourceRecordSet]] = Field(
        None, alias="ResourceRecordSets"
    )
    is_truncated: Optional[bool] = Field(None, alias="IsTruncated")
    next_record_name: Optional[str] = Field(None, alias="NextRecordName")
    next_record_type: Optional[str] = Field(None, alias="NextRecordType")
    max_items: Optional[str] = Field(None, alias="MaxItems")

    class Config:
        populate_by_name = True
        extra = "allow"
