"""Setup the User Manager class."""

# ruff: noqa: T201
import uuid
from collections.abc import AsyncGenerator
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from api.auth import SECRET
from api.db import get_user_db
from api.models import User


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """Define the UserManager."""

    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
        self, user: User, _request: Optional[Request] = None
    ) -> None:
        """Called after a user has registered."""
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, _request: Optional[Request] = None
    ) -> None:
        """Called after a user has requested a password reset."""
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, _request: Optional[Request] = None
    ) -> None:
        """Called after a user has requested a verification."""
        print(
            f"Verification requested for user {user.id}. "
            f"Verification token: {token}"
        )


async def get_user_manager(
    user_db: SQLAlchemyUserDatabase[User, uuid.UUID] = Depends(get_user_db),
) -> AsyncGenerator[UserManager, None]:
    """Get the user manager as a generator."""
    yield UserManager(user_db)
