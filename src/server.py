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
