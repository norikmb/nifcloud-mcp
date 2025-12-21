from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class FAQItem(BaseModel):
    """FAQ Item information"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    faq_id: Optional[str] = None
    faq_number: Optional[int] = None
    title: Optional[str] = None
    summary: Optional[str] = None
    url: Optional[str] = None
    publish_date: Optional[str] = None
    update_date: Optional[str] = None


class ListFAQItemsResponse(BaseModel):
    """Response for FAQ items listing in a category"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    category_id: Optional[str] = None
    category_name: Optional[str] = None
    faq_items: Optional[List[FAQItem]] = None
    total_count: Optional[int] = None
    current_page: Optional[int] = None
    total_pages: Optional[int] = None
