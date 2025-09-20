"""Command line interface."""

from argparse import ArgumentParser
import asyncio

import yaml
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

from example.graph import graph


def parse_args():
    """Parse CLI arguments."""
    parser = ArgumentParser()
    parser.add_argument(
        "--mcp-config",
        type=str,
        default="./config/mcp.yaml",
    )
    return parser.parse_args()


def main():
    """Main."""
    load_dotenv()
    args = parse_args()

    # Setup MCP
    with open(args.mcp_config, "r", encoding="utf-8") as f:
        mcp_config = yaml.load(f, Loader=yaml.Loader)
    client = MultiServerMCPClient(mcp_config)
    tools = asyncio.run(client.get_tools())
    print(f"Tools found: {tools}")

    # Compile Graph and execute
    agent = graph().compile()
    for chunk in agent.stream(
        input={},
        context={},
        stream_mode="updates",
    ):
        print(chunk)


if __name__ == "__main__":
    main()
