# server.py
from mcp.server.fastmcp import FastMCP

from types_nifcloud.describe_db_instances_response import DescribeDBInstancesResponse
from types_nifcloud.describe_instances_response import DescribeInstancesResponse
from types_nifcloud.describe_load_balancers_response import (
    DescribeLoadBalancersResponse,
)
from types_nifcloud.describe_volumes_response import DescribeVolumesResponse
from types_nifcloud.nifty_describe_routers_response import NiftyDescribeRoutersResponse
from types_nifcloud.describe_security_groups_response import (
    DescribeSecurityGroupsResponse,
)
from utils import call_nifcloud_api

mcp = FastMCP("FJcloud-V MCP", log_level="ERROR")


@mcp.tool()
def get_server_list() -> DescribeInstancesResponse:
    """List of all servers in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeInstances.htm
    """
    return call_nifcloud_api("computing", "describe_instances", DescribeInstancesResponse)


@mcp.tool()
def get_disk_list() -> DescribeVolumesResponse:
    """List of all disks in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeVolumes.htm
    """
    return call_nifcloud_api("computing", "describe_volumes", DescribeVolumesResponse)


@mcp.tool()
def get_load_balancer_list() -> DescribeLoadBalancersResponse:
    """List of all load balancers in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeLoadBalancers.htm
    """
    return call_nifcloud_api("computing", "describe_load_balancers", DescribeLoadBalancersResponse)


@mcp.tool()
def get_firewall_list() -> DescribeSecurityGroupsResponse:
    """List of all firewalls in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeSecurityGroups.htm
    """
    return call_nifcloud_api("computing", "describe_security_groups", DescribeSecurityGroupsResponse)


@mcp.tool()
def get_router_list() -> NiftyDescribeRoutersResponse:
    """List of all routers in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/NiftyDescribeRouters.htm
    """
    return call_nifcloud_api("computing", "nifty_describe_routers", NiftyDescribeRoutersResponse)


@mcp.tool()
def get_db_list() -> DescribeDBInstancesResponse:
    """List of all RDB server in FJcloud-V
    See. https://docs.nifcloud.com/rdb/api/DescribeDBInstances.htm
    """
    return call_nifcloud_api("rdb", "describe_db_instances", DescribeDBInstancesResponse)
