"""Main module for the FastAPI application."""

from fastapi import FastAPI

from api.routes import heartbeat, home

app = FastAPI()

app.include_router(home.router)
app.include_router(heartbeat.router)
