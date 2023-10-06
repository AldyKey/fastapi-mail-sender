import pytest
from fastapi.testclient import TestClient
from app.main import get_app


client = TestClient(get_app())
