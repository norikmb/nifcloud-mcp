"""DevOps with GitLab API Response Types - ListInstances"""

from typing import Optional

from pydantic import BaseModel, Field


class DevOpsInstance(BaseModel):
    """DevOps server instance information."""

    instance_id: Optional[str] = Field(None, alias="InstanceId")
    instance_name: Optional[str] = Field(None, alias="InstanceName")
    instance_status: Optional[str] = Field(None, alias="InstanceStatus")
    instance_type: Optional[str] = Field(None, alias="InstanceType")
    availability_zone: Optional[str] = Field(None, alias="AvailabilityZone")
    create_time: Optional[str] = Field(None, alias="CreateTime")

    class Config:
        populate_by_name = True
        extra = "allow"


class ListInstancesResponse(BaseModel):
    """Response from ListInstances API."""

    instances: Optional[list[DevOpsInstance]] = Field(None, alias="Instances")

    class Config:
        populate_by_name = True
        extra = "allow"
