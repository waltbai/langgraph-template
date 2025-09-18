"""Graph."""

from typing import Any, Dict

from langchain_core.messages import HumanMessage
from langgraph.graph import END, START, StateGraph
from langgraph.runtime import Runtime

from example.context import Context
from example.state import State


def graph():
    """Agent graph."""
    builder = StateGraph(
        State,
        context_schema=Context,
    )

    # Nodes
    builder.add_node("mock_node1", mock_node1)
    builder.add_node("mock_node2", mock_node2)

    # Edges
    builder.add_edge(START, "mock_node1")
    builder.add_edge("mock_node1", "mock_node2")
    builder.add_edge("mock_node2", END)

    return builder


def mock_node1(
    state: State,
    runtime: Runtime[Context],
) -> Dict[str, Any]:
    """Mock node."""
    return {
        "history": [HumanMessage("Hello, this is node 1.")],
        "dynamic_state": "node1",
    }


def mock_node2(
    state: State,
    runtime: Runtime[Context],
) -> Dict[str, Any]:
    """Mock node."""
    return {
        "history": [HumanMessage("Hello, this is node 2.")],
        "dynamic_state": "node2",
    }
