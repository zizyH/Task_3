from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):
    def click_order_feed(self):
        self.click(OrderFeedPageLocators.ORDER_FEED_BUTTON)

    def click_first_order(self):
        self.click(OrderFeedPageLocators.FIRST_ORDER)

    def is_order_modal_visible(self):
        return self.is_visible(OrderFeedPageLocators.ORDER_MODAL)

    def get_total_orders_all_time(self):
        return int(self.find(OrderFeedPageLocators.TOTAL_ORDERS_ALL_TIME).text)

    def get_total_orders_today(self):
        return int(self.find(OrderFeedPageLocators.TOTAL_ORDERS_TODAY).text)

    def is_order_in_progress(self, order_number):
        elements = self.driver.find_elements(*OrderFeedPageLocators.IN_PROGRESS_LIST)
        for el in elements:
            if order_number in el.text:
                return True
        return False
    
    def get_first_order_text(self):
        return self.find(OrderFeedPageLocators.FIRST_ORDER).text