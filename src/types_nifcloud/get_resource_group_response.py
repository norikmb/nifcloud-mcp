"""Response type for GetResourceGroup API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class ResourceGroupInfo(BaseModel):
    """Resource group information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    group_id: Optional[str] = None
    group_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    resource_count: Optional[int] = None


class GetResourceGroupResponse(BaseModel):
    """Response from GetResourceGroup API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    resource_group: Optional[ResourceGroupInfo] = None
