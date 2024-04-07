import requests


headers = {"Authorization": "Bearer bdb4b6155be1295579c6787ce6954d7edcb8963b"}
endpoint = "http://localhost:8000/api/products/"

data = {"title": "Samsung", "content": "Market Lead in Phones and Tablets"}

"""
We are using are own custom authentication , also we have created our own custom authenication
so we need to pass the token in the headers file 
"""
get_response = requests.post(endpoint, json=data, headers=headers)
print("\n")
print(get_response.json())
print(get_response.status_code)
print("\n")
