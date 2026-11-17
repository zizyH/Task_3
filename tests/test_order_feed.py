import allure
import time
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.account_page import AccountPage

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Клик по заказу открывает всплывающее окно с деталями")
    def test_click_order_opens_modal(self, driver):
        page = OrderFeedPage(driver)
        page.click_order_feed()
        page.click_first_order()
        assert page.is_order_modal_visible()

    @allure.title("Заказы из Истории заказов отображаются в Ленте")
    def test_order_from_history_in_feed(self, logged_in_driver):
        # 1. Оформляем заказ
        main_page = MainPage(logged_in_driver)
        main_page.click_constructor()
        main_page.add_ingredient_to_order()
        main_page.click_make_order()
        main_page.close_modal()

        # 2. Идем в историю заказов и берем реальный номер
        
        account_page = AccountPage(logged_in_driver)
        account_page.click_personal_account()
        account_page.click_order_history()
        real_order_number = account_page.get_first_order_number_in_history()
       

        # 3. Идем в ленту заказов
        feed_page = OrderFeedPage(logged_in_driver)
        feed_page.click_order_feed()

        # 4. Проверяем, что этот номер есть в первом заказе ленты
        assert real_order_number in feed_page.get_first_order_text()

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается")
    def test_total_orders_all_time_increases(self, logged_in_driver):
        feed_page = OrderFeedPage(logged_in_driver)
        feed_page.click_order_feed()
        
        initial_count = feed_page.get_total_orders_all_time()
        main_page = MainPage(logged_in_driver)
        main_page.click_constructor()
        main_page.add_ingredient_to_order()
        main_page.click_make_order()
        main_page.close_modal()
        feed_page.click_order_feed()
        time.sleep(1)
        new_count = feed_page.get_total_orders_all_time()
        assert new_count > initial_count

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается")
    def test_total_orders_today_increases(self, logged_in_driver):
        feed_page = OrderFeedPage(logged_in_driver)
        feed_page.click_order_feed()
        
        initial_count = feed_page.get_total_orders_today()
        
        main_page = MainPage(logged_in_driver)
        main_page.click_constructor()
        main_page.add_ingredient_to_order()
        main_page.click_make_order()
        main_page.close_modal()
        
        feed_page.click_order_feed()
        time.sleep(1)
        new_count = feed_page.get_total_orders_today()
        assert new_count > initial_count

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        main_page.click_constructor()
        main_page.add_ingredient_to_order()
        main_page.click_make_order()
        order_number = main_page.get_order_number_from_modal()
        main_page.close_modal()
        
        feed_page = OrderFeedPage(logged_in_driver)
        feed_page.click_order_feed()
        
        feed_page.wait.until(lambda d: feed_page.is_order_in_progress(order_number))
        assert feed_page.is_order_in_progress(order_number)