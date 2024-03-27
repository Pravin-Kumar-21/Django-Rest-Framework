import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/"


# a cool thing about python request  library is that we can pass my own json file
get_response = requests.get(
    endpoint, json={"mydata": "Hello Python Developer"}
)  # this is an HTTP request
"""
HTTP Request -> HTML [a http request will get a html response] [request made for browsers or the humans]

and a 

REST API HTTP Request -> JSON (.XML) [a rest api send a response in a JSON format]
(we say it a rest api request which is still a HTTP request)
[rest api requests is not ment for humans, it is ment for software to communicate with each other ]

Javascript Object Notation(JSON) ~ Python Dict

"""  # type:ignore
print(
    get_response.text
)  # this will fetch the source code from the internet in text format

# print(get_response.json())  # this give us back a python dictionary data
"""
we see that the data that we sent in a json type of a python dictionary is echoed back 
so this is how we are going to play with data 
"""

print(get_response.status_code)
print(get_response.json()["Message"])
