from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/parent::div/input') # поле ввода emeil
    PASSWORD_INPUT = (By.NAME, 'Пароль') # поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]') # кнопка входа
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']") # гиперссылка "Зарегистрироваться"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']") # гиперссылка "Восстановить пароль"
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']") # Заголовок формы входа, текст "Вход"