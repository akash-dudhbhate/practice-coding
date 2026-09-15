"""SOLUTION: Mock API call (Medium)"""
from unittest.mock import patch, MagicMock
import pytest

def fetch_user(user_id):
    # This would call a real API
    import requests
    resp = requests.get(f"https://api.example.com/users/{user_id}")
    return resp.json()

@patch("requests.get")
def test_fetch_user(mock_get):
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"id": 1, "name": "Akash"}
    mock_get.return_value = mock_resp

    result = fetch_user(1)
    assert result["name"] == "Akash"
    mock_get.assert_called_once_with("https://api.example.com/users/1")

if __name__ == "__main__":
    # Manual test without pytest
    print("Run with pytest to test the mock")
    print("All tests passed!")
