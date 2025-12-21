"""ESS API Response Types - ListIdentities"""

from typing import Optional

from pydantic import BaseModel, Field


class ListIdentitiesResponse(BaseModel):
    """Response from ListIdentities API."""

    identities: Optional[list[str]] = Field(None, alias="Identities")
    is_truncated: Optional[bool] = Field(None, alias="IsTruncated")
    next_token: Optional[str] = Field(None, alias="NextToken")

    class Config:
        populate_by_name = True
        extra = "allow"
