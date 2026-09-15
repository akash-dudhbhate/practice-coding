"""
SOLUTION: Extract Email Domain (Hard)
======================================
Extract the domain from an email. "user@gmail.com" -> "gmail.com".
"""
def extract_domain(email: str) -> str:
    if "@" not in email:
        return ""
    return email.split("@")[1]

if __name__ == "__main__":
    assert extract_domain("user@gmail.com") == "gmail.com"
    assert extract_domain("test@company.co.uk") == "company.co.uk"
    assert extract_domain("noatsign") == ""
    print("All tests passed!")
