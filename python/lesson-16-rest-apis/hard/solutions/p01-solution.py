"""SOLUTION: APIClient class with Session (Hard)"""
import requests

class APIClient:
    """REST API client with session, auth, and automatic error handling."""

    def __init__(self, base_url, token=None, timeout=30):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.timeout = timeout
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"
        self.session.headers["Accept"] = "application/json"

    def _request(self, method, path, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        kwargs.setdefault("timeout", self.timeout)
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        if response.content:
            return response.json()
        return None

    def get(self, path, **kwargs):
        return self._request("GET", path, **kwargs)

    def post(self, path, data=None, **kwargs):
        return self._request("POST", path, json=data, **kwargs)

    def put(self, path, data=None, **kwargs):
        return self._request("PUT", path, json=data, **kwargs)

    def delete(self, path, **kwargs):
        return self._request("DELETE", path, **kwargs)

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

if __name__ == "__main__":
    with APIClient("https://api.github.com") as client:
        user = client.get("/users/torvalds")
        print(user["name"])
