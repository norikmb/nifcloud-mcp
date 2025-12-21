"""Response type for DescribeEventSubscriptions API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class EventSubscription(BaseModel):
    """Event subscription information."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    subscription_name: Optional[str] = None
    subscription_arn: Optional[str] = None
    sns_topic_arn: Optional[str] = None
    status: Optional[str] = None
    event_categories: Optional[list[str]] = None
    source_type: Optional[str] = None
    enabled: Optional[bool] = None


class DescribeEventSubscriptionsResponse(BaseModel):
    """Response from DescribeEventSubscriptions API."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    response_metadata: Optional[Dict[str, Any]] = None
    event_subscriptions: Optional[list[EventSubscription]] = None
