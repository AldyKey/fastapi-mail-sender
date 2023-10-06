import uvicorn
from fastapi import FastAPI

from app.config import settings
from app.api import list_of_routes
from app.middleware import LoggingMiddleware


def bind_routes(application: FastAPI) -> None:
    for route in list_of_routes:
        application.include_router(route, prefix=settings.PATH_PREFIX)


def get_app() -> FastAPI:
    application = FastAPI(
        docs_url="/swagger",
        openapi_url="/openapi",
    )
    application.add_middleware(LoggingMiddleware)

    bind_routes(application)

    return application


app = get_app()

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        port=settings.APP_PORT,
        reload=True
    )
