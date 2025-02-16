"""Combined router to import all the routes for the FastAPI application.

This module imports all the routers for the FastAPI application and combines
them into a single router. This allows the FastAPI application to include all
the routes with a single import and keeps the main app module clean.

It is also now very easy to change the prefix for all the routes in the APIin
one place. This is done by setting the prefix parameter in the ApiRouter call.
"""

from fastapi import APIRouter

from api.routes import auth, heartbeat, home, users

api_router = APIRouter(prefix="/api/v1")

# Include the home router. This allows the API to respond to requests to the
# '/' endpoint. In this case, the home router will return a simple message.
api_router.include_router(home.router)
# Include the auth router
api_router.include_router(auth.router)
# Include the user router
api_router.include_router(users.router)
# Include the heartbeat router. This allows the API to respond to requests to
# the /heartbeat endpoint. This is useful for monitoring the health of the API.
api_router.include_router(heartbeat.router)
