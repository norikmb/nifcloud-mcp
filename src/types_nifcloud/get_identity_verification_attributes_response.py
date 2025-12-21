"""ESS API Response Types - GetIdentityVerificationAttributes"""

from typing import Any, Optional

from pydantic import BaseModel, Field


class IdentityVerificationAttributes(BaseModel):
    """Verification attributes for an identity."""

    verification_status: Optional[str] = Field(None, alias="VerificationStatus")
    verification_token: Optional[str] = Field(None, alias="VerificationToken")

    class Config:
        populate_by_name = True
        extra = "allow"


class GetIdentityVerificationAttributesResponse(BaseModel):
    """Response from GetIdentityVerificationAttributes API."""

    verification_attributes: Optional[dict[str, Any]] = Field(
        None, alias="VerificationAttributes"
    )

    class Config:
        populate_by_name = True
        extra = "allow"
