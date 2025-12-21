from typing import Optional, Dict, Any
from pydantic import BaseModel, ConfigDict


class HostedZone(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    caller_reference: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
    resource_record_set_count: Optional[int] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )


class GetHostedZoneResponse(BaseModel):
    hosted_zone: Optional[HostedZone] = None
    delegation_set: Optional[Dict[str, Any]] = None
    response_metadata: Optional[dict] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )
