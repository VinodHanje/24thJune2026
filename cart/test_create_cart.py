import json
from playwright.sync_api import APIRequestContext
file_path = "C:\\python_playwright\\June2026_batch2_playwright_APITesting\\global_data.json"
def test_create_new_cart (before_each_test: APIRequestContext):
        response = before_each_test.post("/carts")
        with open(file_path, "r") as file:
            data = json.load(file)
           
        assert response.status == 201
        print(json.dumps(response.json(),indent=4))
        data["cart_id"] = response.json()["cartId"]
        with open(file_path, "w") as file:
            json.dump(data, file,indent=4)


        