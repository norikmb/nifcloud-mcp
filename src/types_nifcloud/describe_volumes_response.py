from pydantic import BaseModel
from datetime import datetime


class AttachmentSet(BaseModel):
    attach_time: str
    delete_on_termination: str
    device: str
    instance_id: str
    instance_unique_id: str
    status: str
    volume_id: str
    volume_unique_id: str


class VolumeSet(BaseModel):
    accounting_type: str
    attachment_set: list[AttachmentSet]
    availability_zone: str
    create_time: datetime
    description: str
    disk_type: str
    next_month_accounting_type: str
    size: str
    snapshot_id: str
    status: str
    volume_id: str
    volume_unique_id: str


class DescribeVolumesResponse(BaseModel):
    request_id: str
    volume_set: list[VolumeSet]
