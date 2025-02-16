"""Define Authentication routes for the API."""

from fastapi import APIRouter

from api.auth import auth_backend
from api.managers.user import fastapi_users
from api.schema.user import UserCreate, UserRead

router = APIRouter(prefix="/auth", tags=["Auth"])
router.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
)
router.include_router(
    fastapi_users.get_reset_password_router(),
)
