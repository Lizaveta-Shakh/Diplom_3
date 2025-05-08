from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    EMAIL_INPUT_FIELD =  (By.CLASS_NAME, 'input__textfield') #Поле ввода почты
    RESTORE_BUTTON = (By.CLASS_NAME, 'button_button__33qZ0') #Кнопка для восстановления пароля
    REMEMBER_PASSWORD_LOGIN = (By.XPATH, "//p[contains(text(), 'Вспомнили пароль?')]/a[text()='Войти']") #Переход на стр логина


class ResetPasswordLocators:
    PASSWORD_INPUT_FIELD =  (By.CSS_SELECTOR, '.input_type_password .input__textfield') #Поле ввода пароля
    HIDE_EYE_ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]') # иконка показать\скрыть пароль
    ACTIVE_PASSWORD_FIELD = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, ''"input_status_active")]') #Поле "Пароль" в фокусе (нажать на глаз)