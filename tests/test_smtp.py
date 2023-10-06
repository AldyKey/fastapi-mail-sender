import pytest

from .conftest import client
from app.config import settings


def test_send_email_success():
    response = client.post("/api/v1/email/send_email", json={
        "to": settings.MAIL_TEST,
        "subject": "yeahey",
        "message": "asdasdasd"
    })

    assert response.status_code == 200
    assert response.json() == {"message": "Email sent successfully"}


def test_send_email_failed():
    response = client.post("/api/v1/email/send_email", json={
        "to": "savghbdj",
        "subject": "yeahey",
        "message": "asdasdasd"
    })

    assert response.status_code == 422
