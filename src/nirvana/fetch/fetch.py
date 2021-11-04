import requests

# Generic function that calls an HTTP GET request to the endpoint and then uses converter to transform the response to a sensible data model
def fetch(endpoint, converter):
    print(f"Fetching from endpoint: {endpoint}")
    response = requests.get(endpoint)
    return converter(response)