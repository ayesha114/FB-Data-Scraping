import requests
import os  # used to get the environment variable

# This script sets up the basic configuration for the Facebook Graph API.
BASE_URL = 'https://graph.facebook.com/v12.0/'  # 'v12.0' is the API version; it may change in the future.

# If you decide to use environment variables, you can fetch the access token like this:
# ACCESS_TOKEN = os.getenv('FB_ACCESS_TOKEN')
# Otherwise, for the sake of this example, I'm leaving your hardcoded token (but it's not recommended)
ACCESS_TOKEN = '2665521916937464|MKn2F-teHWGiwP-1Ej4SYEhZcsA'

def make_request(endpoint):
    """Function to make a request to the Graph API and return the JSON data."""
    try:
        response = requests.get(endpoint, timeout=10)  # timeout after 10 seconds
        if response.status_code != 200:
            return {"error": f"HTTP Status {response.status_code}: {response.text}"}
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

