"""Response type for GetDeliveryLog API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class DeliveryLogEntry(BaseModel):
    """Delivery log entry."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    timestamp: Optional[str] = None
    message_id: Optional[str] = None
    recipient: Optional[str] = None
    status: Optional[str] = None
    diagnostic_code: Optional[str] = None
    delivery_status: Optional[str] = None
    bounce_type: Optional[str] = None


class GetDeliveryLogResponse(BaseModel):
    """Response from GetDeliveryLog API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    delivery_logs: Optional[list[DeliveryLogEntry]] = None
