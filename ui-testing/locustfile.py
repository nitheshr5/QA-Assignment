"""
Simple Locust load test for key public pages on iamdave.ai.

Keep simulated load small for the assignment (e.g., <100 requests/day).
"""
from locust import HttpUser, task, between

class DaveAIUser(HttpUser):
    host = "https://www.iamdave.ai"
    wait_time = between(1, 3)

    @task
    def load_homepage(self):
        self.client.get("/", name="Homepage")

    @task
    def load_solutions(self):
        self.client.get("/solutions/", name="Solutions Page")

    @task
    def load_contact(self):
        self.client.get("/contact-us/", name="Contact Page")
