"""Home routes for the API."""

from fastapi import APIRouter

router = APIRouter(
    tags=["Home"],
)


@router.get("/")
async def read_root() -> dict[str, str]:
    """Currently a placeholder for the root route."""
    return {"Hello": "World"}
