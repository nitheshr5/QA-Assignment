# API Test Cases – 

## API Under Test
- **Base URL:** https://jsonplaceholder.typicode.com
- **Tool Used for Automation:** Python (requests library)

---

## Api test case 1 – Verify GET Users API

### Objective
To verify that the API returns a list of users successfully.

### Endpoint
```
GET /users
```

### Request Headers
- Content-Type: application/json

### Test Steps
1. Send a GET request to `/users`
2. Capture the response status code
3. Validate the response body

### Expected Result
- Status code should be **200**
- Response body should be a **non-empty list**
- Each user object should contain an `id`

---

## Api test case 2 – Verify GET User by ID

### Objective
To verify that a specific user can be retrieved using a valid user ID.

### Endpoint
```
GET /users/1
```

### Test Steps
1. Send a GET request to `/users/1`
2. Capture the response
3. Validate the user details in the response

### Expected Result
- Status code should be **200**
- Response body should contain user with `id = 1`

---

## Api test case 3 – Verify Create User API

### Objective
To verify that a new user can be created successfully using POST request.

### Endpoint
```
POST /users
```

### Request Body
```json
{
  "name": "nithesh",
  "job": "qa-intern"
}
```

### Test Steps
1. Send POST request with valid request body
2. Capture the response status code
3. Validate the response body

### Expected Result
- Status code should be **201** or **200**
- Response should contain generated user id
- Response should echo the sent data

---

## Api test case 4– Verify Invalid Endpoint Handling

### Objective
To verify API behavior when an invalid endpoint is accessed.

### Endpoint
```
POST /invalid-endpoint
```

### Test Steps
1. Send POST request to an invalid endpoint
2. Capture the response status code

### Expected Result
- Status code should be **404** or **405**
- API should return an error response

---

## Api test case 5 – Verify Non-Existing User

### Objective
To verify API behavior when a non-existing user ID is requested.

### Endpoint
```
GET /users/9999
```

### Test Steps
1. Send GET request to `/users/9999`
2. Capture the response status code
3. Validate response body

### Expected Result
- Status code should be **404** or **200 with empty response**
- Response should not contain valid user data

---

## Notes
- These test cases are automated in `simple_api_test.py`
- JSONPlaceholder is used as a public mock API for testing
- Tests cover positive and negative scenarios
- Designed for easy understanding and interview explanation