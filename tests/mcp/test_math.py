"""Test mcp math tools."""

from fastmcp import Client

from example.mcp.math import mcp


async def test_list_tools():
    """Test listing tools."""
    async with Client(mcp) as client: 
        tools = await client.list_tools()
        assert len(tools) == 2
        assert tools[0].name == "add"
        assert tools[1].name == "multiply"


async def test_add():
    """Test add tool."""
    async with Client(mcp) as client:
        result = await client.call_tool("add", {"a": 1, "b": 2})
        assert result.structured_content["result"] == 3


async def test_multiply():
    """Test multiply tool."""
    async with Client(mcp) as client:
        result = await client.call_tool("multiply", {"a": 2, "b": 3})
        assert result.structured_content["result"] == 6
