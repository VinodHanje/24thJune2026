import json
from playwright.sync_api import APIRequestContext
file_path = "C:\\python_playwright\\June2026_batch2_playwright_APITesting\\global_data.json"
def test_add_an_item_to_cart(before_each_test: APIRequestContext):
    # Load the global data from the JSON file
    with open(file_path, "r") as file:
        data = json.load(file)
    
    cart_id = data.get("cart_id")
    # Define the item to be added to the cart
    payload = {
   "productId": 4643,
   "quantity": 2
     }
    
    # Send a POST request to add an item to the cart
    response = before_each_test.post(f"/carts/{cart_id}/items", data=payload)
    
    # Assert that the response status is 201 (Created)
    assert response.status == 201
    
    # Print the response JSON for debugging purposes
    print(json.dumps(response.json(), indent=4))
    data["item_id"] = response.json()["itemId"]
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

        