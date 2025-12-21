from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class Parameter(BaseModel):
    allowed_values: Optional[str] = None
    apply_method: Optional[str] = None
    apply_type: Optional[str] = None
    data_type: Optional[str] = None
    description: Optional[str] = None
    is_modifiable: Optional[bool] = None
    minimum_engine_version: Optional[str] = None
    parameter_name: Optional[str] = None
    parameter_value: Optional[str] = None
    source: Optional[str] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )


class DescribeDBParametersResult(BaseModel):
    marker: Optional[str] = None
    parameters: Optional[List[Parameter]] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )


class DescribeDBParametersResponse(BaseModel):
    describe_db_parameters_result: Optional[DescribeDBParametersResult] = None
    response_metadata: Optional[dict] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )
