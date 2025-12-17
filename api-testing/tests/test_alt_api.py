#tests/test_alt_api.py

"""
Alternate API test suite using JSONPlaceholder so you can demonstrate
the test logic locally or in CI when the primary target (Reqres) is
blocked by Cloudflare or similar protections.

Default BASE_URL:
    https://jsonplaceholder.typicode.com

You can override the base URL with the environment variable:
    BASE_API_URL (e.g. export BASE_API_URL="https://reqres.in/api")
"""

import os
import requests
import pytest

# Default to the friendly JSONPlaceholder test API. This makes local runs reliable.
BASE_URL = os.environ.get("BASE_API_URL", "https://jsonplaceholder.typicode.com")

# Basic browser-like headers to reduce chance of being blocked by naive host filtering
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

def skip_if_forbidden_or_blocked(response):
    """
    If the API returns a 403 Forbidden response (common when Cloudflare blocks scripted clients),
    mark the test as skipped so CI/test reports remain clear.
    """
    if response is None:
        pytest.skip("No response received (possible network issue).")
    if response.status_code == 403:
        pytest.skip("Target API returned 403 Forbidden (likely blocking scripted clients).")

@pytest.mark.api
@pytest.mark.positive
@pytest.mark.smoke
def test_list_users_returns_non_empty_list():
    """
    GET /users -> expect a 200 OK and a non-empty list.
    This maps to the original 'list users' functional test.
    """
    url = f"{BASE_URL}/users"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    skip_if_forbidden_or_blocked(resp)

    assert resp.status_code == 200, f"Expected 200 OK from {url}, got {resp.status_code}"
    body = resp.json()
    assert isinstance(body, list), f"Expected response body to be a list, got {type(body)}"
    assert len(body) > 0, "Expected at least one user in response"

@pytest.mark.api
@pytest.mark.positive
def test_get_single_user_returns_expected_user():
    """
    GET /users/2 -> expect 200 OK and an object with id == 2.
    This is a small deterministic check to show we read fields correctly.
    """
    url = f"{BASE_URL}/users/2"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    skip_if_forbidden_or_blocked(resp)

    assert resp.status_code == 200, f"Expected 200 OK from {url}, got {resp.status_code}"
    body = resp.json()
    assert isinstance(body, dict), "Expected JSON object for single user"
    # JSONPlaceholder user objects include an 'id' field
    assert body.get("id") == 2, f"Expected user id 2, got {body.get('id')}"

@pytest.mark.api
@pytest.mark.negative
def test_get_non_existing_user_returns_404_or_empty():
    """
    Negative test for a non-existing user id.

    Public test APIs vary:
      - Some return 404 Not Found
      - Some return 200 with empty object {}
    We accept either behavior but ensure that we don't receive a valid user id.
    """
    url = f"{BASE_URL}/users/99999"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    skip_if_forbidden_or_blocked(resp)

    # Accept 404 or 200-with-empty
    if resp.status_code == 404:
        assert True  # expected not-found
    else:
        assert resp.status_code == 200, f"Unexpected status {resp.status_code}"
        body = resp.json()
        # Body may be {} or empty list; ensure it doesn't contain a valid id
        if isinstance(body, dict):
            assert not body.get("id"), "Non-existing user should not return an id"
        else:
            # If JSONPlaceholder returns something else, ensure it's empty-ish
            assert not body, "Expected empty result for non-existing user"

@pytest.mark.api
@pytest.mark.positive
def test_create_post_success():
    """
    POST /posts -> JSONPlaceholder creates a post and returns 201 Created.
    We verify that fields are echoed and an id is generated.
    """
    url = f"{BASE_URL}/posts"
    payload = {
        "title": "nithesh-automation-test",
        "body": "dummy post for testing",
        "userId": 1,
    }
    resp = requests.post(url, json=payload, headers=HEADERS, timeout=10)
    skip_if_forbidden_or_blocked(resp)

    assert resp.status_code == 201, f"Expected 201 Created, got {resp.status_code}"
    body = resp.json()
    assert body.get("title") == payload["title"], "Response should echo sent title"
    assert body.get("body") == payload["body"], "Response should echo sent body"
    assert "id" in body, "Expected generated 'id' in created object"

@pytest.mark.api
@pytest.mark.negative
def test_invalid_endpoint_returns_404():
    """
    Call an endpoint that doesn't exist on JSONPlaceholder and expect a 404/405.
    This mirrors negative tests for missing parameters on other APIs.
    """
    url = f"{BASE_URL}/register"  # JSONPlaceholder does not have /register
    resp = requests.post(url, json={"email": "nithesh@test.com"}, headers=HEADERS, timeout=10)

    # If Cloudflare-like blocking occurs, skip instead of failing the job
    if resp.status_code == 403:
        pytest.skip("Target API returned 403 Forbidden (likely blocking scripted clients).")

    assert resp.status_code in (404, 405), (
        f"Expected 404/405 for a non-existent endpoint, got {resp.status_code}"
    )
