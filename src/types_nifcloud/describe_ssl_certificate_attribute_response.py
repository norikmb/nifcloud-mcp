from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class DescribeSslCertificateAttributeResponse(BaseModel):
    """Response for DescribeSslCertificateAttribute API"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request_id: Optional[str] = None
    certificate_detail: Optional[Dict[str, Any]] = None
