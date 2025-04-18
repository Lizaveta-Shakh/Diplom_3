import allure

from helpers.urls import PageUrls
from locators.personal_account_page_locators import ProfilePageLocators
from locators.common_locators import CommonLocators

from pages.base_page import BasePage

class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def modal_overlay_disappears(self, timeout: int = 15):
        self.wait_modal_overlay_disappears(CommonLocators.MODAL_OVERLAY, timeout)

    @allure.step('Открыть личный кабинет')
    def open_account_page(self):
        self.open_page(PageUrls.PERSONAL_ACCOUNT_PAGE)

    @allure.step('Нажать на кнопку "Выход"')
    def click_the_button_exit(self):
        self.scroll_and_click(ProfilePageLocators.LOGOUT_BUTTON,
            overlay_locator=CommonLocators.MODAL_OVERLAY
        )
    @allure.step('Нажать на кнопку "Выход" js')
    def click_the_button_exit_js(self):
        self.scroll_to_element(ProfilePageLocators.LOGOUT_BUTTON)
        self.javascript_click(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Нажать на ссылку "Личный кабинет"')
    def click_the_button_order_history(self):
        self.scroll_and_click(ProfilePageLocators.ORDER_HISTORY_LINK,
            overlay_locator=CommonLocators.MODAL_OVERLAY
        )
    @allure.step('Нажать на ссылку "Личный кабинет"')
    def click_the_button_order_history_js(self):
        self.scroll_to_element(ProfilePageLocators.ORDER_HISTORY_LINK)
        self.javascript_click(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Сравнение, что URL содержит ")
    def is_account_page(self):
        return self.current_url_contains(PageUrls.PERSONAL_ACCOUNT_PAGE)

    @allure.step("Проверка, что текущий url - история заказов")
    def is_current_url_order_history(self):
        return self.is_current_url(PageUrls.ORDER_HISTORY_ACCOUNT)

    @allure.step("Проверка, отображается ли заказ по номеру")
    def is_order_in_history(self, order_number):
        locator = ProfilePageLocators.ORDER_NUMBER_ITEM(order_number)
        return self.is_element_visible(locator)

