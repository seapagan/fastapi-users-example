"""Setup up the authentication system for the API."""

from collections.abc import AsyncGenerator
from typing import Any

from fastapi import Depends
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
)
from fastapi_users.authentication.strategy.db import (
    AccessTokenDatabase,
    DatabaseStrategy,
)
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTableUUID,
)
from sqlalchemy.ext.asyncio import AsyncSession

from api.db import get_async_session
from api.models import Base

SECRET = "THIS_IS_NOT_A_REAL_SECRET"  # noqa: S105

bearer_transport = BearerTransport(tokenUrl="auth/login")


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    """Define the access token table."""


async def get_access_token_db(
    session: AsyncSession = Depends(get_async_session),
) -> AsyncGenerator[SQLAlchemyAccessTokenDatabase[AccessToken], Any]:
    """Get the access token database."""
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)


def get_database_strategy(
    access_token_db: AccessTokenDatabase[AccessToken] = Depends(
        get_access_token_db
    ),
) -> DatabaseStrategy[Any, Any, AccessToken]:
    """Get the database strategy - we store access tokens in the database."""
    return DatabaseStrategy(access_token_db, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="db_strategy",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
