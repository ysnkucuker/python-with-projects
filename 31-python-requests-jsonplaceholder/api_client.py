import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class APIClient:

    def get_posts(self):
        response = requests.get(f"{BASE_URL}/posts")
        return response.json()

    def get_post(self, post_id):
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        return response.json()

    def create_post(self, data):
        response = requests.post(f"{BASE_URL}/posts", json=data)
        return response.json()

    def update_post(self, post_id, data):
        response = requests.put(f"{BASE_URL}/posts/{post_id}", json=data)
        return response.json()

    def patch_post(self, post_id, data):
        response = requests.patch(f"{BASE_URL}/posts/{post_id}", json=data)
        return response.json()

    def delete_post(self, post_id):
        response = requests.delete(f"{BASE_URL}/posts/{post_id}")
        return response.status_code