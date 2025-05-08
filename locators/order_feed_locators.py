from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER_LINK = (By.XPATH,'//li[contains(@class, "OrderHistory_listItem")]//a[contains(@class, "OrderHistory_link__1iNby")]') #локатор выбирает первый (или любой) заказ в списке
    ORDER_DETAILS_MODAL = (By.XPATH,'//div[contains(@class, "Modal_orderBox__1xWdi")]') #локатор для модалки деталей заказа
    ORDER_NUMBER_TEMPLATE = (By.XPATH, './/*[text()="{order_id}"]') #локатор для поска по номеру заказа
    TOTAL_DONE_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p') # Счетчик сделанных заказов за все время
    TOTAL_DONE_TODAY_COUNTER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p') # Счетчик сделанных заказов за сегодня
    ORDER_IN_WORK_NUMBER =  (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]')
    ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')
    FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")