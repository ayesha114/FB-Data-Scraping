# rate_limit_handler.py

import requests
from setup import ACCESS_TOKEN, BASE_URL

def check_rate_limits():
    """Function to check rate limits for the Graph API."""
    endpoint = f"{BASE_URL}me?access_token={ACCESS_TOKEN}"
    response = requests.get(endpoint)
    rate_limits = response.headers.get('x-app-usage', "{}")  # Default to an empty JSON string
    return rate_limits

