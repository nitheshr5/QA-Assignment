"""
Locust load test for JSONPlaceholder API.
Safe alternative to Reqres for performance testing.

Run:
    locust -f locustfile_jsonplaceholder.py --host=https://jsonplaceholder.typicode.com

Notes:
- JSONPlaceholder is a public fake API — responses are static.
- Keep load small (1–5 users) to avoid unnecessary stress on public services.
"""

from locust import HttpUser, task, between

class JsonPlaceholderUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        # Set headers to mimic a real browser
        self.client.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                ),
                "Accept": "application/json",
            }
        )

    @task(3)
    def list_users(self):
        """GET /users – weighted more heavily (3x)."""
        self.client.get("/users", name="GET /users", timeout=10)

    @task(2)
    def get_single_user(self):
        """GET /users/1."""
        self.client.get("/users/1", name="GET /users/1", timeout=10)

    @task(1)
    def create_post(self):
        """POST /posts – create a fake post."""
        payload = {
            "title": "locust-test-title",
            "body": "load testing using locust",
            "userId": 999
        }
        self.client.post("/posts", json=payload, name="POST /posts", timeout=10)
