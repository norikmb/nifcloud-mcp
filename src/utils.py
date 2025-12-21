import logging
import re
from typing import Any, TypeVar

from nifcloud import session

from .settings import Settings

# Configure logging
logger = logging.getLogger(__name__)

T = TypeVar("T")


def camel_to_snake(name):
    """Convert CamelCase to snake_case."""
    if name.startswith("DB"):
        name = name[2:]
        return "db_" + re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()

    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def convert_keys_to_snake_case(data):
    """Recursively convert dictionary keys to snake_case."""
    if isinstance(data, dict):
        if "ResponseMetadata" in data:
            del data["ResponseMetadata"]
        return {
            camel_to_snake(k): convert_keys_to_snake_case(v) for k, v in data.items()
        }
    elif isinstance(data, list):
        return [convert_keys_to_snake_case(i) for i in data]
    else:
        return data


def get_nifcloud_client(service: str):
    """
    Create and return a Nifcloud API client.
    
    Args:
        service: The service name (e.g., 'computing', 'rdb')
    
    Returns:
        A Nifcloud client instance
    
    Raises:
        ValueError: If configuration is missing or invalid
    """
    try:
        settings = Settings()
        client = session.get_session().create_client(
            service,
            region_name=settings.NIFCLOUD_DEFAULT_REGION,
            nifcloud_access_key_id=settings.NIFCLOUD_ACCESS_KEY_ID.get_secret_value(),
            nifcloud_secret_access_key=settings.NIFCLOUD_SECRET_ACCESS_KEY.get_secret_value(),
        )
        logger.debug(f"Created client for service: {service}")
        return client
    except ValueError as e:
        logger.error(f"Failed to create client for service {service}: {e}")
        raise ValueError(f"Failed to create Nifcloud client: {e}") from e
    except Exception as e:
        logger.error(f"Unexpected error creating client for service {service}: {e}")
        raise


def call_nifcloud_api(
    service: str, api_method: str, response_type: type[T], **kwargs
) -> T:
    """
    Generic helper to call Nifcloud API and convert response.
    
    Args:
        service: The service name (e.g., 'computing', 'rdb')
        api_method: The API method name (e.g., 'describe_instances')
        response_type: The Pydantic model type for the response
        **kwargs: Optional keyword arguments to pass to the API method
    
    Returns:
        Parsed response object of the specified type
    
    Raises:
        ValueError: If client creation fails
        AttributeError: If the API method does not exist
        Exception: If the API call fails or response parsing fails
    """
    try:
        logger.info(f"Calling {service}.{api_method}()")
        client = get_nifcloud_client(service)
        
        # Get the API method
        if not hasattr(client, api_method):
            logger.error(f"API method '{api_method}' not found in service '{service}'")
            raise AttributeError(f"Service '{service}' has no method '{api_method}'")
        
        api_func = getattr(client, api_method)
        
        # Call the API with optional arguments
        if kwargs:
            logger.debug(f"Calling with parameters: {list(kwargs.keys())}")
            response = api_func(**kwargs)
        else:
            response = api_func()
        logger.debug(f"Received response from {service}.{api_method}()")
        
        # Convert and parse response
        converted_response = convert_keys_to_snake_case(response)
        result = response_type(**converted_response)
        logger.info(f"Successfully processed response from {service}.{api_method}()")
        return result
        
    except AttributeError as e:
        logger.error(f"API method error: {e}")
        raise
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        raise
    except Exception as e:
        logger.error(f"Error calling {service}.{api_method}(): {type(e).__name__}: {e}")
        raise
