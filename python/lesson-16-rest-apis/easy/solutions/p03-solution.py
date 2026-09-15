"""SOLUTION: search_joke — fetch a joke from free API (Easy)"""
import requests

def search_joke(keyword=None):
    """Fetch a joke from the Official Joke API. Returns joke text."""
    if keyword:
        url = f"https://official-joke-api.appspot.com/jokes/random"
    else:
        url = "https://official-joke-api.appspot.com/jokes/random"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return f"{data['setup']} - {data['punchline']}"

if __name__ == "__main__":
    joke = search_joke()
    print(joke)
