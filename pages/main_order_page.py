import allure

from helpers.urls import  PageUrls
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание загрузки главной страницы')
    def open_main_page(self):
        self.open_page(PageUrls.MAIN_PAGE)

    @allure.step('Ожидание кликабельности кнопки "Личный кабинет"')
    def wait_personal_account_link_clickable(self):
        return self.wait_for_element_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK, timeout=15)

    @allure.step('Клик по кнопке "Личный кабинет" с защитой от модалки')
    def scroll_and_click_personal_account_link(self):
        self.scroll_and_click(MainPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step('Клик по гиперссылке "Конструктор" с защитой от модалки')
    def scroll_and_click_constructor_link(self):
        self.scroll_and_click(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Клик по иегредиенту с защитой от модалки "Соус Spicy-X"')
    def scroll_and_click_ingredient(self):
        self.scroll_and_click(MainPageLocators.SPICY_X_INGREDIENT)

    @allure.step('Ожидание появления окна ингредиента с заголовком "Детали ингредиента"')
    def wait_for_ingredient_modal(self, timeout=10):
        self.wait_for_element(MainPageLocators.INGR_DETAILS_WINDOW_HEADER, timeout)

    @allure.step("Получить текст заголовка модального окна с ингредиентом")
    def get_ingredient_modal_header_text(self):
        return self.wait_for_element(MainPageLocators.INGR_DETAILS_WINDOW_HEADER).text

    @allure.step('Клик по гиперссылке "Лента заказов"')
    def scroll_and_click_order_feed(self):
        self.scroll_and_click(MainPageLocators.LINK_ORDER_FEED)

    @allure.step('Клик по кнопке "Заказать"')
    def scroll_and_click_order_button(self):
        self.scroll_and_click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Клик по крестику закрытия модального окна ингредиента")
    def click_close_ingredient_modal(self):
        self.wait_modal_overlay_disappears(timeout=3)
        self.wait_for_element_clickable(MainPageLocators.CROSS_ICON_FOR_ING_MODAL, timeout=10).click()

    @allure.step("Ожидание, пока модалка с деталями ингредиента станет невидимой")
    def wait_for_ingredient_modal_to_close(self, timeout=10):
        self.wait_for_invisibility(MainPageLocators.INGR_DETAILS_WINDOW_HEADER, timeout)

    @allure.step("Проверка, что окно с деталями ингредиента скрыто")
    def is_ingredient_modal_closed(self):
        return self.is_element_invisible(MainPageLocators.INGR_DETAILS_WINDOW_HEADER)

    @allure.step("Получение значения счётчика ингредиента по имени")
    def get_ingredient_counter_by_name(self, ingredient_name):
        try:
            counter_locator = (
                By.XPATH,
                f'//p[text()="{ingredient_name}"]/ancestor::a//p[contains(@class, "counter_counter__num__3nue1")]'
            )
            return int(self.driver.find_element(*counter_locator).text)
        except:
            return 0


    @allure.step("Перетащить ингредиент по имени в зону конструктора через seletools")
    def drag_ingredient_to_constructor_seletools(self, ingredient_name):
        ingredient = self.wait_for_element(MainPageLocators.ingredient_by_name(ingredient_name))
        self.scroll_to_element(MainPageLocators.ingredient_by_name(ingredient_name))
        target = self.wait_for_element(MainPageLocators.BURGER_CONSTRUCTOR_ZONE)
        self.drag_and_drop_with_seletools(ingredient, target)


    @allure.step("Ожидание отображения корректного номера заказа")
    def wait_for_final_order_number(self):
        return self.wait_for_correct_order_number(MainPageLocators.ORDER_NUMBER_TITLE)

    @allure.step("Создать заказ из ингредиента и булки и получить номер ")
    def create_order_and_return_number(self, ingredient: str, bun: str) -> str:
        self.drag_ingredient_to_constructor_seletools(ingredient)
        self.drag_ingredient_to_constructor_seletools(bun)
        self.scroll_and_click_order_button()
        order_number_element = self.wait_for_final_order_number()
        order_number = order_number_element.text.strip()
        self.click_close_ingredient_modal()
        self.wait_for_ingredient_modal_to_close()
        return order_number



