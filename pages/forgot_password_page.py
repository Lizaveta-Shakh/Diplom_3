import allure

from helpers.urls import PageUrls
from locators.forgot_password_page_locators import ForgotPasswordLocators, ResetPasswordLocators
from locators.common_locators import CommonLocators

from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage

class RestorePassword(BasePage):

    @allure.step("Открыть страницу восстановления пароля")
    def open_restore_page(self):
        self.open_page(PageUrls.FORGOT_PASSWORD_PAGE)

    def modal_overlay_disappears(self, timeout: int = 20):
        self.wait_modal_overlay_disappears(CommonLocators.MODAL_OVERLAY, timeout)

    @allure.step("Ввести email для восстановления")
    def enter_email(self, email):
        self.send_keys_to_input(ForgotPasswordLocators.EMAIL_INPUT_FIELD, email)


    @allure.step("Нажать на кнопку 'Восстановить' (JS)")
    def click_restore_button_js(self):
        self.scroll_to_element(ForgotPasswordLocators.RESTORE_BUTTON)
        self.javascript_click(ForgotPasswordLocators.RESTORE_BUTTON)

    @allure.step("Дождаться появления страницы восстановления пароля")
    def wait_for_password_restore_page(self, timeout=20):
        self.wait_for_element(ForgotPasswordLocators.RESTORE_BUTTON, timeout)

    @allure.step("Дождаться появления страницы сброса пароля")
    def wait_for_password_reset_page(self, timeout=20):
        self.wait_for_element(ResetPasswordLocators.PASSWORD_INPUT_FIELD, timeout)


    @allure.step("Кликнуть на иконку глаза (показать/скрыть пароль)")
    def click_eye_icon(self):
        self.scroll_and_click(ResetPasswordLocators.HIDE_EYE_ICON,
            overlay_locator=CommonLocators.MODAL_OVERLAY
        )

    @allure.step("Проверка, что поле пароля стало активным (подсвечено)")
    def is_password_field_active(self):
        try:
            self.driver.find_element(*ResetPasswordLocators.ACTIVE_PASSWORD_FIELD)
            return True
        except NoSuchElementException:
            return False

    @allure.step("Проверка, что текущий url - восстановления пароля")
    def is_current_url_restore_password_page(self):
        return self.is_current_url(PageUrls.FORGOT_PASSWORD_PAGE)

    @allure.step("Проверка, что текущий url - сброса пароля")
    def is_current_url_reset_password_page(self):
        return self.is_current_url(PageUrls.RESET_PASSWORD_PAGE)