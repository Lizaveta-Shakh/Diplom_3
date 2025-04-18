import allure

from pages.login_page import LoginPage
from pages.forgot_password_page import RestorePassword

from helpers.data import *


class TestPasswordRestoration:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_restore_password_redirect_restore_password_page(self, driver):
        login_page = LoginPage(driver)
        forgot_page = RestorePassword(driver)
        with allure.step("Открытие страницы логина"):
            login_page.open_login_page()
        with allure.step("Переход по ссылке «Восстановить пароль»"):
            login_page.click_the_button_restore_password_js()

        with allure.step("Ожидание страницы восстановления пароля"):
            forgot_page.wait_for_password_restore_page()

        with allure.step("Проверка, что текущий URL — страница восстановления пароля"):
            assert forgot_page.is_current_url_restore_password_page()

    @allure.title('Проверка перехода на страницу сброса пароля после ввода почты и клика по кнопке «Восстановить»')
    def test_click_restore_password_redirect_reset_password_page(self, driver):
        forgot_page = RestorePassword(driver)

        with allure.step("Открытие страницы восстановления пароля"):
            forgot_page.open_restore_page()
        with allure.step("Ввод email и клик по кнопке 'Восстановить'"):
            forgot_page.enter_email(generate_random_email())
            forgot_page.click_restore_button_js()
        with allure.step("Ожидание загрузки страницы сброса пароля"):
            forgot_page.wait_for_password_reset_page()

        with allure.step("Проверка, что текущий URL — страница сброса пароля"):
            assert forgot_page.is_current_url_reset_password_page()

    @allure.title('Проверка: клик по кнопке "показать/скрыть пароль" делает поле активным на стр. сброса пароля')
    def test_click_on_eye_icon_highlights_password_field(self, driver):
        forgot_password_page = RestorePassword(driver)

        with allure.step("Открытие страницы восстановления пароля"):
            forgot_password_page.open_restore_page()
        with allure.step("Ввод email и переход на страницу сброса пароля"):
            forgot_password_page.enter_email(generate_random_email())
            forgot_password_page.click_restore_button_js()
            forgot_password_page.wait_for_password_reset_page()
        with allure.step("Клик по иконке глаза"):
            forgot_password_page.click_eye_icon()

        with allure.step("Проверка, что поле пароля стало активным (подсвечено)"):
            assert forgot_password_page.is_password_field_active()
