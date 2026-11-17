import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):
    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_personal_account(self):
        self.click(AccountPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Клик по кнопке 'История заказов'")
    def click_order_history(self):
        self.click(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Клик по кнопке 'Выход'")
    def click_logout(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step("Проверка видимости профиля")
    def is_profile_visible(self):
        return self.is_visible(AccountPageLocators.PROFILE_TEXT)
        
    @allure.step("Получение номера первого заказа из истории")
    def get_first_order_number_in_history(self):
        element = self.find(AccountPageLocators.ORDER_HISTORY_ITEM)
        return element.text