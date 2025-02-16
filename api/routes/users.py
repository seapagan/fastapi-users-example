"""Define the User routes for the API."""

from fastapi import APIRouter

from api.managers.user import fastapi_users
from api.schema.user import UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])

router.include_router(
    fastapi_users.get_users_router(
        UserRead, UserUpdate, requires_verification=True
    )
)
