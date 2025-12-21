"""Response type for DescribeEngineDefaultParameters API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class DefaultParameter(BaseModel):
    """Default parameter information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    parameter_name: Optional[str] = None
    parameter_value: Optional[str] = None
    description: Optional[str] = None
    source: Optional[str] = None
    data_type: Optional[str] = None
    allowed_values: Optional[str] = None
    is_modifiable: Optional[bool] = None


class DescribeEngineDefaultParametersResponse(BaseModel):
    """Response from DescribeEngineDefaultParameters API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    engine_default_parameters: Optional[list[DefaultParameter]] = None
