"""DevOps with GitLab API Response Types - ListBackups"""

from typing import Optional

from pydantic import BaseModel, Field


class BackupFile(BaseModel):
    """Backup file information."""

    backup_id: Optional[str] = Field(None, alias="BackupId")
    backup_name: Optional[str] = Field(None, alias="BackupName")
    instance_id: Optional[str] = Field(None, alias="InstanceId")
    create_time: Optional[str] = Field(None, alias="CreateTime")
    backup_status: Optional[str] = Field(None, alias="BackupStatus")

    class Config:
        populate_by_name = True
        extra = "allow"


class ListBackupsResponse(BaseModel):
    """Response from ListBackups API."""

    backups: Optional[list[BackupFile]] = Field(None, alias="Backups")

    class Config:
        populate_by_name = True
        extra = "allow"
