import requests
import json


class Request_to_Django:
    def __init__(self, endpoint) -> None:
        self.endpoint = endpoint
        self.headers = {
            "Content-Type": "application/json",
        }

    def post_request(self, data):
        datas = json.dumps(data)
        request = requests.post(url=self.endpoint, data=datas, headers=self.headers)
        if request.status_code == 201:
            return False
        else:
            return request

    def get_request(self):
        request = requests.get(url=self.endpoint, headers=self.headers)
        if request.status_code == 200:
            return request
        else:
            return False

    def put_request(self, data):
        datas = json.dumps(data)
        request = requests.put(url=self.endpoint, data=datas, headers=self.headers)
        if request.status_code == 200:
            return request
        else:
            return False

    def delete_request(self):
        request = requests.delete(url=self.endpoint, headers=self.headers)
        if request.status_code == 200:
            return request
        else:
            return False
