# api-testing/tests/test_alt_api.py
"""
Alternate API test suite using JSONPlaceholder so you can demonstrate
that the test logic works when the target API is reachable.

Default base URL: https://jsonplaceholder.typicode.com
You can override it by setting the environment variable:
    BASE_API_URL (for example: export BASE_API_URL="https://reqres.in/api")
"""

import os  
import requests
import pytest

# default to JSONPlaceholder which is friendly to scripts
BASE_URL = os.environ.get("BASE_API_URL", "https://jsonplaceholder.typicode.com")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}


def skip_if_forbidden_or_blocked(response):
    """
    Helper used in case a target API blocks scripted clients (403).
    Skips the test with a message to keep CI/reporting clean.
    """
    if response.status_code == 403:
        pytest.skip("Target API returned 403 Forbidden (likely blocking scripted clients).")


@pytest.mark.api
@pytest.mark.positive
@pytest.mark.smoke
def test_list_users_returns_non_empty_list():
    """
    Maps to original 'list users' test.
    JSONPlaceholder: GET /users -> returns list of users.
    """
    url = f"{BASE_URL}/users"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    skip_if_forbidden_or_blocked(resp)

    assert resp.status_code == 200, f"Expected 200 OK from {url}, got {resp.status_code}"
    body = resp.json()
    assert isinstance(body, list), "Expected response body to be a list"
    assert len(body) > 0, "Expected at least one user in response"


@pytest.mark.api
@pytest.mark.positive
def test_get_single_user_returns_expected_user():
    """
    Maps to original 'get single user' test.
    JSONPlaceholder: GET /users/2 -> should return user with id 2.
    """
    url = f"{BASE_URL}/users/2"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    skip_if_forbidden_or_blocked(resp)

    assert resp.status_code == 200, f"Expected 200 OK from {url}, got {resp.status_code}"
    body = resp.json()
    # JSONPlaceholder user object has 'id' field
    assert isinstance(body, dict), "Expected JSON object for single user"
    assert body.get("id") == 2, f"Expected user id 2, got {body.get('id')}"


@pytest.mark.api
@pytest.mark.negative
def test_get_non_existing_user_returns_404_or_empty():
    """
    Negative test: request a very high id that likely doesn't exist.
    Behavior varies across public test APIs:
      - JSONPlaceholder may return {} or 404.
    Accept either:
      - status code 404
      - or status code 200 with empty body / no 'id'
    """
    url = f"{BASE_URL}/users/99999"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    skip_if_forbidden_or_blocked(resp)

    if resp.status_code == 404:
        # expected not-found
        assert True
    else:
        # some public APIs return 200 with empty object; allow that too
        assert resp.status_code == 200, f"Unexpected status {resp.status_code}"
        body = resp.json()
        # body may be {} or empty; ensure it doesn't contain a valid id
        assert not body or not body.get("id"), "Non-existing user should not return an id"


@pytest.mark.api
@pytest.mark.positive
def test_create_post_success():
    """
    We map the 'create user' test to creating a post on JSONPlaceholder:
    POST /posts returns 201 and echoes the sent fields with a generated id.
    """
    url = f"{BASE_URL}/posts"
    payload = {
        "title": "qa-automation-candidate",
        "body": "testing create via jsonplaceholder",
        "userId": 1
    }
    resp = requests.post(url, json=payload, headers=HEADERS, timeout=10)
    skip_if_forbidden_or_blocked(resp)

    assert resp.status_code == 201, f"Expected 201 Created, got {resp.status_code}"
    body = resp.json()
    # JSONPlaceholder returns created object with an 'id'
    assert body.get("title") == payload["title"]
    assert body.get("body") == payload["body"]
    assert "id" in body, "Expected generated id in response"


@pytest.mark.api
@pytest.mark.negative
def test_invalid_endpoint_returns_404():
    """
    Maps to the 'register missing password' negative test by calling an
    endpoint that doesn't exist on JSONPlaceholder and expecting 404.
    """
    url = f"{BASE_URL}/register"  # JSONPlaceholder does not provide /register
    resp = requests.post(url, json={"email": "a@b.com"}, headers=HEADERS, timeout=10)

    # Some hosts might reply with HTML/403; handle gracefully:
    if resp.status_code == 403:
        pytest.skip("Target API returned 403 Forbidden (likely Cloudflare blocking scripted clients).")
    assert resp.status_code in (404, 405), f"Expected 404/405 for a non-existent endpoint, got {resp.status_code}"
