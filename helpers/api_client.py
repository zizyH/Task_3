import requests
from config.api_config import REGISTER_ENDPOINT, LOGIN_ENDPOINT, USER_ENDPOINT
from helpers.user_generator import generate_email, generate_password, generate_name

class ApiClient:
    @staticmethod
    def register_user():
        payload = {
            "email": generate_email(),
            "password": generate_password(),
            "name": generate_name()
        }
        response = requests.post(REGISTER_ENDPOINT, json=payload)
        response.raise_for_status()
        data = response.json()
        return {
            "email": payload["email"],
            "password": payload["password"],
            "name": payload["name"],
            "access_token": data["accessToken"],
            "refresh_token": data["refreshToken"]
        }

    @staticmethod
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        response = requests.delete(USER_ENDPOINT, headers=headers)
        return response.status_code