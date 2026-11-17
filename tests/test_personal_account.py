import allure

@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_go_to_personal_account(self, logged_in_driver):
        assert "/account/profile" in logged_in_driver.current_url

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_order_history(self, logged_in_driver):
        from pages.account_page import AccountPage
        account_page = AccountPage(logged_in_driver)
        
        account_page.click_order_history()
        assert "/account/order-history" in logged_in_driver.current_url

    @allure.title("Выход из аккаунта")
    def test_logout(self, logged_in_driver):
        from pages.account_page import AccountPage
        account_page = AccountPage(logged_in_driver)
        
        account_page.click_logout()
    
        account_page.wait.until(lambda d: "/login" in d.current_url)
        
        assert "/login" in logged_in_driver.current_url