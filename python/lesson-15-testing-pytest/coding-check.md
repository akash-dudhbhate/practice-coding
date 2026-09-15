# Lesson 15 — Coding Check

## Easy

### p01-solve.py — Palindrome tests
- [ ] `is_palindrome("racecar")` returns True
- [ ] `is_palindrome("")` returns True
- [ ] `is_palindrome("Aa")` returns True (case-insensitive)
- [ ] At least 3 test functions
- [ ] All tests pass with `pytest`

### p02-solve.py — Factorial with parametrize
- [ ] `factorial(0)` returns 1
- [ ] `factorial(1)` returns 1
- [ ] `factorial(5)` returns 120
- [ ] `factorial(3)` returns 6
- [ ] Uses `@pytest.mark.parametrize` with 5 cases
- [ ] Negative input raises ValueError (or returns appropriate error)

### p03-solve.py — Fixture sample_list
- [ ] `@pytest.fixture` named `sample_list` returns `[3, 1, 4, 1, 5]`
- [ ] Test for `max(sample_list)` returns 5
- [ ] Test for `len(sample_list)` returns 5
- [ ] Both tests use the fixture by parameter name

## Medium

### p01-solve.py — Testing exceptions
- [ ] `divide(10, 2)` returns 5
- [ ] `divide(1, 0)` raises `ZeroDivisionError`
- [ ] Uses `pytest.raises(ZeroDivisionError)`
- [ ] Test passes (exception is correctly raised and caught)

### p02-solve.py — yield fixture
- [ ] Fixture creates a temporary file with content
- [ ] Yields the file path
- [ ] Cleans up (deletes) the file after test
- [ ] Test reads the file and verifies content
- [ ] File is deleted after test (check it doesn't exist)

### p03-solve.py — Mocking
- [ ] `fetch_user(1)` calls an API (e.g., `requests.get`)
- [ ] API call is mocked with `patch`
- [ ] Test does NOT make a real HTTP request
- [ ] Mock returns a fake user dict
- [ ] `fetch_user` returns the mocked data
- [ ] `mock.assert_called_once()` verifies the API was called

## Hard

### p01-solve.py — BankAccount test suite
- [ ] Test deposit: balance increases correctly
- [ ] Test withdraw: balance decreases correctly
- [ ] Test insufficient funds: raises exception
- [ ] Test negative deposit: raises ValueError
- [ ] Uses fixtures for account setup
- [ ] Uses parametrize for multiple deposit/withdraw amounts
- [ ] All tests pass

### p02-solve.py — Stack tests
- [ ] Test push adds items
- [ ] Test pop removes and returns top
- [ ] Test peek returns top without removing
- [ ] Test is_empty returns True/False correctly
- [ ] Test pop on empty stack raises exception
- [ ] Uses parametrize for push/pop sequences
- [ ] All tests pass

### p03-solve.py — CSV processor tests
- [ ] `process_csv` reads CSV and returns list of dicts
- [ ] Test with normal CSV: correct number of rows, correct keys
- [ ] Test with empty file: returns empty list
- [ ] Test with malformed CSV: handles gracefully (raises or returns partial)
- [ ] Uses yield fixture for temp file creation/cleanup
- [ ] All tests pass
