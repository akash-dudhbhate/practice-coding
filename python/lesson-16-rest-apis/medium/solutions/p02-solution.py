"""SOLUTION: create_issue — POST with auth and error handling (Medium)"""
import requests

def create_issue(owner, repo, title, body, token):
    """Create a GitHub issue using POST with auth. Handle errors."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"title": title, "body": body}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 401:
        raise ValueError("Bad credentials — check your token")
    elif response.status_code == 403:
        raise PermissionError("Forbidden — rate limit or no permission")
    elif response.status_code == 422:
        raise ValueError("Validation failed — check issue data")
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Requires a real token to run
    print("Pass a GitHub token to test: create_issue('owner', 'repo', 'title', 'body', 'TOKEN')")
