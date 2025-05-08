import allure
from pages.order_feed_page import OrderFeed
from pages.main_order_page import MainPage
from pages.personal_account_page import  PersonalAccountPage

class TestOrderFeed:
    @allure.title('Проверка открытия окна с информацией о заказе при нажатии на заказ')
    def test_click_on_order_opens_order_info_window(self, driver):
        main_page = MainPage(driver)
        feed_page = OrderFeed(driver)

        with allure.step("Ожидание загрузки главной страницы и переход в 'Ленту заказов'"):
            main_page.open_main_page()
            main_page.wait_order_link_clickable()
            main_page.scroll_and_click_order_feed_js()

        with allure.step("Клик на заказ в ленте заказов"):
            feed_page.click_on_order()

        with allure.step("Ожидание открытия окна с деталями заказа"):
            feed_page.wait_for_order_details_modal()


        assert feed_page.is_order_window_visible()


    @allure.title('Проверка отображения заказов пользователя из "Истории заказов" на стр "Лента заказов"')
    def test_orders_from_history_displayed_on_feed_page(self, driver, user, authorized_user):
        main_page = MainPage(driver)
        account_page = PersonalAccountPage(driver)
        feed_page = OrderFeed(driver)
        main_page.open_main_page()

        with allure.step("Добавить ингредиенты и оформить заказ"):
            order_number = main_page.create_order_and_return_number("Соус Spicy-X", "Краторная булка N-200i")

        with allure.step("Перейти в Личный кабинет и проверить заказ в истории"):
            main_page.scroll_and_click_personal_account_link()
            account_page.click_the_button_order_history()
            assert account_page.is_order_in_history(order_number)

        with allure.step("Перейти в Ленту заказов и найти заказ по номеру"):
            main_page.scroll_and_click_order_feed()


            assert feed_page.check_is_order_in_history (order_number)


    @allure.title('Проверка увеличения счётчика "Выполнено за всё время" после создания нового заказа')
    def test_total_done_counter_increases_after_order(self, driver, user, authorized_user):
        main_page = MainPage(driver)
        feed_page = OrderFeed(driver)

        with allure.step("переход в Ленту заказов"):
            main_page.scroll_and_click_order_feed()

        with allure.step("Получение текущего значения счётчика «Выполнено за всё время»"):
            counter_before = feed_page.get_total_done_counter()

        with allure.step("Переход на главную и создание нового заказа"):
            main_page.scroll_and_click_constructor_link()
            main_page.create_order_and_return_number("Соус Spicy-X", "Краторная булка N-200i")

        with allure.step("Возврат в Ленту заказов и получение нового значения счётчика"):
            main_page.scroll_and_click_order_feed()
            counter_after = feed_page.get_total_done_counter()

        with allure.step("Проверка, что значение счётчика увеличилось"):
            assert counter_after > counter_before

    @allure.title('Проверка увеличения счётчика "Выполнено за сегодня" после создания нового заказа')
    def test_total_done_today_counter_increases_after_order(self, driver, user, authorized_user):
        main_page = MainPage(driver)
        feed_page = OrderFeed(driver)

        with allure.step("Переход в Ленту заказов"):
            main_page.scroll_and_click_order_feed()

        with allure.step("Получение текущего значения счётчика «Выполнено за сегодня»"):
            counter_before = feed_page.get_total_done_today_counter()

        with allure.step("Переход на главную и создание нового заказа"):
            main_page.scroll_and_click_constructor_link()
            main_page.create_order_and_return_number("Соус Spicy-X", "Краторная булка N-200i")

        with allure.step("Возврат в Ленту заказов и получение нового значения счётчика"):
            main_page.scroll_and_click_order_feed()
            counter_after = feed_page.get_total_done_today_counter()

        with allure.step("Проверка, что значение счётчика увеличилось"):
            assert counter_after > counter_before

    @allure.title('Проверка появления номера нового заказа в разделе "В работе"')
    def test_order_number_appears_in_in_progress_section(self, driver, user, authorized_user):
        main_page = MainPage(driver)
        feed_page = OrderFeed(driver)

        with allure.step("Переход в Конструктор и оформление нового заказа"):
            main_page.open_main_page()
            main_page.scroll_and_click_constructor_link()
            new_order_number = main_page.create_order_and_return_number("Соус Spicy-X", "Краторная булка N-200i")

        with allure.step("Переход в Ленту заказов"):
            main_page.scroll_and_click_order_feed()

        with allure.step("Проверка, что номер заказа появился в списке 'В работе'"):

            assert feed_page.get_orders_in_progress() == '0'+new_order_number