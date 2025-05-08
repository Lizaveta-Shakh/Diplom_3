import allure
from pages.main_order_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAcc:
    @allure.title('Проверка перехода в личный кабинет по клику на «Личный кабинет»')
    def test_click_personal_account_link_opens_account_page(self, driver, user, authorized_user):
        main_page = MainPage(driver)
        account_page = PersonalAccountPage(driver)

        with allure.step("Открытие главной страницы и переход по кнопке «Личный кабинет»"):
            main_page.open_main_page()
            main_page.scroll_and_click_personal_account_link_js()

        with allure.step("Проверка, что открыт личный кабинет"):
            assert account_page.is_account_page()



    @allure.title('Проверка перехода в "История заказов" по клику на «История заказов»')
    def test_click_order_history_link_opens_order_history_page(self, driver, user, authorized_user):
        account_page = PersonalAccountPage(driver)

        with allure.step("Открытие страницы личного кабинета и переход в Историю заказов"):
            account_page.open_account_page()
            account_page.click_the_button_order_history_js()

        with allure.step("Проверка, что URL соответствует странице истории заказов"):
            assert account_page.is_current_url_order_history()



    @allure.title('Проверка выхода из учетной записи по клику на «Выход»')
    def test_click_exit_link_opens_login_page(self, driver, user, authorized_user):
        login_page = LoginPage(driver)
        account_page = PersonalAccountPage(driver)

        with allure.step("Открытие страницы личного кабинета"):
            account_page.open_account_page()
        with allure.step("Клик на кнопку 'Выход'"):
            account_page.click_the_button_exit_js()
        with allure.step("Ожидание появления кнопки 'Войти' на странице логина"):
            login_page.wait_for_login_button()

        with allure.step("Проверка, что URL соответствует странице логина"):
            assert login_page.is_current_url_login()








