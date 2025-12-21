"""Response type for DescribeMigrationHubNetworks API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class MigrationHubNetwork(BaseModel):
    """Migration hub network information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    network_id: Optional[str] = None
    cidr_block: Optional[str] = None
    network_type: Optional[str] = None
    status: Optional[str] = None
    extension_status: Optional[str] = None
    created_at: Optional[str] = None


class DescribeMigrationHubNetworksResponse(BaseModel):
    """Response from DescribeMigrationHubNetworks API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    networks: Optional[list[MigrationHubNetwork]] = None
