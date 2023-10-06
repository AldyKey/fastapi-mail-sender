from .health import api_router as ping_router
from .v1.email import api_router as email_router

list_of_routes = [
    ping_router,
    email_router
]

__all__ = [
    "list_of_routes"
]