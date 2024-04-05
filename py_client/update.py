import requests

endpoint = "http://localhost:8000/api/products/18/update/"

get_response = requests.put(
    endpoint,
    json={
        "title": "Xiaomi",
        "content": "Wide Range of Phones and Tablets",
    },
)
print("\n")
print(get_response.json())
print("\n")
print(get_response.status_code)
