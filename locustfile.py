# locustfile.py

from locust import HttpUser, task, between

class ReqresUser(HttpUser):
    """
    Simple load profile:
    - Hits GET /api/users?page=1 repeatedly
    - wait_time ensures we stay well below 100 calls per day
      when run with small user count & duration.
    """
    wait_time = between(3, 5)  # seconds

    @task
    def list_users(self):
        self.client.get("/api/users", params={"page": 1})
