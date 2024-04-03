import requests

endpoint = "http://localhost:8000/api/products/"

data = {"title": "Infinix"}
get_response = requests.post(endpoint, json=data)
print("\n")
print(get_response.json())
print(get_response.status_code)
print("\n")
