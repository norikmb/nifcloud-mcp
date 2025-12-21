"""Resource Information - Documentation and Support Resources"""

from typing import Optional

from pydantic import BaseModel, Field


class SupportResource(BaseModel):
    """Support and resource information."""

    category: str
    title: str
    description: Optional[str] = None
    url: str


class ResourceInformation(BaseModel):
    """NIFCLOUD Resource and Support Information."""

    documentation: list[SupportResource] = Field(
        default=[
            SupportResource(
                category="Documentation",
                title="API Documentation",
                description="Comprehensive API reference for all NIFCLOUD services",
                url="https://docs.nifcloud.com/api/",
            ),
            SupportResource(
                category="Documentation",
                title="All Services Documentation",
                description="Complete documentation for all NIFCLOUD services",
                url="https://docs.nifcloud.com/",
            ),
            SupportResource(
                category="Documentation",
                title="Common Specifications",
                description="Common technical specifications and limitations",
                url="https://docs.nifcloud.com/common/spec/",
            ),
            SupportResource(
                category="Documentation",
                title="CLI Documentation",
                description="Command-line tool documentation",
                url="https://docs.nifcloud.com/cli/",
            ),
            SupportResource(
                category="Documentation",
                title="SDK Documentation",
                description="Software Development Kit documentation",
                url="https://docs.nifcloud.com/sdk/",
            ),
        ]
    )

    support_channels: list[SupportResource] = Field(
        default=[
            SupportResource(
                category="Support",
                title="Support Portal",
                description="Customer support website for FJcloud-V",
                url="https://customer.nifcloud.com/",
            ),
            SupportResource(
                category="Support",
                title="FAQ",
                description="Frequently asked questions",
                url="https://faq.support.nifcloud.com/",
            ),
            SupportResource(
                category="Support",
                title="Inquiry Form",
                description="General inquiries and consultation",
                url="https://pfs.nifcloud.com/inquiry/support.htm",
            ),
        ]
    )

    contact_info: dict = Field(
        default={
            "phone": "0120-22-1200",
            "business_hours": "平日 9:00～17:45",
            "description": "For FJcloud-V customers",
        }
    )

    resources: list[SupportResource] = Field(
        default=[
            SupportResource(
                category="Resources",
                title="News",
                description="Latest news and updates",
                url="https://pfs.nifcloud.com/cs/catalog/cloud_news/top/1.htm",
            ),
            SupportResource(
                category="Resources",
                title="Events & Seminars",
                description="Upcoming seminars and events",
                url="https://pfs.nifcloud.com/seminar/",
            ),
            SupportResource(
                category="Resources",
                title="Estimate Simulator",
                description="Cost calculation tool",
                url="https://estimate.nifcloud.com/web",
            ),
            SupportResource(
                category="Resources",
                title="Downloads",
                description="Materials and ebooks",
                url="https://pfs.nifcloud.com/dl/",
            ),
        ]
    )

    class Config:
        populate_by_name = True
        extra = "allow"
