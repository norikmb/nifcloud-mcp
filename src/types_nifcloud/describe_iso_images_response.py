from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class IsoImageInstance(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    instance_id: Optional[str] = None
    instance_unique_id: Optional[str] = None


class IsoImage(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    iso_image_id: Optional[str] = None
    iso_image_name: Optional[str] = None
    iso_image_size: Optional[str] = None
    status: Optional[str] = None
    instances_set: Optional[List[IsoImageInstance]] = None
    description: Optional[str] = None
    created_time: Optional[str] = None
    expired_time: Optional[str] = None
    availability_zone: Optional[str] = None


class DescribeIsoImagesResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    request_id: Optional[str] = None
    iso_images_set: Optional[List[IsoImage]] = None
