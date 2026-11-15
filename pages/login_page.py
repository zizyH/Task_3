from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def login(self, email, password):
        # Вводим email
        self.fill(LoginPageLocators.EMAIL_INPUT, email)
        # Вводим пароль
        self.fill(LoginPageLocators.PASSWORD_INPUT, password)
        # Жмем кнопку "Войти"
        self.click(LoginPageLocators.LOGIN_BUTTON)