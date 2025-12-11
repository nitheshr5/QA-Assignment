# tests/test_reqres_api.py

"""
Reqres API functional tests.

Notes:
- Reqres (https://reqres.in) is used for the official assignment tests.
- Some environments (or Cloudflare rules) may block scripted requests; in that case
  consider running the alternate test suite (test_alt_api.py) that targets
  jsonplaceholder.typicode.com instead.
"""

import requests
import pytest

BASE_URL = "https://reqres.in/api"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

def _maybe_json(resp):
    """Return parsed JSON or None if body is empty / invalid JSON."""
    try:
        return resp.json()
    except ValueError:
        return None

@pytest.mark.api
@pytest.mark.positive
@pytest.mark.smoke
def test_get_users_page_2_returns_non_empty_list():
    """
    Smoke test:
    - GET /users?page=2 should return 200
    - The 'page' field should match requested page
    - 'data' must be a non-empty list
    """
    response = requests.get(
        f"{BASE_URL}/users",
        params={"page": 2},
        headers=HEADERS,
        timeout=10,
    )

    # If blocked, the remote might return HTML/403; let pytest decide if that's a failure
    assert response.status_code == 200, (
        f"Expected 200 OK for list users; got {response.status_code}. "
        "If the host blocks scripted clients (Cloudflare), consider using the alternate tests."
    )

    body = _maybe_json(response)
    assert isinstance(body, dict), "Expected JSON object at top level"
    assert body.get("page") == 2, "Page number should match requested page"
    assert "data" in body, "'data' key should be present in response"
    assert isinstance(body["data"], list), "'data' should be a list"
    assert len(body["data"]) > 0, "User list should not be empty"

@pytest.mark.api
@pytest.mark.positive
def test_get_existing_user_returns_correct_user():
    """
    GET /users/2 -> expect 200 and data containing user with id 2 and an email
    """
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS, timeout=10)

    assert response.status_code == 200, f"Expected 200 OK for existing user, got {response.status_code}"

    body = _maybe_json(response)
    user = body.get("data") if body else None
    assert user is not None, "'data' for single user should not be None"
    assert user.get("id") == 2, f"Expected user id 2, got {user.get('id')}"
    assert "email" in user, "User should contain an 'email' field"

@pytest.mark.api
@pytest.mark.negative
def test_get_non_existing_user_returns_404():
    """
    GET /users/23 (non-existing) -> should return 404 and an empty/minimal body.
    """
    response = requests.get(f"{BASE_URL}/users/23", headers=HEADERS, timeout=10)
    assert response.status_code == 404, f"Expected 404 for non-existing user; got {response.status_code}"

    # Reqres usually returns empty JSON {} on not-found
    body = _maybe_json(response)
    assert body in (None, {}), f"Expected empty/minimal body for not-found; got: {body}"

@pytest.mark.api
@pytest.mark.positive
@pytest.mark.negative
def test_register_user_success_and_missing_password_error():
    """
    Combined test covering:
    1) Successful registration with valid email+password -> 200 + id + token
    2) Error case for missing password -> 400 + error message
    """
    # 1) Successful registration
    valid_payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
    success_resp = requests.post(
        f"{BASE_URL}/register",
        json=valid_payload,
        headers=HEADERS,
        timeout=10,
    )

    assert success_resp.status_code == 200, f"Expected 200 for valid registration; got {success_resp.status_code}"
    success_body = _maybe_json(success_resp)
    assert isinstance(success_body, dict), "Expected JSON body on successful register"
    assert "id" in success_body, "Successful register should return 'id'"
    assert "token" in success_body, "Successful register should return 'token'"

    # 2) Missing password -> error expected
    missing_pwd_payload = {"email": "sydney@fife"}
    error_resp = requests.post(
        f"{BASE_URL}/register",
        json=missing_pwd_payload,
        headers=HEADERS,
        timeout=10,
    )

    assert error_resp.status_code == 400, f"Expected 400 when password is missing; got {error_resp.status_code}"
    error_body = _maybe_json(error_resp)
    assert error_body and error_body.get("error") == "Missing password", (
        f"Expected error message 'Missing password', got: {error_body}"
    )

@pytest.mark.api
@pytest.mark.positive
def test_create_user_returns_created_resource_metadata():
    """
    POST /users -> expect 201 Created and fields echoed back plus id and createdAt
    """
    payload = {"name": "qa-automation-candidate", "job": "qa-intern"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS, timeout=10)

    assert response.status_code == 201, f"Expected 201 for user creation; got {response.status_code}"
    body = _maybe_json(response)
    assert body.get("name") == payload["name"], "Response should echo 'name'"
    assert body.get("job") == payload["job"], "Response should echo 'job'"
    assert "id" in body, "Response should contain generated 'id'"
    assert "createdAt" in body, "Response should contain 'createdAt' timestamp"

