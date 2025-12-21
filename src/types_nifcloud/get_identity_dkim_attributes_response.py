"""Response type for GetIdentityDkimAttributes API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class DkimAttribute(BaseModel):
    """DKIM attribute information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    dkim_enabled: Optional[bool] = None
    dkim_tokens: Optional[list[str]] = None
    dkim_verification_status: Optional[str] = None


class DkimAttributes(BaseModel):
    """DKIM attributes for identities."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    attributes: Optional[Dict[str, DkimAttribute]] = None


class GetIdentityDkimAttributesResponse(BaseModel):
    """Response from GetIdentityDkimAttributes API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    dkim_attributes: Optional[DkimAttributes] = None
