"""DevOps with GitLab API Response Types - ListParameterGroups"""

from typing import Optional

from pydantic import BaseModel, Field


class ParameterGroup(BaseModel):
    """Parameter group information."""

    parameter_group_id: Optional[str] = Field(None, alias="ParameterGroupId")
    parameter_group_name: Optional[str] = Field(None, alias="ParameterGroupName")
    description: Optional[str] = Field(None, alias="Description")

    class Config:
        populate_by_name = True
        extra = "allow"


class ListParameterGroupsResponse(BaseModel):
    """Response from ListParameterGroups API."""

    parameter_groups: Optional[list[ParameterGroup]] = Field(None, alias="ParameterGroups")

    class Config:
        populate_by_name = True
        extra = "allow"
