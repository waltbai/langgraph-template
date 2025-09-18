"""App."""

from fastapi import FastAPI
import uvicorn

from example.server import router


app = FastAPI()
app.include_router(router.router)


def main():
    """Run server."""
    uvicorn.run(app, host="localhost", port=8000)
