"""Response type for GetInstanceMetrics API (DevOps)."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class Datapoint(BaseModel):
    """Metric datapoint."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    timestamp: Optional[str] = None
    value: Optional[float] = None
    unit: Optional[str] = None


class Metric(BaseModel):
    """Metric information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    metric_name: Optional[str] = None
    datapoints: Optional[list[Datapoint]] = None


class GetInstanceMetricsResponse(BaseModel):
    """Response from GetInstanceMetrics API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    metrics: Optional[list[Metric]] = None
