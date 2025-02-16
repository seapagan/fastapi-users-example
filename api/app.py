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


app = FastAPI(
    lifespan=lifespan,
    swagger_ui_parameters={"defaultModelsExpandDepth": 0},
    title="FastAPI Auth with 'fastapi-users'",
    description=(
        "A simple FastAPI application that demonstrates how to use "
        "the `fastapi-users` package for authentication."
    ),
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
    version="0.1.0",
)

# Include the home router. This allows the API to respond to requests to the
# '/' endpoint. In this case, the home router will return a simple message.
app.include_router(home.router)
# Include the heartbeat router. This allows the API to respond to requests to
# the /heartbeat endpoint. This is useful for monitoring the health of the API.
app.include_router(heartbeat.router)
# Include the auth router
app.include_router(auth.router)
