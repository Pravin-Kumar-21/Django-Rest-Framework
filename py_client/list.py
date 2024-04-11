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
"""
Here we have created a 
"""
# next_url = data["next"]
# if next_url is not None:
#     print(next_url)
#     result = data["results"]
#     print(result)
#     next_url = data["next"]
next_url = data.pop("next")
print(next_url)
data = data["results"]
for item in data:
    print("------")
    for key, value in item.items():
        if isinstance(value, dict):  # Check if the value is a dictionary
            print(f"{key}:")
            for nested_key, nested_value in value.items():
                print(f"  {nested_key}: {nested_value}")
        else:
            print(f"{key}: {value}")

"""
So we have done a default pagination of 5 so the total in divided into querysets 5 objects in one page 
followed by next 5 in the other page
"""
