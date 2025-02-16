"""Define Authentication routes for the API."""

import uuid

from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from api.auth import auth_backend
from api.managers.user import get_user_manager
from api.models import User

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

router = APIRouter()
router.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
    prefix="/auth/jwt",
    tags=["auth"],
)
