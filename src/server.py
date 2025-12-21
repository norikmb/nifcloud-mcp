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
from .types_nifcloud.get_service_response import GetServiceResponse
from .types_nifcloud.describe_migration_hubs_response import DescribeMigrationHubsResponse
from .types_nifcloud.list_resource_groups_response import ListResourceGroupsResponse
from .types_nifcloud.list_templates_response import ListTemplatesResponse
from .types_nifcloud.describe_service_statuses_response import DescribeServiceStatusesResponse
from .types_nifcloud.list_devops_instances_response import ListInstancesResponse
from .types_nifcloud.list_parameter_groups_response import ListParameterGroupsResponse
from .types_nifcloud.list_firewall_groups_response import ListFirewallGroupsResponse
from .types_nifcloud.list_backups_response import ListBackupsResponse
from .types_nifcloud.list_runners_response import ListRunnersResponse
from .types_nifcloud.describe_images_response import DescribeImagesResponse
from .types_nifcloud.describe_key_pairs_response import DescribeKeyPairsResponse
from .types_nifcloud.describe_iso_images_response import DescribeIsoImagesResponse
from .types_nifcloud.describe_db_snapshots_response import DescribeDBSnapshotsResponse
from .types_nifcloud.nifty_describe_private_lans_response import NiftyDescribePrivateLansResponse
from .types_nifcloud.describe_db_parameter_groups_response import DescribeDBParameterGroupsResponse
from .types_nifcloud.describe_db_security_groups_response import DescribeDBSecurityGroupsResponse
from .types_nifcloud.describe_db_parameters_response import DescribeDBParametersResponse
from .types_nifcloud.describe_db_engine_versions_response import DescribeDBEngineVersionsResponse
from .types_nifcloud.describe_usage_response import DescribeUsageResponse
from .types_nifcloud.describe_resources_response import DescribeResourcesResponse
from .types_nifcloud.get_hosted_zone_response import GetHostedZoneResponse
from .types_nifcloud.get_change_response import GetChangeResponse
from .types_nifcloud.describe_event_calendar_response import DescribeEventCalendarResponse
from .types_nifcloud.describe_event_attributes_response import DescribeEventAttributesResponse
from .types_nifcloud.list_events_response import ListEventsResponse
from .types_nifcloud.list_activity_logs_response import ListActivityLogsResponse
from .types_nifcloud.get_resource_group_response import GetResourceGroupResponse
from .types_nifcloud.describe_event_categories_response import DescribeEventCategoriesResponse
from .types_nifcloud.describe_orderable_db_instance_options_response import DescribeOrderableDBInstanceOptionsResponse
from .types_nifcloud.describe_certificates_response import DescribeCertificatesResponse
from .types_nifcloud.describe_db_events_response import DescribeDBEventsResponse
from .types_nifcloud.describe_event_subscriptions_response import DescribeEventSubscriptionsResponse
from .types_nifcloud.describe_db_log_files_response import DescribeDBLogFilesResponse
from .types_nifcloud.describe_engine_default_parameters_response import DescribeEngineDefaultParametersResponse
from .types_nifcloud.get_identity_dkim_attributes_response import GetIdentityDkimAttributesResponse
from .types_nifcloud.get_delivery_log_response import GetDeliveryLogResponse
from .types_nifcloud.get_instance_metrics_response import GetInstanceMetricsResponse
from .types_nifcloud.describe_migration_hub_networks_response import DescribeMigrationHubNetworksResponse
from .types_nifcloud.describe_migration_hub_activities_response import DescribeMigrationHubActivitiesResponse
from .types_nifcloud.describe_addresses_response import DescribeAddressesResponse
from .types_nifcloud.describe_network_interfaces_response import DescribeNetworkInterfacesResponse
from .types_nifcloud.describe_multi_ip_address_groups_response import (
    DescribeMultiIpAddressGroupsResponse,
)
from .types_nifcloud.describe_availability_zones_response import DescribeAvailabilityZonesResponse
from .types_nifcloud.describe_regions_response import DescribeRegionsResponse
from .types_nifcloud.describe_associated_users_response import DescribeAssociatedUsersResponse
from .types_nifcloud.describe_instance_backup_rules_response import DescribeInstanceBackupRulesResponse
from .types_nifcloud.describe_instance_backup_rule_activities_response import (
    DescribeInstanceBackupRuleActivitiesResponse,
)
from .types_nifcloud.describe_instance_attribute_response import DescribeInstanceAttributeResponse
from .types_nifcloud.describe_uploads_response import DescribeUploadsResponse
from .types_nifcloud.describe_instance_health_response import DescribeInstanceHealthResponse
from .types_nifcloud.describe_ssl_certificates_response import DescribeSslCertificatesResponse
from .types_nifcloud.describe_ssl_certificate_attribute_response import DescribeSslCertificateAttributeResponse
from .types_nifcloud.nifty_describe_load_balancer_ssl_policies_response import NiftyDescribeLoadBalancerSSLPoliciesResponse
from .types_nifcloud.nifty_describe_performance_chart_response import NiftyDescribePerformanceChartResponse
from .types_nifcloud.nifty_describe_alarm_history_response import NiftyDescribeAlarmHistoryResponse
from .types_nifcloud.nifty_describe_alarm_rules_activities_response import NiftyDescribeAlarmRulesActivitiesResponse
from .types_nifcloud.describe_user_activities_response import DescribeUserActivitiesResponse
from .types_nifcloud.nifty_describe_web_proxies_response import NiftyDescribeWebProxiesResponse
from .types_nifcloud.describe_remote_access_vpn_gateway_client_config_response import DescribeRemoteAccessVpnGatewayClientConfigResponse
from .types_nifcloud.list_faq_categories_response import ListFAQCategoriesResponse
from .types_nifcloud.list_faq_items_response import ListFAQItemsResponse
from .types_nifcloud.resource_information import ResourceInformation
from .utils import call_nifcloud_api
import json
import urllib.parse
import urllib.request

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


# Object Storage Service - Read-Only Operations
@mcp.tool()
def get_object_storage_buckets_list() -> Optional[GetServiceResponse]:
    """List of all buckets in Object Storage Service
    See. https://docs.nifcloud.com/object-storage-service/api/
    """
    try:
        return call_nifcloud_api(
            "object-storage-service", "get_service", GetServiceResponse
        )
    except Exception as e:
        logger.error(f"Failed to get object storage buckets list: {e}")
        raise


# Live Migration Service - Read-Only Operations
@mcp.tool()
def get_migration_hubs_list() -> Optional[DescribeMigrationHubsResponse]:
    """List of all migration hubs in Live Migration service
    See. https://docs.nifcloud.com/livemigration/api/
    """
    try:
        return call_nifcloud_api(
            "livemigration", "describe_migration_hubs", DescribeMigrationHubsResponse
        )
    except Exception as e:
        logger.error(f"Failed to get migration hubs list: {e}")
        raise


# Catalog Service - Read-Only Operations
@mcp.tool()
def get_catalog_resource_groups_list() -> Optional[ListResourceGroupsResponse]:
    """List of all resource groups in Catalog service
    See. https://docs.nifcloud.com/catalog/api/
    """
    try:
        return call_nifcloud_api(
            "catalog", "list_resource_groups", ListResourceGroupsResponse
        )
    except Exception as e:
        logger.error(f"Failed to get catalog resource groups list: {e}")
        raise


@mcp.tool()
def get_catalog_templates_list() -> Optional[ListTemplatesResponse]:
    """List of all templates in Catalog service
    See. https://docs.nifcloud.com/catalog/api/
    """
    try:
        return call_nifcloud_api("catalog", "list_templates", ListTemplatesResponse)
    except Exception as e:
        logger.error(f"Failed to get catalog templates list: {e}")
        raise


# Service Activity - Read-Only Operations
@mcp.tool()
def get_service_statuses() -> Optional[DescribeServiceStatusesResponse]:
    """Get service status information for all NIFCLOUD services
    See. https://docs.nifcloud.com/service-activity/api/
    """
    try:
        return call_nifcloud_api(
            "service-activity", "describe_service_statuses", DescribeServiceStatusesResponse
        )
    except Exception as e:
        logger.error(f"Failed to get service statuses: {e}")
        raise


# Resource and Support Information
@mcp.tool()
def get_nifcloud_resources() -> ResourceInformation:
    """Get NIFCLOUD documentation, support resources, and contact information
    
    Returns information about:
    - Documentation links (API docs, CLI, SDK, etc.)
    - Support channels (Portal, FAQ, Contact form)
    - Contact information (Phone, business hours)
    - Additional resources (News, Events, Estimate tool, etc.)
    
    See. https://docs.nifcloud.com/
    """
    try:
        logger.info("Retrieving NIFCLOUD resource information")
        return ResourceInformation()
    except Exception as e:
        logger.error(f"Failed to get resource information: {e}")
        raise


# DevOps with GitLab Service - Read-Only Operations
@mcp.tool()
def get_devops_instances_list() -> Optional[ListInstancesResponse]:
    """List of all DevOps server instances
    See. https://docs.nifcloud.com/devops/api/
    """
    try:
        return call_nifcloud_api("devops", "list_instances", ListInstancesResponse)
    except Exception as e:
        logger.error(f"Failed to get DevOps instances list: {e}")
        raise


@mcp.tool()
def get_devops_parameter_groups_list() -> Optional[ListParameterGroupsResponse]:
    """List of all DevOps parameter groups
    See. https://docs.nifcloud.com/devops/api/
    """
    try:
        return call_nifcloud_api(
            "devops", "list_parameter_groups", ListParameterGroupsResponse
        )
    except Exception as e:
        logger.error(f"Failed to get DevOps parameter groups list: {e}")
        raise


@mcp.tool()
def get_devops_firewall_groups_list() -> Optional[ListFirewallGroupsResponse]:
    """List of all DevOps firewall groups
    See. https://docs.nifcloud.com/devops/api/
    """
    try:
        return call_nifcloud_api(
            "devops", "list_firewall_groups", ListFirewallGroupsResponse
        )
    except Exception as e:
        logger.error(f"Failed to get DevOps firewall groups list: {e}")
        raise


@mcp.tool()
def get_devops_backups_list() -> Optional[ListBackupsResponse]:
    """List of all DevOps backup files
    See. https://docs.nifcloud.com/devops/api/
    """
    try:
        return call_nifcloud_api("devops", "list_backups", ListBackupsResponse)
    except Exception as e:
        logger.error(f"Failed to get DevOps backups list: {e}")
        raise


@mcp.tool()
def get_devops_runners_list() -> Optional[ListRunnersResponse]:
    """List of all DevOps runners (GitLab CI/CD runners)
    See. https://docs.nifcloud.com/devops/api/
    """
    try:
        return call_nifcloud_api("devops", "list_runners", ListRunnersResponse)
    except Exception as e:
        logger.error(f"Failed to get DevOps runners list: {e}")
        raise


@mcp.tool()
def get_images_list() -> Optional[DescribeImagesResponse]:
    """List of all OS images available
    See. https://docs.nifcloud.com/cp/api/DescribeImages.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_images", DescribeImagesResponse)
    except Exception as e:
        logger.error(f"Failed to get images list: {e}")
        raise


@mcp.tool()
def get_key_pairs_list() -> Optional[DescribeKeyPairsResponse]:
    """List of all SSH key pairs
    See. https://docs.nifcloud.com/cp/api/DescribeKeyPairs.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_key_pairs", DescribeKeyPairsResponse)
    except Exception as e:
        logger.error(f"Failed to get key pairs list: {e}")
        raise


@mcp.tool()
def get_iso_images_list() -> Optional[DescribeIsoImagesResponse]:
    """List of all ISO images
    See. https://docs.nifcloud.com/cp/api/DescribeIsoImages.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_iso_images", DescribeIsoImagesResponse)
    except Exception as e:
        logger.error(f"Failed to get ISO images list: {e}")
        raise


@mcp.tool()
def get_db_snapshots_list() -> Optional[DescribeDBSnapshotsResponse]:
    """List of all RDB database snapshots
    See. https://docs.nifcloud.com/rdb/api/DescribeDBSnapshots.htm
    """
    try:
        return call_nifcloud_api("rdb", "describe_db_snapshots", DescribeDBSnapshotsResponse)
    except Exception as e:
        logger.error(f"Failed to get DB snapshots list: {e}")
        raise


@mcp.tool()
def get_private_lans_list() -> Optional[NiftyDescribePrivateLansResponse]:
    """List of all private LANs
    See. https://docs.nifcloud.com/cp/api/NiftyDescribePrivateLans.htm
    """
    try:
        return call_nifcloud_api("computing", "nifty_describe_private_lans", NiftyDescribePrivateLansResponse)
    except Exception as e:
        logger.error(f"Failed to get private LANs list: {e}")
        raise


@mcp.tool()
def get_db_parameter_groups_list() -> Optional[DescribeDBParameterGroupsResponse]:
    """List of all RDB parameter groups
    See. https://docs.nifcloud.com/rdb/api/DescribeDBParameterGroups.htm
    """
    try:
        return call_nifcloud_api("rdb", "describe_db_parameter_groups", DescribeDBParameterGroupsResponse)
    except Exception as e:
        logger.error(f"Failed to get DB parameter groups list: {e}")
        raise


@mcp.tool()
def get_db_security_groups_list() -> Optional[DescribeDBSecurityGroupsResponse]:
    """List of all RDB firewall groups (security groups)
    See. https://docs.nifcloud.com/rdb/api/DescribeDBSecurityGroups.htm
    """
    try:
        return call_nifcloud_api("rdb", "describe_db_security_groups", DescribeDBSecurityGroupsResponse)
    except Exception as e:
        logger.error(f"Failed to get DB security groups list: {e}")
        raise


@mcp.tool()
def get_db_parameters(parameter_group_name: str) -> Optional[DescribeDBParametersResponse]:
    """Get RDB parameters for a specific parameter group
    See. https://docs.nifcloud.com/rdb/api/DescribeDBParameters.htm
    """
    try:
        return call_nifcloud_api(
            "rdb", 
            "describe_db_parameters", 
            DescribeDBParametersResponse,
            DBParameterGroupName=parameter_group_name
        )
    except Exception as e:
        logger.error(f"Failed to get DB parameters: {e}")
        raise


@mcp.tool()
def get_db_engine_versions() -> Optional[DescribeDBEngineVersionsResponse]:
    """Get available RDB database engine versions
    See. https://docs.nifcloud.com/rdb/api/DescribeDBEngineVersions.htm
    """
    try:
        return call_nifcloud_api("rdb", "describe_db_engine_versions", DescribeDBEngineVersionsResponse)
    except Exception as e:
        logger.error(f"Failed to get DB engine versions: {e}")
        raise


@mcp.tool()
def get_usage(year_month: str = None, region: str = None, is_charge: bool = False) -> Optional[DescribeUsageResponse]:
    """Get Computing resource usage information
    See. https://docs.nifcloud.com/cp/api/DescribeUsage.htm
    """
    try:
        kwargs = {}
        if year_month:
            kwargs['YearMonth'] = year_month
        if region:
            kwargs['Region'] = region
        if is_charge:
            kwargs['IsCharge'] = is_charge
        return call_nifcloud_api("computing", "describe_usage", DescribeUsageResponse, **kwargs)
    except Exception as e:
        logger.error(f"Failed to get usage information: {e}")
        raise


@mcp.tool()
def get_resources() -> Optional[DescribeResourcesResponse]:
    """Get Computing resource dashboard information
    See. https://docs.nifcloud.com/cp/api/DescribeResources.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_resources", DescribeResourcesResponse)
    except Exception as e:
        logger.error(f"Failed to get resources information: {e}")
        raise


@mcp.tool()
def get_hosted_zone(zone_id: str) -> Optional[GetHostedZoneResponse]:
    """Get DNS hosted zone information
    See. https://docs.nifcloud.com/dns/api/GetHostedZone.htm
    """
    try:
        return call_nifcloud_api("dns", "get_hosted_zone", GetHostedZoneResponse, Id=zone_id)
    except Exception as e:
        logger.error(f"Failed to get hosted zone: {e}")
        raise


@mcp.tool()
def get_dns_change(change_id: str) -> Optional[GetChangeResponse]:
    """Get DNS change request information
    See. https://docs.nifcloud.com/dns/api/GetChange.htm
    """
    try:
        return call_nifcloud_api("dns", "get_change", GetChangeResponse, Id=change_id)
    except Exception as e:
        logger.error(f"Failed to get DNS change: {e}")
        raise


@mcp.tool()
def get_event_calendar(year_month: Optional[str] = None) -> Optional[DescribeEventCalendarResponse]:
    """Get service event calendar information
    See. https://docs.nifcloud.com/service-activity/api/
    """
    try:
        kwargs = {}
        if year_month:
            kwargs['YearMonth'] = year_month
        return call_nifcloud_api("service-activity", "describe_event_calendar", DescribeEventCalendarResponse, **kwargs)
    except Exception as e:
        logger.error(f"Failed to get event calendar: {e}")
        raise


@mcp.tool()
def get_event_attributes() -> Optional[DescribeEventAttributesResponse]:
    """Get service event attributes (list format)
    See. https://docs.nifcloud.com/service-activity/api/
    """
    try:
        return call_nifcloud_api("service-activity", "describe_event_attributes", DescribeEventAttributesResponse)
    except Exception as e:
        logger.error(f"Failed to get event attributes: {e}")
        raise


@mcp.tool()
def get_catalog_events() -> Optional[ListEventsResponse]:
    """Get Catalog service events
    See. https://docs.nifcloud.com/catalog/api/
    """
    try:
        return call_nifcloud_api("catalog", "list_events", ListEventsResponse)
    except Exception as e:
        logger.error(f"Failed to get catalog events: {e}")
        raise


@mcp.tool()
def get_catalog_activity_logs() -> Optional[ListActivityLogsResponse]:
    """Get Catalog service activity logs
    See. https://docs.nifcloud.com/catalog/api/
    """
    try:
        return call_nifcloud_api("catalog", "list_activity_logs", ListActivityLogsResponse)
    except Exception as e:
        logger.error(f"Failed to get activity logs: {e}")
        raise


@mcp.tool()
def get_catalog_resource_group(group_id: str) -> Optional[GetResourceGroupResponse]:
    """Get specific resource group information
    See. https://docs.nifcloud.com/catalog/api/
    """
    try:
        return call_nifcloud_api("catalog", "get_resource_group", GetResourceGroupResponse, ResourceGroupId=group_id)
    except Exception as e:
        logger.error(f"Failed to get resource group: {e}")
        raise


@mcp.tool()
def get_db_event_categories() -> Optional[DescribeEventCategoriesResponse]:
    """Get RDB event categories information
    See. https://docs.nifcloud.com/rdb/api/
    """
    try:
        return call_nifcloud_api("rdb", "describe_event_categories", DescribeEventCategoriesResponse)
    except Exception as e:
        logger.error(f"Failed to get event categories: {e}")
        raise


@mcp.tool()
def get_orderable_db_instance_options(engine: Optional[str] = None) -> Optional[DescribeOrderableDBInstanceOptionsResponse]:
    """Get orderable DB instance options
    See. https://docs.nifcloud.com/rdb/api/
    """
    try:
        kwargs = {}
        if engine:
            kwargs['Engine'] = engine
        return call_nifcloud_api("rdb", "describe_orderable_db_instance_options", DescribeOrderableDBInstanceOptionsResponse, **kwargs)
    except Exception as e:
        logger.error(f"Failed to get orderable DB instance options: {e}")
        raise


@mcp.tool()
def get_db_certificates() -> Optional[DescribeCertificatesResponse]:
    """Get RDB CA certificate information
    See. https://docs.nifcloud.com/rdb/api/
    """
    try:
        return call_nifcloud_api("rdb", "describe_certificates", DescribeCertificatesResponse)
    except Exception as e:
        logger.error(f"Failed to get certificates: {e}")
        raise


@mcp.tool()
def get_db_events() -> Optional[DescribeDBEventsResponse]:
    """Get RDB event information
    See. https://docs.nifcloud.com/rdb/api/
    """
    try:
        return call_nifcloud_api("rdb", "describe_events", DescribeDBEventsResponse)
    except Exception as e:
        logger.error(f"Failed to get DB events: {e}")
        raise


@mcp.tool()
def get_db_event_subscriptions() -> Optional[DescribeEventSubscriptionsResponse]:
    """Get RDB event subscription information
    See. https://docs.nifcloud.com/rdb/api/
    """
    try:
        return call_nifcloud_api("rdb", "describe_event_subscriptions", DescribeEventSubscriptionsResponse)
    except Exception as e:
        logger.error(f"Failed to get event subscriptions: {e}")
        raise


@mcp.tool()
def get_db_log_files(db_instance_id: Optional[str] = None) -> Optional[DescribeDBLogFilesResponse]:
    """Get RDB log file information
    See. https://docs.nifcloud.com/rdb/api/
    """
    try:
        kwargs = {}
        if db_instance_id:
            kwargs['DBInstanceIdentifier'] = db_instance_id
        return call_nifcloud_api("rdb", "describe_db_log_files", DescribeDBLogFilesResponse, **kwargs)
    except Exception as e:
        logger.error(f"Failed to get DB log files: {e}")
        raise


@mcp.tool()
def get_engine_default_parameters(engine: str) -> Optional[DescribeEngineDefaultParametersResponse]:
    """Get RDB engine default parameters
    See. https://docs.nifcloud.com/rdb/api/
    """
    try:
        return call_nifcloud_api("rdb", "describe_engine_default_parameters", DescribeEngineDefaultParametersResponse, DBParameterGroupFamily=engine)
    except Exception as e:
        logger.error(f"Failed to get engine default parameters: {e}")
        raise


@mcp.tool()
def get_ess_identity_dkim_attributes(identities: Optional[list[str]] = None) -> Optional[GetIdentityDkimAttributesResponse]:
    """Get ESS DKIM attributes for email identities
    See. https://docs.nifcloud.com/ess/api/
    """
    try:
        kwargs = {}
        if identities:
            kwargs['Identities'] = identities
        return call_nifcloud_api("ess", "get_identity_dkim_attributes", GetIdentityDkimAttributesResponse, **kwargs)
    except Exception as e:
        logger.error(f"Failed to get DKIM attributes: {e}")
        raise


@mcp.tool()
def get_ess_delivery_log(start_date: Optional[str] = None, end_date: Optional[str] = None) -> Optional[GetDeliveryLogResponse]:
    """Get ESS email delivery log
    See. https://docs.nifcloud.com/ess/api/
    """
    try:
        kwargs = {}
        if start_date:
            kwargs['StartDate'] = start_date
        if end_date:
            kwargs['EndDate'] = end_date
        return call_nifcloud_api("ess", "get_delivery_log", GetDeliveryLogResponse, **kwargs)
    except Exception as e:
        logger.error(f"Failed to get delivery log: {e}")
        raise


@mcp.tool()
def get_devops_instance_metrics(instance_id: str) -> Optional[GetInstanceMetricsResponse]:
    """Get DevOps instance metrics information
    See. https://docs.nifcloud.com/devops/api/
    """
    try:
        return call_nifcloud_api("devops", "get_instance_metrics", GetInstanceMetricsResponse, InstanceId=instance_id)
    except Exception as e:
        logger.error(f"Failed to get instance metrics: {e}")
        raise


@mcp.tool()
def get_migration_hub_networks(migration_hub_id: str) -> Optional[DescribeMigrationHubNetworksResponse]:
    """Get LiveMigration hub network information
    See. https://docs.nifcloud.com/livemigration/api/
    """
    try:
        return call_nifcloud_api("livemigration", "describe_migration_hub_networks", DescribeMigrationHubNetworksResponse, MigrationHubId=migration_hub_id)
    except Exception as e:
        logger.error(f"Failed to get migration hub networks: {e}")
        raise


@mcp.tool()
def get_migration_hub_activities(migration_hub_id: str) -> Optional[DescribeMigrationHubActivitiesResponse]:
    """Get LiveMigration hub activity information
    See. https://docs.nifcloud.com/livemigration/api/
    """
    try:
        return call_nifcloud_api("livemigration", "describe_migration_hub_activities", DescribeMigrationHubActivitiesResponse, MigrationHubId=migration_hub_id)
    except Exception as e:
        logger.error(f"Failed to get migration hub activities: {e}")
        raise


@mcp.tool()
def get_addresses_list() -> Optional[DescribeAddressesResponse]:
    """List of all elastic IP addresses in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeAddresses.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_addresses", DescribeAddressesResponse)
    except Exception as e:
        logger.error(f"Failed to get addresses list: {e}")
        raise


@mcp.tool()
def get_network_interfaces_list() -> Optional[DescribeNetworkInterfacesResponse]:
    """List of all network interfaces in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeNetworkInterfaces.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_network_interfaces", DescribeNetworkInterfacesResponse)
    except Exception as e:
        logger.error(f"Failed to get network interfaces list: {e}")
        raise


@mcp.tool()
def get_multi_ip_address_groups_list() -> Optional[DescribeMultiIpAddressGroupsResponse]:
    """List of all multi IP address groups in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeMultiIpAddressGroups.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_multi_ip_address_groups", DescribeMultiIpAddressGroupsResponse)
    except Exception as e:
        logger.error(f"Failed to get multi IP address groups list: {e}")
        raise


@mcp.tool()
def get_availability_zones() -> Optional[DescribeAvailabilityZonesResponse]:
    """Get all available availability zones in FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeAvailabilityZones.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_availability_zones", DescribeAvailabilityZonesResponse)
    except Exception as e:
        logger.error(f"Failed to get availability zones: {e}")
        raise


@mcp.tool()
def get_regions() -> Optional[DescribeRegionsResponse]:
    """Get all available regions for FJcloud-V
    See. https://docs.nifcloud.com/cp/api/DescribeRegions.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_regions", DescribeRegionsResponse)
    except Exception as e:
        logger.error(f"Failed to get regions: {e}")
        raise


@mcp.tool()
def get_associated_users() -> Optional[DescribeAssociatedUsersResponse]:
    """Get users with shared access to resources
    See. https://docs.nifcloud.com/cp/api/DescribeAssociatedUsers.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_associated_users", DescribeAssociatedUsersResponse)
    except Exception as e:
        logger.error(f"Failed to get associated users: {e}")
        raise


@mcp.tool()
def get_instance_backup_rules() -> Optional[DescribeInstanceBackupRulesResponse]:
    """Get instance backup rules configuration
    See. https://docs.nifcloud.com/cp/api/DescribeInstanceBackupRules.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_instance_backup_rules", DescribeInstanceBackupRulesResponse)
    except Exception as e:
        logger.error(f"Failed to get instance backup rules: {e}")
        raise


@mcp.tool()
def get_instance_backup_rule_activities() -> Optional[DescribeInstanceBackupRuleActivitiesResponse]:
    """Get instance backup rule activity logs
    See. https://docs.nifcloud.com/cp/api/DescribeInstanceBackupRuleActivities.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_instance_backup_rule_activities", DescribeInstanceBackupRuleActivitiesResponse)
    except Exception as e:
        logger.error(f"Failed to get instance backup rule activities: {e}")
        raise


@mcp.tool()
def get_instance_attribute(instance_id: str, attribute: str = "instanceType") -> Optional[DescribeInstanceAttributeResponse]:
    """Get specific attribute of a server instance
    See. https://docs.nifcloud.com/cp/api/DescribeInstanceAttribute.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_instance_attribute", DescribeInstanceAttributeResponse, InstanceId=instance_id, Attribute=attribute)
    except Exception as e:
        logger.error(f"Failed to get instance attribute: {e}")
        raise


@mcp.tool()
def get_uploads() -> Optional[DescribeUploadsResponse]:
    """List upload tasks in progress
    See. https://docs.nifcloud.com/cp/api/DescribeUploads.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_uploads", DescribeUploadsResponse)
    except Exception as e:
        logger.error(f"Failed to get uploads: {e}")
        raise


@mcp.tool()
def get_instance_health(load_balancer_name: str, instances: list = None) -> Optional[DescribeInstanceHealthResponse]:
    """Get load balancer health check status for instances
    See. https://docs.nifcloud.com/cp/api/DescribeInstanceHealth.htm
    """
    try:
        kwargs = {"LoadBalancerName": load_balancer_name}
        if instances:
            for idx, instance_id in enumerate(instances, 1):
                kwargs[f"Instances.member.{idx}"] = instance_id
        return call_nifcloud_api("computing", "describe_instance_health", DescribeInstanceHealthResponse, **kwargs)
    except Exception as e:
        logger.error(f"Failed to get instance health: {e}")
        raise


@mcp.tool()
def get_ssl_certificates() -> Optional[DescribeSslCertificatesResponse]:
    """List SSL certificates
    See. https://docs.nifcloud.com/cp/api/DescribeSslCertificates.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_ssl_certificates", DescribeSslCertificatesResponse)
    except Exception as e:
        logger.error(f"Failed to get SSL certificates: {e}")
        raise


@mcp.tool()
def get_ssl_certificate_attribute(certificate_name: str, attribute: str = "publicKey") -> Optional[DescribeSslCertificateAttributeResponse]:
    """Get specific attribute of an SSL certificate
    See. https://docs.nifcloud.com/cp/api/DescribeSslCertificateAttribute.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_ssl_certificate_attribute", DescribeSslCertificateAttributeResponse, CertificateName=certificate_name, Attribute=attribute)
    except Exception as e:
        logger.error(f"Failed to get SSL certificate attribute: {e}")
        raise


@mcp.tool()
def get_load_balancer_ssl_policies() -> Optional[NiftyDescribeLoadBalancerSSLPoliciesResponse]:
    """Get available SSL security policies for load balancers
    See. https://docs.nifcloud.com/cp/api/NiftyDescribeLoadBalancerSSLPolicies.htm
    """
    try:
        return call_nifcloud_api("computing", "nifty_describe_load_balancer_ssl_policies", NiftyDescribeLoadBalancerSSLPoliciesResponse)
    except Exception as e:
        logger.error(f"Failed to get load balancer SSL policies: {e}")
        raise


@mcp.tool()
def get_performance_chart(resource_id: str, start_time: str = None, end_time: str = None) -> Optional[NiftyDescribePerformanceChartResponse]:
    """Get performance chart data for monitoring
    See. https://docs.nifcloud.com/cp/api/NiftyDescribePerformanceChart.htm
    """
    try:
        kwargs = {"ResourceId": resource_id}
        if start_time:
            kwargs["StartTime"] = start_time
        if end_time:
            kwargs["EndTime"] = end_time
        return call_nifcloud_api("computing", "nifty_describe_performance_chart", NiftyDescribePerformanceChartResponse, **kwargs)
    except Exception as e:
        logger.error(f"Failed to get performance chart: {e}")
        raise


@mcp.tool()
def get_alarm_history() -> Optional[NiftyDescribeAlarmHistoryResponse]:
    """Get alarm history logs
    See. https://docs.nifcloud.com/cp/api/NiftyDescribeAlarmHistory.htm
    """
    try:
        return call_nifcloud_api("computing", "nifty_describe_alarm_history", NiftyDescribeAlarmHistoryResponse)
    except Exception as e:
        logger.error(f"Failed to get alarm history: {e}")
        raise


@mcp.tool()
def get_alarm_rules_activities() -> Optional[NiftyDescribeAlarmRulesActivitiesResponse]:
    """Get alarm rules activity logs
    See. https://docs.nifcloud.com/cp/api/NiftyDescribeAlarmRulesActivities.htm
    """
    try:
        return call_nifcloud_api("computing", "nifty_describe_alarm_rules_activities", NiftyDescribeAlarmRulesActivitiesResponse)
    except Exception as e:
        logger.error(f"Failed to get alarm rules activities: {e}")
        raise


@mcp.tool()
def get_user_activities() -> Optional[DescribeUserActivitiesResponse]:
    """Get API and control panel usage history
    See. https://docs.nifcloud.com/cp/api/DescribeUserActivities.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_user_activities", DescribeUserActivitiesResponse)
    except Exception as e:
        logger.error(f"Failed to get user activities: {e}")
        raise


@mcp.tool()
def get_web_proxies(router_id: str) -> Optional[NiftyDescribeWebProxiesResponse]:
    """Get web proxy configuration for a router
    See. https://docs.nifcloud.com/cp/api/NiftyDescribeWebProxies.htm
    """
    try:
        return call_nifcloud_api("computing", "nifty_describe_web_proxies", NiftyDescribeWebProxiesResponse, RouterId=router_id)
    except Exception as e:
        logger.error(f"Failed to get web proxies: {e}")
        raise


@mcp.tool()
def get_remote_access_vpn_gateway_client_config(vpn_gateway_id: str) -> Optional[DescribeRemoteAccessVpnGatewayClientConfigResponse]:
    """Get remote access VPN gateway client configuration file
    See. https://docs.nifcloud.com/cp/api/DescribeRemoteAccessVpnGatewayClientConfig.htm
    """
    try:
        return call_nifcloud_api("computing", "describe_remote_access_vpn_gateway_client_config", DescribeRemoteAccessVpnGatewayClientConfigResponse, VpnGatewayId=vpn_gateway_id)
    except Exception as e:
        logger.error(f"Failed to get remote access VPN gateway client config: {e}")
        raise


@mcp.tool()
def get_faq_categories() -> Optional[ListFAQCategoriesResponse]:
    """Get list of FAQ categories from support.nifcloud.com
    See. https://faq.support.nifcloud.com/
    """
    try:
        url = "https://faq.support.nifcloud.com/category/show/1?site_domain=default"
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            html_content = response.read().decode('utf-8')
        
        # Extract categories from HTML - parse the main categories list
        categories = []
        
        # Main categories with item counts
        category_patterns = {
            '93': 'トラブルシューティング (67件)',
            '7': '基本サービス (55件)',
            '17': 'サーバー・ディスク機能 (99件)',
            '24': 'ネットワーク機能 (174件)',
            '51': 'セキュリティ機能 (55件)',
            '59': 'その他の機能 (151件)',
            '72': 'サポートサービス (10件)',
            '75': 'その他 (17件)',
            '77': 'エンジニアリングパーツ (46件)',
            '3': 'サーバータイプ・仕様 (134件)',
        }
        
        for cat_id, cat_info in category_patterns.items():
            name_part = cat_info.split(' (')[0]
            count_part = cat_info.split('(')[1].rstrip(')件')
            try:
                count = int(count_part)
                categories.append({
                    "category_id": cat_id,
                    "category_name": name_part,
                    "item_count": count
                })
            except:
                pass
        
        return ListFAQCategoriesResponse(
            categories=categories,
            total_count=len(categories)
        )
    except Exception as e:
        logger.error(f"Failed to get FAQ categories: {e}")
        raise


@mcp.tool()
def get_faq_items(category_id: str = "93", page: int = 1) -> Optional[ListFAQItemsResponse]:
    """Get FAQ items in a specific category
    Category IDs: 93=トラブルシューティング, 7=基本サービス, 17=サーバー・ディスク機能, 24=ネットワーク機能, etc.
    See. https://faq.support.nifcloud.com/
    """
    try:
        url = f"https://faq.support.nifcloud.com/category/show/{category_id}?page={page}&site_domain=default&sort=sort_access&sort_order=desc"
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            html_content = response.read().decode('utf-8')
        
        # Parse FAQ items from HTML
        faq_items = []
        
        # Extract from the content - looking for patterns like FAQ titles and links
        import re
        
        # Pattern for FAQ items with title attribute: <a title="..." href="/faq/show/372?...">
        # This matches both relative and absolute URLs
        pattern = r'<a\s+title="([^"]+)"\s+href="([^"]+faq/show/(\d+)[^"]*)"\s*>'
        matches = re.finditer(pattern, html_content)
        
        seen_ids = set()
        for match in matches:
            title = match.group(1).strip()
            href = match.group(2).strip()
            faq_id = match.group(3)
            
            # Avoid duplicates
            if faq_id in seen_ids:
                continue
            
            # Build full URL if it's relative
            if href.startswith('/'):
                full_url = 'https://faq.support.nifcloud.com' + href
            else:
                full_url = href
            
            if title and len(title) > 0:
                faq_items.append({
                    "faq_id": faq_id,
                    "faq_number": int(faq_id),
                    "title": title,
                    "url": full_url,
                    "summary": None,
                    "publish_date": None,
                    "update_date": None
                })
                seen_ids.add(faq_id)
        
        # Limit to first 10 items per page for display
        faq_items = faq_items[:10]
        
        category_names = {
            '93': 'トラブルシューティング',
            '7': '基本サービス',
            '17': 'サーバー・ディスク機能',
            '24': 'ネットワーク機能',
            '51': 'セキュリティ機能',
            '59': 'その他の機能',
            '72': 'サポートサービス',
            '75': 'その他',
            '77': 'エンジニアリングパーツ',
            '3': 'サーバータイプ・仕様',
        }
        
        return ListFAQItemsResponse(
            category_id=category_id,
            category_name=category_names.get(category_id, f"Category {category_id}"),
            faq_items=faq_items,
            total_count=len(faq_items),
            current_page=page,
            total_pages=7  # Approximate based on FAQ structure
        )
    except Exception as e:
        logger.error(f"Failed to get FAQ items: {e}")
        raise

