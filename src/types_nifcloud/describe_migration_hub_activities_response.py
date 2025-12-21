"""Response type for DescribeMigrationHubActivities API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class MigrationActivity(BaseModel):
    """Migration activity information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    activity_id: Optional[str] = None
    activity_type: Optional[str] = None
    status: Optional[str] = None
    timestamp: Optional[str] = None
    description: Optional[str] = None
    resource_id: Optional[str] = None


class DescribeMigrationHubActivitiesResponse(BaseModel):
    """Response from DescribeMigrationHubActivities API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    activities: Optional[list[MigrationActivity]] = None
