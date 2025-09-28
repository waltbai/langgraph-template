"""Router."""

from fastapi import APIRouter, BackgroundTasks

from example.graph import graph
# from langgraph_sdk import get_client


router = APIRouter(
    prefix="",
    responses={404: {"description": "Not found"}},
)


def call_agent():
    """Call agent in streaming mode and save state update."""
    agent = graph().compile()
    for chunk in agent.stream(
        input={},
        context={},
        stream_mode="updates",
    ):
        # Handle state update
        print(chunk)


@router.get("/background_start")
async def background_start(background_tasks: BackgroundTasks):
    """Start a task in the background."""
    background_tasks.add_task(call_agent)
    return {"message": "Start background task"}
