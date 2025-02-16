"""Main module for the FastAPI application."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI

from api.db import create_db_and_tables
from api.routes import auth, heartbeat, home


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, Any]:
    """Setup the lifespan events for the FastAPI app."""
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

# Include the home router. This allows the API to respond to requests to the
# '/' endpoint. In this case, the home router will return a simple message.
app.include_router(home.router)
# Include the heartbeat router. This allows the API to respond to requests to
# the /heartbeat endpoint. This is useful for monitoring the health of the API.
app.include_router(heartbeat.router)
# Include the auth router
app.include_router(auth.router)
