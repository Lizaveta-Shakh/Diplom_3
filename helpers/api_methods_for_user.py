import requests
import allure
from helpers.urls import BaseUrls

BASE_URL = BaseUrls.BASE_URL


class ApiMethods:
    @staticmethod
    @allure.step('Регистрация нового пользователя')
    def register_new_user(name, email, password):
        url = f"{BASE_URL}/api/auth/register"
        data = {
            'email': email,
            'password': password,
            'name': name
        }
        response = requests.post(url, json=data)
        return response


    @staticmethod
    @allure.step('Удаление существующего юзера')
    def delete_user(access_token):
        url = f"{BASE_URL}/api/auth/user"
        headers = {"Authorization": f"Bearer {access_token}"}
        delete_response = requests.delete(url, headers=headers)
        return delete_response


    @staticmethod
    @allure.step('Авторизация пользователя')
    def login(login_data):
        url = f"{BASE_URL}/api/auth/login"
        login_response = requests.post(url, json = login_data)
        return login_response

