"""Catalog API Response Types - ListTemplates"""

from typing import Optional

from pydantic import BaseModel, Field


class Template(BaseModel):
    """Template information."""

    template_id: Optional[str] = Field(None, alias="TemplateId")
    template_name: Optional[str] = Field(None, alias="TemplateName")
    description: Optional[str] = Field(None, alias="Description")
    create_time: Optional[str] = Field(None, alias="CreateTime")

    class Config:
        populate_by_name = True
        extra = "allow"


class ListTemplatesResponse(BaseModel):
    """Response from ListTemplates API."""

    templates: Optional[list[Template]] = Field(None, alias="Templates")
    next_token: Optional[str] = Field(None, alias="NextToken")

    class Config:
        populate_by_name = True
        extra = "allow"
