import allure

from helpers.urls import PageUrls
from locators.order_feed_locators import OrderFeedLocators

from pages.base_page import BasePage

class OrderFeed(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие страницы "Лента заказов"')
    def open_feed_page(self):
        self.open_page(PageUrls.LOGIN_PAGE)


    @allure.step('Нажать на заказ')
    def click_on_order(self):
        self.scroll_and_click(OrderFeedLocators.ORDER_LINK)

    @allure.step("Ожидание появления модального окна с деталями заказа")
    def wait_for_order_details_modal(self, timeout=10):
        return self.wait_for_element(OrderFeedLocators.ORDER_DETAILS_MODAL, timeout)

    @allure.step("Проверка видимости окна с инфо о заказе")
    def is_order_window_visible(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_DETAILS_MODAL)

    @allure.step("Проверка наличия заказа по номеру на странице")
    def check_is_order_in_history(self, order_number, timeout=10):
        locator = OrderFeedLocators.ORDER_NUMBER_TEMPLATE
        locator_with_number =  (locator[0], locator[1].format(order_id=order_number))
        self.wait_for_element(locator_with_number)
        return self.is_element_visible(locator_with_number)

    @allure.step("Получение значения счётчика 'Выполнено за всё время'")
    def get_total_done_counter(self):
        self.wait_for_element(OrderFeedLocators.TOTAL_DONE_COUNTER)
        return self.get_text_on_element(OrderFeedLocators.TOTAL_DONE_COUNTER)

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_total_done_today_counter(self):
        self.wait_for_element(OrderFeedLocators.TOTAL_DONE_TODAY_COUNTER)
        return self.get_text_on_element(OrderFeedLocators.TOTAL_DONE_TODAY_COUNTER)

    @allure.step("Получить список номеров заказов в разделе 'В работе'")
    def get_orders_in_progress(self):
        return self.get_text_on_element(OrderFeedLocators.ORDER_IN_WORK_NUMBER)