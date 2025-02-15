"""Add a 'heartbeat' route to the API.

This just allows an easyh way for tools to check if the API is up and running.
"""

from fastapi import APIRouter

router = APIRouter(tags=["Heartbeat"])


@router.get("/heartbeat", summary="Check if the API is up and running.")
async def read_heartbeat() -> dict[str, str]:
    """Heartbeat check to ensure the API is up and running."""
    return {"status": "ok"}
