"""NAS API Response Types - DescribeNASSecurityGroups"""

from typing import Any, Optional

from pydantic import BaseModel, Field


class IPRange(BaseModel):
    """IP range for NAS security group."""

    cidr_ip: Optional[str] = Field(None, alias="CidrIp")

    class Config:
        populate_by_name = True
        extra = "allow"


class SecurityGroupIngress(BaseModel):
    """Ingress rule for NAS security group."""

    protocol: Optional[str] = Field(None, alias="Protocol")
    from_port: Optional[int] = Field(None, alias="FromPort")
    to_port: Optional[int] = Field(None, alias="ToPort")
    cidr_ip: Optional[str] = Field(None, alias="CidrIp")
    nas_security_group_name: Optional[str] = Field(None, alias="NASSecurityGroupName")

    class Config:
        populate_by_name = True
        extra = "allow"


class NASSecurityGroup(BaseModel):
    """NAS security group information."""

    nas_security_group_id: Optional[str] = Field(None, alias="NASSecurityGroupId")
    nas_security_group_name: Optional[str] = Field(None, alias="NASSecurityGroupName")
    nas_security_group_description: Optional[str] = Field(
        None, alias="NASSecurityGroupDescription"
    )
    nas_security_group_status: Optional[str] = Field(None, alias="NASSecurityGroupStatus")
    ingress: Optional[list[SecurityGroupIngress]] = Field(None, alias="Ingress")

    class Config:
        populate_by_name = True
        extra = "allow"


class DescribeNASSecurityGroupsResponse(BaseModel):
    """Response from DescribeNASSecurityGroups API."""

    nas_security_groups: Optional[list[NASSecurityGroup]] = Field(
        None, alias="NASSecurityGroups"
    )

    class Config:
        populate_by_name = True
        extra = "allow"
