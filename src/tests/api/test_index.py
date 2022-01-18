from locust import FastHttpUser, task, constant


class IndexTestUser(FastHttpUser):
    """
    Test index
    """

    wait_time = constant(1)

    @task
    def request_index(self):
        self.client.get("/index")
