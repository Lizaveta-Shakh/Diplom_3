class BaseUrls:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

class PageUrls(BaseUrls):
    MAIN_PAGE = f"{BaseUrls.BASE_URL}/"
    LOGIN_PAGE = f"{BaseUrls.BASE_URL}/login"
    REGISTRATION_PAGE = f"{BaseUrls.BASE_URL}/register"
    PERSONAL_ACCOUNT_PAGE = f"{BaseUrls.BASE_URL}/account"
    ORDER_HISTORY_ACCOUNT = f"{BaseUrls.BASE_URL}/account/order-history"
    FORGOT_PASSWORD_PAGE = f"{BaseUrls.BASE_URL}/forgot-password"
    RESET_PASSWORD_PAGE = f"{BaseUrls.BASE_URL}/reset-password"
    FEED_PAGE = f"{BaseUrls.BASE_URL}/feed"