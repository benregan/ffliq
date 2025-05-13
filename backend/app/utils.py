"""
Common utility functions for FFLIQ backend.
Add shared helpers here as needed.
"""
from typing import Any

def to_camel_case(snake_str: str) -> str:
    """Convert snake_case string to camelCase."""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
