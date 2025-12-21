"""DevOps with GitLab API Response Types - ListRunners"""

from typing import Optional

from pydantic import BaseModel, Field


class Runner(BaseModel):
    """Runner information."""

    runner_id: Optional[str] = Field(None, alias="RunnerId")
    runner_name: Optional[str] = Field(None, alias="RunnerName")
    runner_status: Optional[str] = Field(None, alias="RunnerStatus")
    instance_type: Optional[str] = Field(None, alias="InstanceType")
    create_time: Optional[str] = Field(None, alias="CreateTime")

    class Config:
        populate_by_name = True
        extra = "allow"


class ListRunnersResponse(BaseModel):
    """Response from ListRunners API."""

    runners: Optional[list[Runner]] = Field(None, alias="Runners")

    class Config:
        populate_by_name = True
        extra = "allow"
