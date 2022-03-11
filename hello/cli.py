import os
from typing import Optional

from .settings import DEFAULT_HELLO_WORLD


def hello(world: Optional[str] = None):
    world = world or DEFAULT_HELLO_WORLD
    return f"Hello, {world}"

