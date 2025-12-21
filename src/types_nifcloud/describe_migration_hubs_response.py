"""Live Migration API Response Types - DescribeMigrationHubs"""

from typing import Any, Optional

from pydantic import BaseModel, Field


class MigrationHub(BaseModel):
    """Migration Hub information."""

    migration_hub_id: Optional[str] = Field(None, alias="MigrationHubId")
    migration_hub_name: Optional[str] = Field(None, alias="MigrationHubName")
    migration_hub_status: Optional[str] = Field(None, alias="MigrationHubStatus")
    create_time: Optional[str] = Field(None, alias="CreateTime")
    description: Optional[str] = Field(None, alias="Description")

    class Config:
        populate_by_name = True
        extra = "allow"


class DescribeMigrationHubsResponse(BaseModel):
    """Response from DescribeMigrationHubs API."""

    migration_hubs: Optional[list[MigrationHub]] = Field(None, alias="MigrationHubs")

    class Config:
        populate_by_name = True
        extra = "allow"
