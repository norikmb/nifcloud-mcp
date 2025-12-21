"""DevOps with GitLab API Response Types - ListFirewallGroups"""

from typing import Optional

from pydantic import BaseModel, Field


class FirewallRule(BaseModel):
    """Firewall rule information."""

    protocol: Optional[str] = Field(None, alias="Protocol")
    from_port: Optional[int] = Field(None, alias="FromPort")
    to_port: Optional[int] = Field(None, alias="ToPort")
    cidr_ip: Optional[str] = Field(None, alias="CidrIp")

    class Config:
        populate_by_name = True
        extra = "allow"


class FirewallGroup(BaseModel):
    """Firewall group information."""

    firewall_group_id: Optional[str] = Field(None, alias="FirewallGroupId")
    firewall_group_name: Optional[str] = Field(None, alias="FirewallGroupName")
    description: Optional[str] = Field(None, alias="Description")
    firewall_rules: Optional[list[FirewallRule]] = Field(None, alias="FirewallRules")

    class Config:
        populate_by_name = True
        extra = "allow"


class ListFirewallGroupsResponse(BaseModel):
    """Response from ListFirewallGroups API."""

    firewall_groups: Optional[list[FirewallGroup]] = Field(None, alias="FirewallGroups")

    class Config:
        populate_by_name = True
        extra = "allow"
