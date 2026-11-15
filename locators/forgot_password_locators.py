from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    # Главная страница (кнопка "Войти в аккаунт")
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Страница логина (ссылка "Восстановить пароль")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")

    
    # Поле email 
    EMAIL_INPUT = (By.NAME, "name")
    # Кнопка "Восстановить"
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    # Поле пароля, которое подсвечивается
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    
    # Кнопка "глаз" (показать/скрыть пароль)
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")