import os
from typing import Optional


DEFAULT_WORLD = os.environ.get(
    "HELLO_WORLD",
    default="world",
)


def hello(world: Optional[str] = None):
    world = world or DEFAULT_WORLD
    return f"Hello, {world}"


if __name__ == "__main__":
    print(hello())
