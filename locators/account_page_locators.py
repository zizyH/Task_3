from selenium.webdriver.common.by import By

class AccountPageLocators:
    # Ссылка "Личный кабинет" в шапке сайта
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and contains(., 'Личный Кабинет')]")
    
    # Ссылка "История заказов" в боковом меню ЛК
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[@href='/account/order-history']")
    
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
    ORDER_HISTORY_ITEM = (By.XPATH, "(//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text_type_digits-default')])[1]")