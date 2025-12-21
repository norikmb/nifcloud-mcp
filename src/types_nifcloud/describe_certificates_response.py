"""Response type for DescribeCertificates API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class Certificate(BaseModel):
    """Certificate information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    certificate_identifier: Optional[str] = None
    certificate_type: Optional[str] = None
    thumbprint: Optional[str] = None
    valid_from: Optional[str] = None
    valid_till: Optional[str] = None
    source_arn: Optional[str] = None


class DescribeCertificatesResponse(BaseModel):
    """Response from DescribeCertificates API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    certificates: Optional[list[Certificate]] = None
