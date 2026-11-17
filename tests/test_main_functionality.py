import allure
import time
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, logged_in_driver):
        page = MainPage(logged_in_driver)
        page.click_order_feed()
        page.click_constructor()
        # Конструктор — это главная страница
        assert logged_in_driver.current_url == "https://qa-stellarburgers.education-services.ru/"

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_order_feed(self, logged_in_driver):
        page = MainPage(logged_in_driver)
        page.click_order_feed()
        assert "/feed" in logged_in_driver.current_url

    @allure.title("Клик по ингредиенту открывает всплывающее окно")
    def test_ingredient_modal_opens(self, driver):
        page = MainPage(driver)
        page.click_ingredient()
        assert page.is_modal_visible()

    @allure.title("Всплывающее окно закрывается по крестику")
    def test_ingredient_modal_closes(self, driver):
        page = MainPage(driver)
        page.click_ingredient()
        page.close_modal()
        # Ждем немного, пока окно исчезнет, и проверяем, что его нет
        assert page.is_invisible(MainPageLocators.MODAL_TITLE)

    @allure.title("При добавлении ингредиента увеличивается каунтер")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        page.wait.until(lambda d: page.get_ingredient_counter() == 0)
        page.add_ingredient_to_order()
        page.wait.until(lambda d: page.get_ingredient_counter() > 0)
        new_count = page.get_ingredient_counter()
        assert new_count > 0, f"Счетчик не увеличился, текущее значение: {new_count}"

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_make_order(self, logged_in_driver):
        page = MainPage(logged_in_driver)
        page.click_constructor()
        page.add_ingredient_to_order()
        page.click_make_order()
        assert page.is_order_modal_visible()