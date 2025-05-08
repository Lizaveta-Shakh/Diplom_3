import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


from helpers.data import *
from helpers.api_methods_for_user import  ApiMethods

from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    else:
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    yield driver

    driver.quit()


@pytest.fixture (scope="function")
def user():
    data = create_user_data()

    response = ApiMethods.register_new_user(data['name'], data['email'], data['password'])
    assert response.status_code == 200

    login_response = ApiMethods.login({
        'email': data['email'],
        'password': data['password']
    })
    assert login_response.status_code == 200
    tokens = login_response.json()

    yield {
        "tokens": tokens,
        "user_data": data
    }

    ApiMethods.delete_user(tokens['accessToken'])

@pytest.fixture(scope="function")
def authorized_user(driver, user):
    driver.get("https://stellarburgers.nomoreparties.site")
    access_token = user['tokens']['accessToken']
    refresh_token = user['tokens']['refreshToken']


    driver.execute_script(f"window.localStorage.setItem('accessToken', '{access_token}');")
    driver.execute_script(f"window.localStorage.setItem('refreshToken', '{refresh_token}');")

    driver.refresh()
    return user