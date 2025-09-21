"""MCP math tools."""

from typing import Annotated
from fastmcp import FastMCP


mcp = FastMCP(name="math")


@mcp.tool
def add(
    a: Annotated[int, "the first number"],
    b: Annotated[int, "the second number"],
) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool
def multiply(
    a: Annotated[int, "the first number"],
    b: Annotated[int, "the second number"],
) -> int:
    """Multiply two numbers."""
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio")
