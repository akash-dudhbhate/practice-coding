"""SOLUTION: get_user — fetch GitHub user profile (Easy)"""
import requests

def get_user(username):
    """Fetch a GitHub user profile and return JSON data."""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    user = get_user("torvalds")
    print(f"Name: {user['name']}")
    print(f"Followers: {user['followers']}")
