# Facebook Graph API Data Fetching

This project consists of three Python scripts that interact with the Facebook Graph API to fetch data about Facebook groups and users. It includes the following scripts:

1. **fetch_group_data.py**: This script fetches members of a Facebook group using the Facebook Graph API.

2. **fetch_user_data.py**: This script fetches details about the authenticated user using the Facebook Graph API.

3. **rate_limit_handler.py**: This script checks rate limits for the Facebook Graph API.

## Getting Started

Before you can use these scripts, make sure to set up your Facebook Graph API access token in the `setup.py` file. You can either hardcode your access token or use environment variables for better security.

```python
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN_HERE'
