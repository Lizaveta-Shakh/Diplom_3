import allure
from pages.main_order_page import MainPage
from helpers.urls import PageUrls
from helpers.data import TextData


class TestMainFunctionality:
    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_click_on_constructor_navigates_to_constructor_page(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        with allure.step("Перейти в раздел 'Лента заказов'"): #Так как сразу открывается стр с конструктором
            main_page.scroll_and_click_order_feed()
        with allure.step("Кликнуть по ссылке 'Конструктор'"):
            main_page.scroll_and_click_constructor_link()

        with allure.step("Проверить, что произошёл переход на главную страницу"):
            assert driver.current_url == PageUrls.MAIN_PAGE

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    def test_click_on_order_feed_navigates_to_order_feed_page(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        with allure.step("Кликнуть по ссылке 'Лента заказов'"):
            main_page.scroll_and_click_order_feed()

        with allure.step("Проверить, что произошёл переход на страницу ленты заказов"):
            assert driver.current_url == PageUrls.FEED_PAGE


    @allure.title('Проверка появления всплывающего окна с деталями ингредиента после клика по ингредиенту')
    def test_click_on_ingredient_opens_ingredient_info_window(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        with allure.step("Кликнуть по ингредиенту и дождаться модального окна"):
            main_page.scroll_and_click_ingredient()
            main_page.wait_for_ingredient_modal()

        with allure.step("Проверить, что заголовок модального окна соответствует ожидаемому"):
            modal_title = main_page.get_ingredient_modal_header_text()
            assert TextData.MODAL_ING_WINDOW_TEXT in modal_title


    @allure.title('Проверка закрытия окна "Детали ингредиента" нажатием на крестик')
    def test_close_ingredient_details_modal_by_cross_icon(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        with allure.step("Открыть окно с деталями ингредиента"):
            main_page.scroll_and_click_ingredient()
            main_page.wait_for_ingredient_modal()
        with allure.step("Закрыть модалку по крестику"):
            main_page.click_close_ingredient_modal()
            main_page.wait_for_ingredient_modal_to_close()

        with allure.step("Проверить, что модалка закрылась"):
            assert main_page.is_ingredient_modal_closed()


    @allure.title('Проверка увеличения счётчика ингредиента при добавлении в заказ') #Добавление в заказ реализовано через drag-and-drop
    def test_ingredient_counter_increases_on_drag_to_constructor(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
            ingredient = "Соус Spicy-X"
        with allure.step(f"Получить значение счётчика ингредиента до добавления"):
            count_before = main_page.get_ingredient_counter_by_name(ingredient)
        with allure.step(f"Добавить ингредиент в конструктор через drag-and-drop"):
            main_page.drag_ingredient_to_constructor_seletools(ingredient)
        with allure.step(f"Получить значение счётчика ингредиента после добавления"):
            count_after = main_page.get_ingredient_counter_by_name(ingredient)

        with allure.step("Проверка, что счётчик увеличился на 1"):
            assert count_after == count_before + 1


    @allure.title('Проверка создания заказа залогиненным пользователем')
    def test_create_order_auth_user_returns_order_number(self, driver,user,authorized_user):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
            ingredient = "Соус Spicy-X"
            bun_name = "Краторная булка N-200i"
        with allure.step(f"Добавить ингредиенты в конструктор через drag-and-drop"):
            main_page.drag_ingredient_to_constructor_seletools(ingredient)
            main_page.drag_ingredient_to_constructor_seletools(bun_name)
        with allure.step("Нажать на кнопку 'Оформить заказ'"):
            main_page.scroll_and_click_order_button()
            order_number_element = main_page.wait_for_final_order_number()
            order_number = order_number_element.text


        with allure.step(f"Проверка, что номер заказа является числом"):
            assert order_number.isdigit()