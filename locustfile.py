import random
import string
from locust import HttpUser, constant, task, between

class MahasiswaTest(HttpUser):
    wait_time = constant(1)

    #perf
    @task
    def get(self):
        self.client.get('/mahasiswa/123456789')

    # #load
    # @task
    # def put(self):
    #     self.client.put('/mahasiswa/123456789', json={"nama":"test", "alamat":"testalamat", "npm":"12345678905"})

    #stress
    # @task
    # def create(self):
    #     npm = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    #     self.client.post('/mahasiswa', json={"nama":"test", "alamat":"testalamat", "npm":npm})

