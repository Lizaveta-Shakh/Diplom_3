from selenium.webdriver.common.by import By

class MainPageLocators: #+Конструктор
    PERSONAL_ACCOUNT_LINK = (By.XPATH, ".//*[text()='Личный Кабинет']") # Кнопка-гипрссылка "Личный кабинет"
    LOG_IN_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']") #Кнопка входа с главной, видна тольео если пользователь еще не авторизовался
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]') # Кнопка "оформить заказ", если соверщена авторизация
    CONSTRUCTOR_LINK = (By.XPATH, '//p[text() = "Конструктор"]') #Гиперссылка "Конструктор"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']") # кнопка для перехода к разделу "Соусы" на таб нав с заголовками разделов
    LINK_ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li') # кнопка "Лента заказов"
    INGR_DETAILS_WINDOW_HEADER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]') # Заголовок окна с инфо о ингредиенте
    CROSS_ICON_FOR_ING_MODAL = (By.XPATH, '//section[contains(@class, ''"Modal_modal_opened")]//button[contains(@class, "close")]') # Кнопка закрытия окна инфо о ингредиенте
    ORDER_NUMBER_TITLE = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(@class, "text_type_digits-large")]') #Номер заказа заголовок
    BURGER_CONSTRUCTOR_ZONE = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]') # Зона конструктор
    SPICY_X_INGREDIENT = (By.XPATH, '//p[text()="Соус Spicy-X"]/ancestor::a')
    ORDER_FEED_TEXT = (
        By.XPATH,
        "//a[@href='/feed']//p[text()='Лента Заказов']"
    )
    # Cчетчик ингредиента
    @staticmethod
    def ingredient_counter_locator(name: str):
        return (
            By.XPATH, f'//p[text()="{name}"]/ancestor::a//p[contains(@class, "counter_counter__num__3nue1")]')

    # Локатор ингредиента(по передаче имени ингредиента)
    @staticmethod
    def ingredient_by_name(name: str):
        return (
            By.XPATH,
            f'//p[text()="{name}"]/ancestor::a'
        )


