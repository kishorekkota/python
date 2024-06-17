from locust import HttpUser, task, between, TaskSet

class UserBehavior(TaskSet):
    @task
    def get_items(self):
        self.client.get("/items")
    @task
    def get_items_async(self):
        self.client.get("/items_async")
        


class WebSiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)