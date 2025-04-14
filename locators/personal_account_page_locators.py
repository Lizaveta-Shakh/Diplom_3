from selenium.webdriver.common.by import By

class ProfilePageLocators:
    ORDER_HISTORY_LINK = (By.LINK_TEXT, 'История заказов') #гиперссылка "История заказов" в личном кабинете
    CONSTRUCTOR_LINK = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Конструктор"]') # Гиперссылка "Конмтруктор" в шапке
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Логотип "Stellar Burgers" в шапке
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") #кнопка выхода в личном кабинете
    ORDER_NUMBER_ITEM = lambda order_number: (By.XPATH, f'//p[contains(text(), "{order_number.zfill(7)}")]') # локатор для поиска элемента с номером заказа по тексту