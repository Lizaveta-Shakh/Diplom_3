import allure

from helpers.urls import PageUrls
from locators.personal_account_page_locators import ProfilePageLocators
from pages.base_page import BasePage

class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть личный кабинет')
    def open_account_page(self):
        self.open_page(PageUrls.PERSONAL_ACCOUNT_PAGE)

    @allure.step('Нажать на кнопку "Выход"')
    def click_the_button_exit(self):
        self.scroll_and_click(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Нажать на ссылку "Личный кабинет"')
    def click_the_button_order_history(self):
        self.scroll_and_click(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Проверка, отображается ли заказ по номеру")
    def is_order_in_history(self, order_number):
        locator = ProfilePageLocators.ORDER_NUMBER_ITEM(order_number)
        return self.is_element_visible(locator)

