import allure

from helpers.urls import PageUrls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открытие страницы логина")
    def open_login_page(self):
        self.open_page(PageUrls.LOGIN_PAGE)


    @allure.step('Нажать на кнопку "Восстановить пароль" (JS)')
    def click_the_button_restore_password_js(self):
        self.scroll_to_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
        self.javascript_click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Ожидание кнопки 'Войти'")
    def wait_for_login_button(self, timeout=20):
        return self.wait_for_element(LoginPageLocators.LOGIN_BUTTON, timeout)

    @allure.step("Проверка, что текущий url - стр логина")
    def is_current_url_login(self):
        return self.is_current_url(PageUrls.LOGIN_PAGE)




