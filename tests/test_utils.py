"""Tests for utils module."""
import pytest
from unittest.mock import Mock, patch

from src.utils import (
    camel_to_snake,
    convert_keys_to_snake_case,
    get_nifcloud_client,
    call_nifcloud_api,
)


class TestCamelToSnake:
    """Test camel_to_snake function."""

    def test_camel_to_snake_basic(self):
        """Test basic camelCase conversion."""
        assert camel_to_snake("camelCase") == "camel_case"
        assert camel_to_snake("PascalCase") == "pascal_case"
        assert camel_to_snake("simpleword") == "simpleword"

    def test_camel_to_snake_db_prefix(self):
        """Test DB prefix handling."""
        assert camel_to_snake("DBInstance") == "db_instance"
        assert camel_to_snake("DBName") == "db_name"

    def test_camel_to_snake_consecutive_capitals(self):
        """Test consecutive capital letters."""
        assert camel_to_snake("XMLParser") == "x_m_l_parser"
        assert camel_to_snake("HTTPResponse") == "h_t_t_p_response"


class TestConvertKeysToSnakeCaseSnakeCaseRecursively:
    """Test convert_keys_to_snake_case function."""

    def test_convert_dict(self):
        """Test dictionary conversion."""
        data = {"camelKey": "value", "AnotherKey": "test"}
        result = convert_keys_to_snake_case(data)
        assert result == {"camel_key": "value", "another_key": "test"}

    def test_convert_nested_dict(self):
        """Test nested dictionary conversion."""
        data = {"outerKey": {"innerKey": "value"}}
        result = convert_keys_to_snake_case(data)
        assert result == {"outer_key": {"inner_key": "value"}}

    def test_convert_list(self):
        """Test list conversion."""
        data = ["value1", "value2"]
        result = convert_keys_to_snake_case(data)
        assert result == ["value1", "value2"]

    def test_convert_list_of_dicts(self):
        """Test list of dictionaries conversion."""
        data = [{"camelKey": "value1"}, {"camelKey": "value2"}]
        result = convert_keys_to_snake_case(data)
        assert result == [{"camel_key": "value1"}, {"camel_key": "value2"}]

    def test_remove_response_metadata(self):
        """Test ResponseMetadata removal."""
        data = {"camelKey": "value", "ResponseMetadata": {"extra": "data"}}
        result = convert_keys_to_snake_case(data)
        assert "response_metadata" not in result
        assert "camel_key" in result


class TestGetNifcloudClient:
    """Test get_nifcloud_client function."""

    @patch("src.utils.session.get_session")
    @patch("src.utils.Settings")
    def test_get_client_success(self, mock_settings, mock_session):
        """Test successful client creation."""
        # Setup mocks
        mock_settings_instance = Mock()
        mock_settings_instance.NIFCLOUD_DEFAULT_REGION = "jp-east-1"
        mock_settings_instance.NIFCLOUD_ACCESS_KEY_ID.get_secret_value.return_value = "test_key"
        mock_settings_instance.NIFCLOUD_SECRET_ACCESS_KEY.get_secret_value.return_value = "test_secret"
        mock_settings.return_value = mock_settings_instance

        mock_session_instance = Mock()
        mock_client = Mock()
        mock_session_instance.create_client.return_value = mock_client
        mock_session.return_value = mock_session_instance

        # Call function
        result = get_nifcloud_client("computing")

        # Assert
        assert result == mock_client
        mock_session_instance.create_client.assert_called_once_with(
            "computing",
            region_name="jp-east-1",
            nifcloud_access_key_id="test_key",
            nifcloud_secret_access_key="test_secret",
        )

    @patch("src.utils.session.get_session")
    @patch("src.utils.Settings")
    def test_get_client_settings_error(self, mock_settings, mock_session):
        """Test client creation with settings error."""
        mock_settings.side_effect = ValueError("Missing environment variables")

        with pytest.raises(ValueError, match="Missing environment variables"):
            get_nifcloud_client("computing")

    @patch("src.utils.session.get_session")
    @patch("src.utils.Settings")
    def test_get_client_network_error(self, mock_settings, mock_session):
        """Test client creation with network error."""
        mock_settings_instance = Mock()
        mock_settings_instance.NIFCLOUD_DEFAULT_REGION = "jp-east-1"
        mock_settings_instance.NIFCLOUD_ACCESS_KEY_ID.get_secret_value.return_value = "test_key"
        mock_settings_instance.NIFCLOUD_SECRET_ACCESS_KEY.get_secret_value.return_value = "test_secret"
        mock_settings.return_value = mock_settings_instance

        mock_session.return_value.create_client.side_effect = Exception("Network error")

        with pytest.raises(Exception):
            get_nifcloud_client("computing")


class TestCallNifcloudApi:
    """Test call_nifcloud_api function."""

    @patch("src.utils.get_nifcloud_client")
    def test_call_api_success(self, mock_get_client):
        """Test successful API call."""
        # Setup mock
        mock_client = Mock()
        mock_client.describe_instances.return_value = {
            "reservation": [{"instance_id": "i-123"}],
            "ResponseMetadata": {},
        }
        mock_get_client.return_value = mock_client

        # Create a simple mock response type
        class MockResponseType:
            def __init__(self, **kwargs):
                self.data = kwargs

        # Call function
        result = call_nifcloud_api("computing", "describe_instances", MockResponseType)

        # Assert
        assert result.data["reservation"] == [{"instance_id": "i-123"}]
        mock_get_client.assert_called_once_with("computing")
        mock_client.describe_instances.assert_called_once()

    @patch("src.utils.get_nifcloud_client")
    def test_call_api_method_not_found(self, mock_get_client):
        """Test API method not found error."""
        mock_client = Mock(spec=[])  # Empty spec means no attributes
        mock_get_client.return_value = mock_client

        class MockResponseType:
            pass

        with pytest.raises(AttributeError, match="no method"):
            call_nifcloud_api("computing", "invalid_method", MockResponseType)

    @patch("src.utils.get_nifcloud_client")
    def test_call_api_client_creation_error(self, mock_get_client):
        """Test API call with client creation error."""
        mock_get_client.side_effect = ValueError("Configuration error")

        class MockResponseType:
            pass

        with pytest.raises(ValueError, match="Configuration error"):
            call_nifcloud_api("computing", "describe_instances", MockResponseType)

    @patch("src.utils.get_nifcloud_client")
    def test_call_api_response_parsing_error(self, mock_get_client):
        """Test API call with response parsing error."""
        mock_client = Mock()
        mock_client.describe_instances.return_value = {"invalid": "data"}
        mock_get_client.return_value = mock_client

        class StrictMockResponseType:
            def __init__(self, **kwargs):
                if "reservation" not in kwargs:
                    raise ValueError("Missing required field: reservation")

        with pytest.raises(ValueError, match="Missing required field"):
            call_nifcloud_api("computing", "describe_instances", StrictMockResponseType)
