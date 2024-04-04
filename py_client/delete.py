import requests

product_id = input("What is the Product Id you want to use\n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not valid\n")

endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

get_response = requests.delete(endpoint)
print("\n")
print(get_response.status_code, get_response.status_code == 204)
