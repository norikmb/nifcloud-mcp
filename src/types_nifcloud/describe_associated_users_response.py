from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class AssociatedUser(BaseModel):
    """共有ユーザー情報"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    user_id: Optional[str] = None
    user_name: Optional[str] = None
    description: Optional[str] = None


class DescribeAssociatedUsersResponse(BaseModel):
    """共有ユーザー一覧レスポンス"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    associated_users: Optional[list[AssociatedUser]] = None
    associated_user_set: Optional[list[AssociatedUser]] = None
    request_id: Optional[str] = None
    response_metadata: Optional[Dict[str, Any]] = None
