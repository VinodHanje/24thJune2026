import json
from playwright.sync_api import Playwright


def test_api_key_auth(playwright: Playwright):    # Replace this placeholder with a real PAT in CI or set via environment variables    api_key = "GITHUB_PAT_PLACEHOLDER"    request = playwright.request.new_context()    response = request.get(        "https://api.github.com/user/repos",        headers={            "Authorization": f"Bearer {api_key}"        }    )    assert response.status == 200    print(json.dumps(response.json()[1]["full_name"], indent=4))    request.dispose()