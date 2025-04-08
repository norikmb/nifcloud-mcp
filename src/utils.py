import re


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
