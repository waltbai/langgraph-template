"""Router."""

import json

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from langgraph_sdk import get_client


router = APIRouter(
    prefix="",
    responses={404: {"description": "Not found"}},
)


@router.get("/start")
async def start():
    """Start and stream a task."""
    async def start_task():
        client = get_client(url="http://localhost:2024")
        async for chunk in client.runs.stream(
            None,   # Threadless run
            "agent",  # Assistant name
            input={},
            stream_mode="updates",
        ):
            yield json.dumps(chunk.data)

    return StreamingResponse(start_task())
