"""Define schemas for the User model."""

import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    """Define the UserRead schema."""


class UserCreate(schemas.BaseUserCreate):
    """Define the UserCreate schema."""


class UserUpdate(schemas.BaseUserUpdate):
    """Define the UserUpdate schema."""
