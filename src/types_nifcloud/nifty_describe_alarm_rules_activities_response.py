from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class NiftyDescribeAlarmRulesActivitiesResponse(BaseModel):
    """Response for NiftyDescribeAlarmRulesActivities API"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request_id: Optional[str] = None
    alarm_rules_activities: Optional[Dict[str, Any]] = None
