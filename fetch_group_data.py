# fetch_group_data.py

from setup import BASE_URL, ACCESS_TOKEN, make_request

def fetch_group_members(group_id):
    """Function to fetch members of a group."""
    endpoint = f"{BASE_URL}{group_id}/members?access_token={ACCESS_TOKEN}&limit=1000"  # Increase limit for faster scraping
    members_data = make_request(endpoint)
    return members_data