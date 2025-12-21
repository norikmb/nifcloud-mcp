"""Object Storage Service API Response Types - GetService (List Buckets)"""

from typing import Optional

from pydantic import BaseModel, Field


class Bucket(BaseModel):
    """Bucket information."""

    name: Optional[str] = Field(None, alias="Name")
    creation_date: Optional[str] = Field(None, alias="CreationDate")

    class Config:
        populate_by_name = True
        extra = "allow"


class GetServiceResponse(BaseModel):
    """Response from GetService API (list buckets)."""

    buckets: Optional[list[Bucket]] = Field(None, alias="Buckets")
    owner: Optional[dict] = Field(None, alias="Owner")

    class Config:
        populate_by_name = True
        extra = "allow"
