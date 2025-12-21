from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class NiftyDescribeAlarmHistoryResponse(BaseModel):
    """Response for NiftyDescribeAlarmHistory API"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request_id: Optional[str] = None
    alarm_history: Optional[Dict[str, Any]] = None
