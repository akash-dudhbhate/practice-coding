"""SOLUTION: get_repos — fetch user's repo names (Easy)"""
import requests

def get_repos(username):
    """Fetch a GitHub user's repositories and return list of repo names."""
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    response.raise_for_status()
    repos = response.json()
    return [repo["name"] for repo in repos]

if __name__ == "__main__":
    repos = get_repos("torvalds")
    print(f"Found {len(repos)} repos")
    for r in repos[:5]:
        print(f"  {r}")
