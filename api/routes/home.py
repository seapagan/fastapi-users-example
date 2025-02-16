"""Home routes for the API."""

from typing import Annotated

from fastapi import APIRouter, Depends

from api.managers.user import current_active_user
from api.models import User

router = APIRouter(
    tags=["Home"],
)


@router.get("/")
async def read_root() -> dict[str, str]:
    """Currently a placeholder for the root route."""
    return {"Hello": "World"}


@router.get("/authenticated-route")
async def authenticated_route(
    user: Annotated[User, Depends(current_active_user)],
) -> dict[str, str]:
    """Example of an authenticated route."""
    return {"message": f"Hello {user.email}!"}
