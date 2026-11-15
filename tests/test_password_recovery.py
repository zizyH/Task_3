import allure
from pages.forgot_password_page import ForgotPasswordPage
import time

@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    def go_to_reset_password_step(self, page, email):
        """Вспомогательный метод, чтобы не дублировать код"""
        page.click_login_account_button()
        page.click_recover_password_link()
        page.enter_email(email)
        page.click_recover_button()
        page.wait.until(lambda d: "reset-password" in d.current_url)

    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_recovery_page(self, driver):
        page = ForgotPasswordPage(driver)
        page.click_login_account_button()
        page.click_recover_password_link()
        assert "forgot-password" in driver.current_url

    @allure.title("Ввод email и переход ко второму шагу")
    def test_submit_recovery_form(self, driver, test_user):
        page = ForgotPasswordPage(driver)
        self.go_to_reset_password_step(page, test_user["email"])
        assert "reset-password" in driver.current_url

    @allure.title("Кнопка показать/скрыть пароль делает поле активным")
    def test_show_hide_password_activates_field(self, driver, test_user):
        page = ForgotPasswordPage(driver)
        
        self.go_to_reset_password_step(page, test_user["email"])

        assert page.get_password_input_type() == "password"

        page.click_show_hide_password()

       
        assert page.get_password_input_type() == "text"

        
        assert page.is_password_field_active()