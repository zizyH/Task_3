from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):
    def click_personal_account(self):
        self.click(AccountPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_order_history(self):
        self.click(AccountPageLocators.ORDER_HISTORY_BUTTON)

    def click_logout(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)

    def is_profile_visible(self):
        return self.is_visible(AccountPageLocators.PROFILE_TEXT)
    def get_first_order_number_in_history(self):
        element = self.find(AccountPageLocators.ORDER_HISTORY_ITEM)
        return element.text