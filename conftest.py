import json
from pathlib import Path
from playwright.sync_api import Playwright
import pytest

# Use a path relative to this file so tests work regardless of CWD
filepath = Path(__file__).resolve().parent / "global_data.json"
@pytest.fixture(scope="function")
def before_each_test(playwright: Playwright):
    #Load the global data from the JSON file
    with open(filepath, "r") as file:
        data = json.load(file)
    request = playwright.request.new_context(base_url=data["base_url"])
    yield request
    request.dispose()
