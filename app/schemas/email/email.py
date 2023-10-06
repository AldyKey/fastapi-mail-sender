from pydantic import BaseModel, EmailStr, Field


class EmailSendRequest(BaseModel):
    receiver: EmailStr = Field(..., alias="to")
    subject: str
    message: str
