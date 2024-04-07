import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("Enter Username\n")
password = getpass()

endpoint = "http://localhost:8000/api/products/"
auth_response = requests.post(
    auth_endpoint, json={"username": username, "password": password}
)
print(auth_response.json())
token = auth_response.json()["token"]
headers = {"Authorization": f"Bearer {token}"}  # Added space after "Token"

get_response = requests.get(endpoint, headers=headers)
data = get_response.json()
# print(data)
for item in data:
    print("------")
    for key, value in item.items():
        if isinstance(value, dict):  # Check if the value is a dictionary
            print(f"{key}:")
            for nested_key, nested_value in value.items():
                print(f"  {nested_key}: {nested_value}")
        else:
            print(f"{key}: {value}")
