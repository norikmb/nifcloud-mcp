from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class BackupRule(BaseModel):
    """バックアップルール情報"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    backup_rule_id: Optional[str] = None
    instance_id: Optional[str] = None
    rule_name: Optional[str] = None
    start_time: Optional[str] = None
    backup_type: Optional[str] = None
    backup_cycle: Optional[str] = None
    backup_time: Optional[str] = None
    retention_period: Optional[int] = None
    status: Optional[str] = None
    tag_set: Optional[list[Dict[str, Any]]] = None
    create_time: Optional[str] = None


class DescribeInstanceBackupRulesResponse(BaseModel):
    """バックアップルール一覧レスポンス"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    backup_rules: Optional[list[BackupRule]] = None
    instance_backup_rule_set: Optional[list[BackupRule]] = None
    request_id: Optional[str] = None
    response_metadata: Optional[Dict[str, Any]] = None
