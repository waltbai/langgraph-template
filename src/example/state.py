"""State."""

from typing import Annotated, TypedDict

from langgraph.graph.message import add_messages


class State(TypedDict):
    """State."""
    history: Annotated[list, add_messages]
