from typing import Optional, Dict, Any
from pydantic import BaseModel, ConfigDict


class Change(BaseModel):
    id: Optional[str] = None
    status: Optional[str] = None
    submitted_at: Optional[str] = None
    comment: Optional[str] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )


class GetChangeResponse(BaseModel):
    change: Optional[Change] = None
    response_metadata: Optional[dict] = None

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow"
    )
