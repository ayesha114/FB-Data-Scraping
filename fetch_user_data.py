# fetch_user_data.py

from setup import BASE_URL, ACCESS_TOKEN, make_request

# Fetch details about the authenticated user
def fetch_user_details():
    endpoint = f"{BASE_URL}me?access_token={ACCESS_TOKEN}"
    user_data = make_request(endpoint)
    return user_data

if __name__ == '__main__':
    print(fetch_user_details())
