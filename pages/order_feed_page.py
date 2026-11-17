import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):
    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed(self):
        self.click(OrderFeedPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик по первому заказу в ленте")
    def click_first_order(self):
        self.click(OrderFeedPageLocators.FIRST_ORDER)

    @allure.step("Проверка видимости модального окна заказа")
    def is_order_modal_visible(self):
        return self.is_visible(OrderFeedPageLocators.ORDER_MODAL)

    @allure.step("Получение счетчика 'Выполнено за всё время'")
    def get_total_orders_all_time(self):
        return int(self.find(OrderFeedPageLocators.TOTAL_ORDERS_ALL_TIME).text)

    @allure.step("Получение счетчика 'Выполнено за сегодня'")
    def get_total_orders_today(self):
        return int(self.find(OrderFeedPageLocators.TOTAL_ORDERS_TODAY).text)

    @allure.step("Проверка наличия заказа {order_number} в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        elements = self.driver.find_elements(*OrderFeedPageLocators.IN_PROGRESS_LIST)
        for el in elements:
            if order_number in el.text:
                return True
        return False
        
    @allure.step("Получение текста первого заказа в ленте")
    def get_first_order_text(self):
        return self.find(OrderFeedPageLocators.FIRST_ORDER).text