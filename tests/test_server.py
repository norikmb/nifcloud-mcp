"""Tests for server module."""
import pytest
from unittest.mock import Mock, patch

from src import server


class TestToolEndpoints:
    """Test MCP tool endpoints."""

    @patch("src.server.call_nifcloud_api")
    def test_get_server_list_success(self, mock_api):
        """Test get_server_list tool."""
        mock_response = Mock()
        mock_api.return_value = mock_response

        result = server.get_server_list()

        assert result == mock_response
        mock_api.assert_called_once_with("computing", "describe_instances", server.DescribeInstancesResponse)

    @patch("src.server.call_nifcloud_api")
    def test_get_server_list_error(self, mock_api):
        """Test get_server_list tool with error."""
        mock_api.side_effect = Exception("API Error")

        with pytest.raises(Exception, match="API Error"):
            server.get_server_list()

    @patch("src.server.call_nifcloud_api")
    def test_get_disk_list_success(self, mock_api):
        """Test get_disk_list tool."""
        mock_response = Mock()
        mock_api.return_value = mock_response

        result = server.get_disk_list()

        assert result == mock_response
        mock_api.assert_called_once_with("computing", "describe_volumes", server.DescribeVolumesResponse)

    @patch("src.server.call_nifcloud_api")
    def test_get_load_balancer_list_success(self, mock_api):
        """Test get_load_balancer_list tool."""
        mock_response = Mock()
        mock_api.return_value = mock_response

        result = server.get_load_balancer_list()

        assert result == mock_response
        mock_api.assert_called_once_with("computing", "describe_load_balancers", server.DescribeLoadBalancersResponse)

    @patch("src.server.call_nifcloud_api")
    def test_get_firewall_list_success(self, mock_api):
        """Test get_firewall_list tool."""
        mock_response = Mock()
        mock_api.return_value = mock_response

        result = server.get_firewall_list()

        assert result == mock_response
        mock_api.assert_called_once_with("computing", "describe_security_groups", server.DescribeSecurityGroupsResponse)

    @patch("src.server.call_nifcloud_api")
    def test_get_router_list_success(self, mock_api):
        """Test get_router_list tool."""
        mock_response = Mock()
        mock_api.return_value = mock_response

        result = server.get_router_list()

        assert result == mock_response
        mock_api.assert_called_once_with("computing", "nifty_describe_routers", server.NiftyDescribeRoutersResponse)

    @patch("src.server.call_nifcloud_api")
    def test_get_db_list_success(self, mock_api):
        """Test get_db_list tool."""
        mock_response = Mock()
        mock_api.return_value = mock_response

        result = server.get_db_list()

        assert result == mock_response
        mock_api.assert_called_once_with("rdb", "describe_db_instances", server.DescribeDBInstancesResponse)

    @patch("src.server.call_nifcloud_api")
    def test_get_db_list_error(self, mock_api):
        """Test get_db_list tool with error."""
        mock_api.side_effect = Exception("Database error")

        with pytest.raises(Exception, match="Database error"):
            server.get_db_list()
