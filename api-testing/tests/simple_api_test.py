import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

print("Starting Simple API Tests\n")

# api test case 01: Get all users 
print("Api test case 1: verify GET Users API")

response = requests.get(f"{BASE_URL}/users")
assert response.status_code == 200, "Expected statuscode 200"

users = response.json()
assert isinstance(users, list), "response should belist"
assert len(users) > 0, "User list should not be empty"

print("Pass, Users list retrieved successfully\n")

# Api test case 2: Get single user 
print("Api test case 2: Verify GET user by ID")

response = requests.get(f"{BASE_URL}/users/1")
assert response.status_code == 200, "Expected status code 200"

user = response.json()
assert user.get("id") == 1, "User ID should be 1"

print("pass: Single user retrieved successfully\n")

# Api test case 3: Create user 
print("Api test case 3: Verify CREATE user Api")

payload = {
    "name": "nithesh",
    "job": "qa-intern"
}

response = requests.post(f"{BASE_URL}/users", json=payload)
assert response.status_code in (201, 200), "Expected status code 201 or 200"

created_user = response.json()
assert "id" in created_user, "Response should contain user ID"

print("Pass: User created successfully\n")

#  Api test case 4: Invalid endpoint 
print("Api test case 4: Verify Invalid Endpoint")

response = requests.post(f"{BASE_URL}/invalid-endpoint")
assert response.status_code in (404, 405), "Expected 404"

print("Pass: Invalid endpoint handled correctly\n")

print("All test cases completed successfully")
