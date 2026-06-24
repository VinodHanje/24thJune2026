import json
from playwright.sync_api import APIRequestContext


def test_status_24thjune2026(before_each_test: APIRequestContext):
    response = before_each_test.get("/status")
    print(f"status code ={response.status}")
    assert response.status == 200
    body = response.json()
    print(json.dumps(body, indent=2))
    assert body == {"status": "UP"}
