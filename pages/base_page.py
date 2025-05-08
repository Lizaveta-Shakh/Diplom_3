import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from seletools.actions import drag_and_drop

from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    def __init__(self, driver):
        self.driver = driver


    #  Поиск элементов
    @allure.step('возвращает один элемент (первый найденный)')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('возвращает список всех элементов, подходящих под локатор')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)



    #  Ожидания

    @allure.step('Открыть страницу')
    def open_page(self, page_url):
        self.driver.get(page_url)

    @allure.step("Ожидание видимости элемента")
    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_element_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))


    @allure.step("Ожидание, пока элемент станет невидимым")
    def wait_for_invisibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator))

    @allure.step("Ожидание исчезновения модального оверлея")
    def wait_modal_overlay_disappears(self, overlay_locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(overlay_locator)
            )
        except:
            pass

    @allure.step("Ожидание появления корректного номера заказа")
    def wait_for_correct_order_number(self, locator, timeout=5):
        def valid_number(driver):
            try:
                element = driver.find_element(*locator)
                text = element.text.strip()
                return text.isdigit() and len(text) >= 5
            except:
                return False

        WebDriverWait(self.driver, timeout).until(valid_number)
        return self.driver.find_element(*locator)

    @allure.step("Ожидание появления текста в элементе")
    def wait_for_text_to_be_present_in_element(self, locator, text):
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(locator, text))



    #  Проверки
    @allure.step("Проверка, что элемент стал невидимым")
    def is_element_invisible(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator))
            return True
        except:
            return False

    @allure.step("Проверка, что элемент видим на странице")
    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Сравнение текущего URL")
    def is_current_url(self, url):
        return self.driver.current_url == url

    @allure.step("Сравнение, что URL содержит подстроку")
    def current_url_contains(self, url_part):
        return url_part in self.driver.current_url



    #  Взаимодействие с элементами
    @allure.step("Ввод текста в поле")
    def send_keys_to_input(self, locator, keys, timeout=15):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Нажатие на элемент")
    def click_on_element(self, locator, timeout=15):
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    @allure.step("Клик по элементу с повторными попытками")
    def click_to_element_few_tries(self,
                                   locator,
                                   attempts: int = 4,
                                   timeout: int = 4,
                                   overlay_locator = None):
        for attempt in range(attempts):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
                return
            except ElementClickInterceptedException:
                if overlay_locator:
                    self.wait_modal_overlay_disappears(overlay_locator, timeout)
                else:
                    WebDriverWait(self.driver, timeout).until(
                        EC.element_to_be_clickable(locator)
                    )
            except Exception as e:
                if attempt == attempts - 1:
                    raise Exception(f"Не удалось кликнуть по элементу {locator} после {attempts} попыток") from e


    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=15):
        element = self.wait_for_element_clickable(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Скролл и безопасный клик")
    def scroll_and_click(self, locator, overlay_locator=None):
        self.scroll_to_element(locator)
        if overlay_locator:
            self.wait_modal_overlay_disappears(overlay_locator)
        self.click_to_element_few_tries(
            locator,
            overlay_locator=overlay_locator
        )

    @allure.step("Клик по элементу с помощью JavaScript")
    def javascript_click(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)  # Убедиться, что элемент есть в DOM
        self.driver.execute_script("arguments[0].click();", element)



    #  Drag & Drop
    @allure.step("Перетащить элемент через seletools")
    def drag_and_drop_with_seletools(self, source_element, target_element):
        drag_and_drop(self.driver, source_element, target_element)



