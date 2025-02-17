"""Setup the User Manager class."""

import uuid
from collections.abc import AsyncGenerator
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from api.auth import SECRET, auth_backend
from api.db import get_user_db
from api.log_config import logger
from api.models import User


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """Define the UserManager."""

    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
        self, user: User, _request: Optional[Request] = None
    ) -> None:
        """Called after a user has registered."""
        logger.info(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, _request: Optional[Request] = None
    ) -> None:
        """Called after a user has requested a password reset."""
        logger.info(
            f"User {user.id} has forgot their password. Reset token: {token}"
        )

    async def on_after_request_verify(
        self, user: User, token: str, _request: Optional[Request] = None
    ) -> None:
        """Called after a user has requested a verification."""
        logger.info(
            f"Verification requested for user {user.id}. "
            f"Verification token: {token}"
        )


async def get_user_manager(
    user_db: SQLAlchemyUserDatabase[User, uuid.UUID] = Depends(get_user_db),
) -> AsyncGenerator[UserManager, None]:
    """Get the user manager as a generator."""
    yield UserManager(user_db)


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)
