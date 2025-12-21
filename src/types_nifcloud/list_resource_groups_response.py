"""Catalog API Response Types - ListResourceGroups"""

from typing import Optional

from pydantic import BaseModel, Field


class ResourceGroup(BaseModel):
    """Resource group information."""

    resource_group_id: Optional[str] = Field(None, alias="ResourceGroupId")
    resource_group_name: Optional[str] = Field(None, alias="ResourceGroupName")
    description: Optional[str] = Field(None, alias="Description")
    create_time: Optional[str] = Field(None, alias="CreateTime")

    class Config:
        populate_by_name = True
        extra = "allow"


class ListResourceGroupsResponse(BaseModel):
    """Response from ListResourceGroups API."""

    resource_groups: Optional[list[ResourceGroup]] = Field(None, alias="ResourceGroups")
    next_token: Optional[str] = Field(None, alias="NextToken")

    class Config:
        populate_by_name = True
        extra = "allow"
