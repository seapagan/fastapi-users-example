"""Main module for the FastAPI application."""

from api.routes import heartbeat, home
from fastapi import FastAPI

app = FastAPI()

app.include_router(home.router)
app.include_router(heartbeat.router)
