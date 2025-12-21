"""NAS API Response Types - DescribeNASInstances"""

from typing import Any, Optional

from pydantic import BaseModel, Field


class NASInstance(BaseModel):
    """NAS instance information."""

    nas_instance_id: Optional[str] = Field(None, alias="NASInstanceId")
    nas_instance_name: Optional[str] = Field(None, alias="NASInstanceName")
    nas_instance_status: Optional[str] = Field(None, alias="NASInstanceStatus")
    nas_instance_description: Optional[str] = Field(None, alias="NASInstanceDescription")
    nas_instance_type: Optional[str] = Field(None, alias="NASInstanceType")
    mount_point: Optional[str] = Field(None, alias="MountPoint")
    allocated_storage: Optional[int] = Field(None, alias="AllocatedStorage")
    used_storage: Optional[int] = Field(None, alias="UsedStorage")
    availability_zone: Optional[str] = Field(None, alias="AvailabilityZone")
    create_time: Optional[str] = Field(None, alias="CreateTime")
    update_time: Optional[str] = Field(None, alias="UpdateTime")

    class Config:
        populate_by_name = True
        extra = "allow"


class DescribeNASInstancesResponse(BaseModel):
    """Response from DescribeNASInstances API."""

    nas_instances: Optional[list[NASInstance]] = Field(None, alias="NASInstances")

    class Config:
        populate_by_name = True
        extra = "allow"
