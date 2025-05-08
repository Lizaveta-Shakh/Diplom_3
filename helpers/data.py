import random
import allure
import uuid

from faker import Faker

fake = Faker('en_US')

@allure.step('Генерация имя и фамилии')
def generate_random_name():
    random_name = fake.user_name()
    return random_name

@allure.step('Генерация пароля из цифр, макс длина 6')
def generate_random_password(length=6):
    min_value = 10**(length - 1)
    max_value = 10**length - 1
    random_number = random.randint(min_value, max_value)
    return str(random_number)

@allure.step('Генерация имейл')
def generate_random_email():
    unique_part = uuid.uuid4().hex[:8]
    random_email = f"testuser_{unique_part}@ya.com"
    return random_email

@allure.step('Генерация тестовых данных для регистрации юзера')
def create_user_data():
    return {
        "name": generate_random_name(),
        "email": generate_random_email(),
        "password": generate_random_password()
    }


class TextData:
    MODAL_ING_WINDOW_TEXT = 'Детали ингредиента'