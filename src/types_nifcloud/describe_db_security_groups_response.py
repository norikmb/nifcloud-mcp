from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class EC2SecurityGroupElement(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    ec2_security_group_name: Optional[str] = None
    ec2_security_group_owner_id: Optional[str] = None
    status: Optional[str] = None


class IPRange(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    cidrip: Optional[str] = None
    status: Optional[str] = None


class DBSecurityGroup(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    db_security_group_description: Optional[str] = None
    db_security_group_name: Optional[str] = None
    ec2_security_groups: Optional[List[EC2SecurityGroupElement]] = None
    ip_ranges: Optional[List[IPRange]] = None
    owner_id: Optional[str] = None
    nifty_availability_zone: Optional[str] = None


class DescribeDBSecurityGroupsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    db_security_groups: Optional[List[DBSecurityGroup]] = None
    marker: Optional[str] = None
