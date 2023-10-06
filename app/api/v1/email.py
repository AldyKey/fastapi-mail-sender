from fastapi import APIRouter, Depends, Request, HTTPException
from starlette import status
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from app.schemas import EmailSendRequest
from app.config import settings


api_router = APIRouter(
    prefix="/email",
    tags=["Email Sending"],
)


@api_router.post(
    "/send_email",
    status_code=status.HTTP_200_OK
)
async def ping_application(request: EmailSendRequest):
    smtp_connection = settings.smtp_settings
    message = MessageSchema(
        subject=request.subject,
        recipients=[request.receiver],
        body=request.message,
        subtype="html"
    )
    fm = FastMail(smtp_connection)

    try:
        sent = await fm.send_message(message)

        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
