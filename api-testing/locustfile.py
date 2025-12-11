
"""
Simple Locust load test for the Reqres scenario.

Usage:
    locust -f locustfile.py --host=https://reqres.in

Notes:
- Keep the simulated load very small to respect the assignment constraint
  of a maximum ~100 API calls within the day.
- You can configure number of users and spawn rate from the Locust web UI.
"""

from locust import HttpUser, task, between

class ReqresUser(HttpUser):
    # Each simulated user waits between 1 and 3 seconds between tasks
    wait_time = between(1, 3)

    def on_start(self):
        # Set browser-like headers on the session to reduce blocking likelihood
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

    @task
    def list_users_page_2(self):
        """
        Simple scenario: GET /api/users?page=2
        This mirrors the functional test 'test_get_users_page_2_returns_non_empty_list'.
        """
        response = self.client.get(
            "/api/users",
            params={"page": 2},
            name="GET /api/users?page=2",
            timeout=10,
        )
        # Locust collects stats automatically. Print only for optional debug.
        if response.status_code != 200:
            print(f"[locust] Unexpected status code: {response.status_code}")
