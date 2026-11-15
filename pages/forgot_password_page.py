from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
from selenium.webdriver.common.by import By

class ForgotPasswordPage(BasePage):
    def click_login_account_button(self):
        self.click(ForgotPasswordLocators.LOGIN_ACCOUNT_BUTTON)

    def click_recover_password_link(self):
        self.click(ForgotPasswordLocators.RECOVER_PASSWORD_LINK)

    def enter_email(self, email):
        self.fill(ForgotPasswordLocators.EMAIL_INPUT, email)

    def click_recover_button(self):
        self.click(ForgotPasswordLocators.RECOVER_BUTTON)

    def click_show_hide_password(self):
        self.click(ForgotPasswordLocators.SHOW_HIDE_PASSWORD_BUTTON)

    def get_password_input_type(self):
        element = self.find(ForgotPasswordLocators.PASSWORD_INPUT)
        return element.get_attribute("type")

    def is_password_field_active(self):
        element = self.find(ForgotPasswordLocators.PASSWORD_INPUT)
        parent_div = element.find_element(By.XPATH, "./..") 
        return "input_status_active" in parent_div.get_attribute("class")