from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class DBSnapshot(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    allocated_storage: Optional[int] = None
    availability_zone: Optional[str] = None
    db_instance_identifier: Optional[str] = None
    db_snapshot_identifier: Optional[str] = None
    engine: Optional[str] = None
    engine_version: Optional[str] = None
    instance_create_time: Optional[str] = None
    license_model: Optional[str] = None
    master_username: Optional[str] = None
    option_group_name: Optional[str] = None
    port: Optional[int] = None
    snapshot_create_time: Optional[str] = None
    snapshot_type: Optional[str] = None
    status: Optional[str] = None


class DescribeDBSnapshotsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    db_snapshots: Optional[List[DBSnapshot]] = None
    marker: Optional[str] = None
