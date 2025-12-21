import re
from typing import Any, TypeVar

from nifcloud import session

from settings import Settings

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
    """
    settings = Settings()
    return session.get_session().create_client(
        service,
        region_name=settings.NIFCLOUD_DEFAULT_REGION,
        nifcloud_access_key_id=settings.NIFCLOUD_ACCESS_KEY_ID.get_secret_value(),
        nifcloud_secret_access_key=settings.NIFCLOUD_SECRET_ACCESS_KEY.get_secret_value(),
    )


def call_nifcloud_api(
    service: str, api_method: str, response_type: type[T]
) -> T:
    """
    Generic helper to call Nifcloud API and convert response.
    
    Args:
        service: The service name (e.g., 'computing', 'rdb')
        api_method: The API method name (e.g., 'describe_instances')
        response_type: The Pydantic model type for the response
    
    Returns:
        Parsed response object of the specified type
    
    Raises:
        Exception: If the API call fails
    """
    client = get_nifcloud_client(service)
    api_func = getattr(client, api_method)
    response = api_func()
    converted_response = convert_keys_to_snake_case(response)
    return response_type(**converted_response)
