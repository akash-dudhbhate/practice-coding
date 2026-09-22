"""
LESSON 16 — REST APIs
MEDIUM P02 — Create Issue (POST with auth)
============================================

CONCEPT:
  POST sends a JSON body (`json=data`) and auth goes in headers.
  Check status codes yourself for clear errors: 401 bad token,
  403 forbidden, 422 bad data.

PROBLEM:
  Write `create_issue(owner, repo, title, body, token)` that POSTs
  to `https://api.github.com/repos/{owner}/{repo}/issues` with an
  Authorization token header and JSON body {"title", "body"}.
  Raise ValueError on 401/422, PermissionError on 403, otherwise
  raise_for_status() and return the parsed JSON.

TRY THIS INPUT:
  ```python
  # needs a real token:
  # issue = create_issue("me", "repo", "Bug", "details", TOKEN)
  # print(issue["number"])
  ```

EXPECTED OUTPUT:
  ```
  <issue number>
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
