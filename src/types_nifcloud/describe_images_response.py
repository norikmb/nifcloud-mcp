from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class BlockDeviceMapping(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    device_name: Optional[str] = None
    ebs: Optional[dict] = None  # EBS詳細情報


class Image(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    image_id: Optional[str] = None
    image_location: Optional[str] = None
    image_state: Optional[str] = None
    image_owner_id: Optional[str] = None
    is_public: Optional[bool] = None
    product_codes: Optional[List[dict]] = None
    architecture: Optional[str] = None
    image_type: Optional[str] = None
    kernel_id: Optional[str] = None
    ramdisk_id: Optional[str] = None
    platform: Optional[str] = None
    state_reason: Optional[dict] = None
    image_owner_alias: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    detail_description: Optional[str] = None
    redistributable: Optional[bool] = None
    placement: Optional[dict] = None
    root_device_type: Optional[str] = None
    root_device_name: Optional[str] = None
    block_device_mapping: Optional[List[BlockDeviceMapping]] = None
    nifty_image_size: Optional[str] = None
    nifty_contact_url: Optional[str] = None
    launch_time: Optional[str] = None
    nifty_distribution_ids: Optional[List[dict]] = None
    nifty_is_allowed_distribution: Optional[bool] = None
    is_gpu_configurable: Optional[bool] = None


class DescribeImagesResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    
    request_id: Optional[str] = None
    images_set: Optional[List[Image]] = None
