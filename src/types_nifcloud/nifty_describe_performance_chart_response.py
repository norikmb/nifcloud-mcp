from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class NiftyDescribePerformanceChartResponse(BaseModel):
    """Response for NiftyDescribePerformanceChart API"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request_id: Optional[str] = None
    metric_data: Optional[Dict[str, Any]] = None
