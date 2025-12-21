from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class DBParameterGroup(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    db_parameter_group_family: Optional[str] = None
    db_parameter_group_name: Optional[str] = None
    description: Optional[str] = None


class DescribeDBParameterGroupsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    db_parameter_groups: Optional[List[DBParameterGroup]] = None
    marker: Optional[str] = None
