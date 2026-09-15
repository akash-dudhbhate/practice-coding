"""SOLUTION: get_all_repos — handle pagination (Medium)"""
import requests

def get_all_repos(username):
    """Fetch ALL repos for a user, handling pagination."""
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos"
        params = {"per_page": 100, "page": page}
        response = requests.get(url, params=params)
        response.raise_for_status()
        batch = response.json()
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return [repo["name"] for repo in repos]

if __name__ == "__main__":
    repos = get_all_repos("torvalds")
    print(f"Total repos: {len(repos)}")
