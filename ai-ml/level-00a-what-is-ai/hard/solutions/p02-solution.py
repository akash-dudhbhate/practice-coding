"""Solution — hard/p02-what-is-an-agent.py"""


def choose_action(query):
    q = query.lower()
    if "weather" in q or "temperature" in q:
        return "get_weather"
    if "search" in q or "find" in q or "look up" in q:
        return "web_search"
    if "email" in q or "send" in q or "mail" in q:
        return "send_email"
    if "calculate" in q or "math" in q or "+" in q or "-" in q:
        return "calculator"
    return "chat"
