from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class FAQCategory(BaseModel):
    """FAQ Category information"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    category_id: Optional[str] = None
    category_name: Optional[str] = None
    item_count: Optional[int] = None


class ListFAQCategoriesResponse(BaseModel):
    """Response for FAQ categories listing"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    categories: Optional[List[FAQCategory]] = None
    total_count: Optional[int] = None
