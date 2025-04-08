# server.py
from mcp.server.fastmcp import FastMCP
from nifcloud import session
from settings import Settings
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
from utils import convert_keys_to_snake_case

settings = Settings()


mcp = FastMCP("FJcloud-V MCP", log_level="ERROR")


@mcp.tool()
def get_server_list() -> DescribeInstancesResponse:
    """List of all servers in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeInstances.htm
    """
    client = session.get_session().create_client(
        "computing",
        region_name=settings.NIFCLOUD_DEFAULT_REGION,
        nifcloud_access_key_id=settings.NIFCLOUD_ACCESS_KEY_ID.get_secret_value(),
        nifcloud_secret_access_key=settings.NIFCLOUD_SECRET_ACCESS_KEY.get_secret_value(),
    )
    response = client.describe_instances()
    convert_response = convert_keys_to_snake_case(response)
    return DescribeInstancesResponse(**convert_response)


@mcp.tool()
def get_disk_list() -> DescribeVolumesResponse:
    """List of all disks in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeVolumes.htm
    """
    client = session.get_session().create_client(
        "computing",
        region_name=settings.NIFCLOUD_DEFAULT_REGION,
        nifcloud_access_key_id=settings.NIFCLOUD_ACCESS_KEY_ID.get_secret_value(),
        nifcloud_secret_access_key=settings.NIFCLOUD_SECRET_ACCESS_KEY.get_secret_value(),
    )
    response = client.describe_volumes()
    convert_response = convert_keys_to_snake_case(response)
    return DescribeVolumesResponse(**convert_response)


@mcp.tool()
def get_load_balancer_list() -> DescribeLoadBalancersResponse:
    """List of all load balancers in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeLoadBalancers.htm
    """
    client = session.get_session().create_client(
        "computing",
        region_name=settings.NIFCLOUD_DEFAULT_REGION,
        nifcloud_access_key_id=settings.NIFCLOUD_ACCESS_KEY_ID.get_secret_value(),
        nifcloud_secret_access_key=settings.NIFCLOUD_SECRET_ACCESS_KEY.get_secret_value(),
    )
    response = client.describe_load_balancers()
    convert_response = convert_keys_to_snake_case(response)
    return DescribeLoadBalancersResponse(**convert_response)


@mcp.tool()
def get_firewall_list() -> DescribeSecurityGroupsResponse:
    """List of all firewalls in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeSecurityGroups.htm
    """
    client = session.get_session().create_client(
        "computing",
        region_name=settings.NIFCLOUD_DEFAULT_REGION,
        nifcloud_access_key_id=settings.NIFCLOUD_ACCESS_KEY_ID.get_secret_value(),
        nifcloud_secret_access_key=settings.NIFCLOUD_SECRET_ACCESS_KEY.get_secret_value(),
    )
    response = client.describe_security_groups()
    convert_response = convert_keys_to_snake_case(response)
    return DescribeSecurityGroupsResponse(**convert_response)


@mcp.tool()
def get_router_list() -> NiftyDescribeRoutersResponse:
    """List of all routers in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/NiftyDescribeRouters.htm
    """
    client = session.get_session().create_client(
        "computing",
        region_name=settings.NIFCLOUD_DEFAULT_REGION,
        nifcloud_access_key_id=settings.NIFCLOUD_ACCESS_KEY_ID.get_secret_value(),
        nifcloud_secret_access_key=settings.NIFCLOUD_SECRET_ACCESS_KEY.get_secret_value(),
    )
    response = client.nifty_describe_routers()
    convert_response = convert_keys_to_snake_case(response)
    return NiftyDescribeRoutersResponse(**convert_response)


@mcp.tool()
def get_db_list() -> DescribeDBInstancesResponse:
    """List of all RDB server in FJcloud-V
    See. https://docs.nifcloud.com/rdb/api/DescribeDBInstances.htm
    """
    client = session.get_session().create_client(
        "rdb",
        region_name=settings.NIFCLOUD_DEFAULT_REGION,
        nifcloud_access_key_id=settings.NIFCLOUD_ACCESS_KEY_ID.get_secret_value(),
        nifcloud_secret_access_key=settings.NIFCLOUD_SECRET_ACCESS_KEY.get_secret_value(),
    )
    response = client.describe_db_instances()
    convert_response = convert_keys_to_snake_case(response)
    return DescribeDBInstancesResponse(**convert_response)
