from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class KeyPairInstance(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    instance_id: Optional[str] = None
    region_name: Optional[str] = None


class KeyPair(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    key_name: Optional[str] = None
    key_fingerprint: Optional[str] = None
    description: Optional[str] = None
    instances_set: Optional[List[KeyPairInstance]] = None


class DescribeKeyPairsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    request_id: Optional[str] = None
    key_set: Optional[List[KeyPair]] = None
