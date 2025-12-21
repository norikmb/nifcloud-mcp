"""Response type for DescribeOrderableDBInstanceOptions API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class OrderableDBInstanceOption(BaseModel):
    """Orderable DB instance option."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    engine: Optional[str] = None
    engine_version: Optional[str] = None
    db_instance_class: Optional[str] = None
    license_model: Optional[str] = None
    availability_zones: Optional[list[str]] = None
    vpc: Optional[bool] = None
    storage_type: Optional[str] = None
    multi_az: Optional[bool] = None


class DescribeOrderableDBInstanceOptionsResponse(BaseModel):
    """Response from DescribeOrderableDBInstanceOptions API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    orderable_db_instance_options: Optional[list[OrderableDBInstanceOption]] = None
