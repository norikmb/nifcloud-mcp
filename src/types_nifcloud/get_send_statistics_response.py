"""ESS API Response Types - GetSendStatistics"""

from typing import Any, Optional

from pydantic import BaseModel, Field


class SendDataPoint(BaseModel):
    """Send statistics data point."""

    timestamp: Optional[str] = Field(None, alias="Timestamp")
    bounces: Optional[int] = Field(None, alias="Bounces")
    complaints: Optional[int] = Field(None, alias="Complaints")
    delivery_attempts: Optional[int] = Field(None, alias="DeliveryAttempts")
    rejects: Optional[int] = Field(None, alias="Rejects")

    class Config:
        populate_by_name = True
        extra = "allow"


class GetSendStatisticsResponse(BaseModel):
    """Response from GetSendStatistics API."""

    send_data_points: Optional[list[SendDataPoint]] = Field(None, alias="SendDataPoints")

    class Config:
        populate_by_name = True
        extra = "allow"
