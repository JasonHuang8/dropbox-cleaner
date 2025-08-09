from fastapi.testclient import TestClient
from mock_scrubber.app import app


def test_scrub_endpoint():
    client = TestClient(app)
    response = client.post("/scrub", files={"file": ("test.txt",
                                                     b"hello world")})
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "scrubbed"
    assert body["filename"] == "test.txt"
