from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class DescribeSslCertificatesResponse(BaseModel):
    """Response for DescribeSslCertificates API"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request_id: Optional[str] = None
    ssl_certificates: Optional[Dict[str, Any]] = None
