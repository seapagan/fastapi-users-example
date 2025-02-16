"""Define the User Model for the API."""

from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from api.models import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    """Define the User model."""
