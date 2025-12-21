"""ESS API Response Types - GetSendQuota"""

from typing import Optional

from pydantic import BaseModel, Field


class GetSendQuotaResponse(BaseModel):
    """Response from GetSendQuota API."""

    max_24_hour_send: Optional[float] = Field(None, alias="Max24HourSend")
    max_send_rate: Optional[float] = Field(None, alias="MaxSendRate")
    sent_last_24_hour: Optional[float] = Field(None, alias="SentLast24Hour")

    class Config:
        populate_by_name = True
        extra = "allow"
