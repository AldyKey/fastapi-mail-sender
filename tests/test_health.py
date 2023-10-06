from .conftest import client


def test_health_ping():
    response = client.get("/api/v1/health/ping")

    assert response.status_code == 200


