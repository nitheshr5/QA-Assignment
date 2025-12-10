from locust import HttpUser, task, between

class ReqresUser(HttpUser):
    """
    Simple Locust user for load testing the Reqres API.

    We intentionally keep the load very small to stay within
    the assignment limit of ~100 calls per day.
    """

    # Each simulated user will wait between 1 and 3 seconds between tasks
    wait_time = between(1, 3)

    def on_start(self):
        """
        Called when a simulated user starts.
        We set browser-like headers once per user.
        """
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
        Main scenario:
        - Call GET /api/users?page=2
        - This mirrors the functional test 'test_get_users_page_2_returns_non_empty_list'
        """
        response = self.client.get(
            "/api/users",
            params={"page": 2},
            name="GET /api/users?page=2",
            timeout=10,
        )

        # Optional basic logging – Locust records stats regardless
        if response.status_code != 200:
            print(f"Unexpected status code: {response.status_code}")
