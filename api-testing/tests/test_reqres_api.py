# tests/api/test_reqres_api.py

import requests
import pytest

BASE_URL = "https://reqres.in/api"



HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}


@pytest.mark.api
def test_list_users_success():
    """
    Positive test:
    - GET /users?page=2 returns 200
    - response contains a non-empty 'data' list
    - correct page number
    """
    response = requests.get(f"{BASE_URL}/users", params={"page": 2}, headers=HEADERS)

    assert response.status_code == 200, "Expected 200 OK for list users"
    body = response.json()

    assert body.get("page") == 2, "Page number should match requested page"
    assert "data" in body, "'data' key should be present in response"
    assert isinstance(body["data"], list), "'data' should be a list"
    assert len(body["data"]) > 0, "User list should not be empty"


@pytest.mark.api
def test_get_single_user_success():
    """
    Positive test:
    - GET /users/2 returns 200
    - response contains user with id=2 and an email field
    """
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)

    assert response.status_code == 200, "Expected 200 OK for existing user"
    body = response.json()

    user = body.get("data")
    assert user is not None, "'data' for single user should not be None"
    assert user.get("id") == 2, "User id should be 2"
    assert "email" in user, "User should contain an 'email' field"


@pytest.mark.api
def test_get_user_not_found():
    """
    Negative test:
    - GET /users/23 (non-existing user) should return 404
    - body is empty or minimal
    """
    response = requests.get(f"{BASE_URL}/users/23", headers=HEADERS)

    assert response.status_code == 404, "Expected 404 for non-existing user"
    # For Reqres this is usually an empty body {}
    try:
        body = response.json()
    except ValueError:
        body = None

    assert body in (None, {},), "Non-existing user should not return a full payload"


@pytest.mark.api
def test_register_success_and_missing_password():
    """
    Combo test to show positive + error handling on /register.
    1) Valid email+password -> 200 + token
    2) Missing password -> 400 + 'Missing password' error
    """
    # 1) Successful registration
    # Known valid user for Reqres registration. :contentReference[oaicite:1]{index=1}
    valid_payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    success_resp = requests.post(f"{BASE_URL}/register", json=valid_payload, headers=HEADERS)
    assert success_resp.status_code == 200, "Expected 200 for valid registration"
    success_body = success_resp.json()

    assert "id" in success_body, "Successful register should return 'id'"
    assert "token" in success_body, "Successful register should return 'token'"

    # 2) Missing password error case
    missing_pwd_payload = {
        "email": "sydney@fife"
    }
    error_resp = requests.post(f"{BASE_URL}/register", json=missing_pwd_payload, headers=HEADERS)
    # Reqres returns 400 + { "error": "Missing password" } for this. :contentReference[oaicite:2]{index=2}
    assert error_resp.status_code == 400, "Expected 400 when password is missing"
    error_body = error_resp.json()

    assert error_body.get("error") == "Missing password", "Error message should be 'Missing password'"


@pytest.mark.api
def test_create_user_success():
    """
    Positive test for POST /users:
    - status code 201
    - response echoes name/job and returns generated id + createdAt
    """
    payload = {
        "name": "qa-automation-candidate",
        "job": "qa-intern"
    }

    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)

    assert response.status_code == 201, "Expected 201 for user creation"
    body = response.json()

    assert body.get("name") == payload["name"], "Response should echo 'name'"
    assert body.get("job") == payload["job"], "Response should echo 'job'"
    assert "id" in body, "Response should contain generated 'id'"
    assert "createdAt" in body, "Response should contain 'createdAt' timestamp"
