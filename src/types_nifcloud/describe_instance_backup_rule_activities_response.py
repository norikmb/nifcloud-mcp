from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class Activity(BaseModel):
    """バックアップアクティビティ情報"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    activity_id: Optional[str] = None
    backup_rule_id: Optional[str] = None
    instance_id: Optional[str] = None
    activity_type: Optional[str] = None
    status: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    description: Optional[str] = None
    error_message: Optional[str] = None


class DescribeInstanceBackupRuleActivitiesResponse(BaseModel):
    """バックアップアクティビティ一覧レスポンス"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    activities: Optional[list[Activity]] = None
    scaling_activity_set: Optional[list[Activity]] = None
    request_id: Optional[str] = None
    response_metadata: Optional[Dict[str, Any]] = None
