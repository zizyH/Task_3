import allure
from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
from selenium.webdriver.common.by import By

class ForgotPasswordPage(BasePage):
    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_account_button(self):
        self.click(ForgotPasswordLocators.LOGIN_ACCOUNT_BUTTON)

    @allure.step("Клик по ссылке 'Восстановить пароль'")
    def click_recover_password_link(self):
        self.click(ForgotPasswordLocators.RECOVER_PASSWORD_LINK)

    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        self.fill(ForgotPasswordLocators.EMAIL_INPUT, email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_recover_button(self):
        self.click(ForgotPasswordLocators.RECOVER_BUTTON)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_hide_password(self):
        self.click(ForgotPasswordLocators.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step("Получение типа поля пароля (password/text)")
    def get_password_input_type(self):
        element = self.find(ForgotPasswordLocators.PASSWORD_INPUT)
        return element.get_attribute("type")

    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        element = self.find(ForgotPasswordLocators.PASSWORD_INPUT)
        parent_div = element.find_element(By.XPATH, "./..") 
        return "input_status_active" in parent_div.get_attribute("class")