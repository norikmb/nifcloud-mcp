# server.py
import logging
from typing import Optional

from mcp.server.fastmcp import FastMCP

from .types_nifcloud.describe_db_instances_response import DescribeDBInstancesResponse
from .types_nifcloud.describe_instances_response import DescribeInstancesResponse
from .types_nifcloud.describe_load_balancers_response import (
    DescribeLoadBalancersResponse,
)
from .types_nifcloud.describe_volumes_response import DescribeVolumesResponse
from .types_nifcloud.nifty_describe_routers_response import NiftyDescribeRoutersResponse
from .types_nifcloud.describe_security_groups_response import (
    DescribeSecurityGroupsResponse,
)
from .types_nifcloud.describe_hosted_zones_response import ListHostedZonesResponse
from .types_nifcloud.list_resource_record_sets_response import (
    ListResourceRecordSetsResponse,
)
from .types_nifcloud.describe_nas_instances_response import DescribeNASInstancesResponse
from .types_nifcloud.describe_nas_security_groups_response import (
    DescribeNASSecurityGroupsResponse,
)
from .types_nifcloud.list_identities_response import ListIdentitiesResponse
from .types_nifcloud.get_identity_verification_attributes_response import (
    GetIdentityVerificationAttributesResponse,
)
from .types_nifcloud.get_send_quota_response import GetSendQuotaResponse
from .types_nifcloud.get_send_statistics_response import GetSendStatisticsResponse
from .utils import call_nifcloud_api

# Configure logging with structured format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

mcp = FastMCP("FJcloud-V MCP", log_level="ERROR")


@mcp.tool()
def get_server_list() -> Optional[DescribeInstancesResponse]:
    """List of all servers in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeInstances.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_instances", DescribeInstancesResponse)
    except Exception as e:
        logger.error(f"Failed to get server list: {e}")
        raise


@mcp.tool()
def get_disk_list() -> Optional[DescribeVolumesResponse]:
    """List of all disks in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeVolumes.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_volumes", DescribeVolumesResponse)
    except Exception as e:
        logger.error(f"Failed to get disk list: {e}")
        raise


@mcp.tool()
def get_load_balancer_list() -> Optional[DescribeLoadBalancersResponse]:
    """List of all load balancers in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeLoadBalancers.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_load_balancers", DescribeLoadBalancersResponse)
    except Exception as e:
        logger.error(f"Failed to get load balancer list: {e}")
        raise


@mcp.tool()
def get_firewall_list() -> Optional[DescribeSecurityGroupsResponse]:
    """List of all firewalls in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeSecurityGroups.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_security_groups", DescribeSecurityGroupsResponse)
    except Exception as e:
        logger.error(f"Failed to get firewall list: {e}")
        raise


@mcp.tool()
def get_router_list() -> Optional[NiftyDescribeRoutersResponse]:
    """List of all routers in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/NiftyDescribeRouters.htm
    """
    try:
        return call_nifcloud_api("computing", "nifty_describe_routers", NiftyDescribeRoutersResponse)
    except Exception as e:
        logger.error(f"Failed to get router list: {e}")
        raise


@mcp.tool()
def get_db_list() -> Optional[DescribeDBInstancesResponse]:
    """List of all RDB server in FJcloud-V
    See. https://docs.nifcloud.com/rdb/api/DescribeDBInstances.htm
    """
    try:
        return call_nifcloud_api("rdb", "describe_db_instances", DescribeDBInstancesResponse)
    except Exception as e:
        logger.error(f"Failed to get database list: {e}")
        raise


# DNS Service - Read-Only Operations
@mcp.tool()
def get_hosted_zones_list() -> Optional[ListHostedZonesResponse]:
    """List of all hosted zones in DNS service
    See. https://docs.nifcloud.com/dns/api/
    """
    try:
        return call_nifcloud_api("dns", "list_hosted_zones", ListHostedZonesResponse)
    except Exception as e:
        logger.error(f"Failed to get hosted zones list: {e}")
        raise


@mcp.tool()
def get_resource_record_sets(zone_id: str) -> Optional[ListResourceRecordSetsResponse]:
    """List of all resource record sets in a DNS hosted zone
    
    Args:
        zone_id: The ID of the hosted zone
    
    See. https://docs.nifcloud.com/dns/api/
    """
    try:
        logger.info(f"Calling dns.list_resource_record_sets for zone {zone_id}")
        from .utils import get_nifcloud_client
        
        client = get_nifcloud_client("dns")
        response = client.list_resource_record_sets(HostedZoneId=zone_id)
        
        from .utils import convert_keys_to_snake_case
        
        converted_response = convert_keys_to_snake_case(response)
        result = ListResourceRecordSetsResponse(**converted_response)
        logger.info(f"Successfully processed resource record sets for zone {zone_id}")
        return result
    except Exception as e:
        logger.error(f"Failed to get resource record sets: {e}")
        raise


# NAS Service - Read-Only Operations
@mcp.tool()
def get_nas_instances_list() -> Optional[DescribeNASInstancesResponse]:
    """List of all NAS instances in FJcloud-V
    See. https://docs.nifcloud.com/nas/api/
    """
    try:
        return call_nifcloud_api("nas", "describe_nas_instances", DescribeNASInstancesResponse)
    except Exception as e:
        logger.error(f"Failed to get NAS instances list: {e}")
        raise


@mcp.tool()
def get_nas_security_groups_list() -> Optional[DescribeNASSecurityGroupsResponse]:
    """List of all NAS security groups in FJcloud-V
    See. https://docs.nifcloud.com/nas/api/
    """
    try:
        return call_nifcloud_api(
            "nas", "describe_nas_security_groups", DescribeNASSecurityGroupsResponse
        )
    except Exception as e:
        logger.error(f"Failed to get NAS security groups list: {e}")
        raise


# ESS Service - Read-Only Operations
@mcp.tool()
def get_ess_identities_list() -> Optional[ListIdentitiesResponse]:
    """List of all ESS email identities (addresses and domains)
    See. https://docs.nifcloud.com/ess/api/
    """
    try:
        return call_nifcloud_api("ess", "list_identities", ListIdentitiesResponse)
    except Exception as e:
        logger.error(f"Failed to get ESS identities list: {e}")
        raise


@mcp.tool()
def get_ess_send_quota() -> Optional[GetSendQuotaResponse]:
    """Get the current send quota for ESS (Email Sending Service)
    See. https://docs.nifcloud.com/ess/api/
    """
    try:
        return call_nifcloud_api("ess", "get_send_quota", GetSendQuotaResponse)
    except Exception as e:
        logger.error(f"Failed to get ESS send quota: {e}")
        raise


@mcp.tool()
def get_ess_send_statistics() -> Optional[GetSendStatisticsResponse]:
    """Get send statistics for ESS (Email Sending Service)
    See. https://docs.nifcloud.com/ess/api/
    """
    try:
        return call_nifcloud_api("ess", "get_send_statistics", GetSendStatisticsResponse)
    except Exception as e:
        logger.error(f"Failed to get ESS send statistics: {e}")
        raise


@mcp.tool()
def get_ess_identity_verification_attributes(
    identities: list[str],
) -> Optional[GetIdentityVerificationAttributesResponse]:
    """Get verification attributes for ESS email identities
    
    Args:
        identities: List of email addresses or domains to get verification attributes for
    
    See. https://docs.nifcloud.com/ess/api/
    """
    try:
        logger.info(f"Calling ess.get_identity_verification_attributes for {len(identities)} identities")
        from .utils import get_nifcloud_client, convert_keys_to_snake_case
        
        client = get_nifcloud_client("ess")
        response = client.get_identity_verification_attributes(Identities=identities)
        
        converted_response = convert_keys_to_snake_case(response)
        result = GetIdentityVerificationAttributesResponse(**converted_response)
        logger.info(f"Successfully processed verification attributes")
        return result
    except Exception as e:
        logger.error(f"Failed to get ESS identity verification attributes: {e}")
        raise
