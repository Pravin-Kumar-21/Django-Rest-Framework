import requests

endpoint = "http://localhost:8000/api/products/"
get_response = requests.get(endpoint)
print("\n")
data = {}
data = get_response.json()  # converts json file to python Dictionary
for i in data:
    print(i.get("title"))
    print(i.get("content"))
    print(i.get("price"))
    print(i.get("sale_price"))
    print(i.get("discount"))
    print("\n")
# print(get_response.status_code)
