from fastapi import APIRouter, Depends, Request
from starlette import status

from app.schemas import PingResponse


api_router = APIRouter(
    prefix="/health",
    tags=["Application Health"],
)


@api_router.get(
    "/ping",
    response_model=PingResponse,
    status_code=status.HTTP_200_OK
)
async def ping_application(_: Request):
    return {"message": "pong"}
