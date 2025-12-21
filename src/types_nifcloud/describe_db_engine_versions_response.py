from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class UpgradeTarget(BaseModel):
    auto_upgrade: Optional[bool] = None
    db_parameter_group_family: Optional[str] = None
    description: Optional[str] = None
    engine: Optional[str] = None
    engine_version: Optional[str] = None
    is_major_version_upgrade: Optional[bool] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )


class DBEngineVersion(BaseModel):
    db_engine_description: Optional[str] = None
    db_engine_version_description: Optional[str] = None
    db_parameter_group_family: Optional[str] = None
    engine: Optional[str] = None
    engine_version: Optional[str] = None
    status: Optional[str] = None
    valid_upgrade_target: Optional[List[UpgradeTarget]] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )


class DescribeDBEngineVersionsResult(BaseModel):
    db_engine_versions: Optional[List[DBEngineVersion]] = None
    marker: Optional[str] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )


class DescribeDBEngineVersionsResponse(BaseModel):
    describe_db_engine_versions_result: Optional[DescribeDBEngineVersionsResult] = None
    response_metadata: Optional[dict] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )
