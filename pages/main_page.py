import allure
import time
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By 

class MainPage(BasePage):
    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик по ингредиенту 'Краторная булка N-200i'")
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT_BUN)

    @allure.step("Закрытие модального окна по крестику")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверка видимости модального окна")
    def is_modal_visible(self):
        return self.is_visible(MainPageLocators.MODAL_TITLE)

    @allure.step("Получение значения каунтера ингредиента")
    def get_ingredient_counter(self):
        return int(self.find(MainPageLocators.INGREDIENT_COUNTER).text)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        source = self.find(MainPageLocators.INGREDIENT_BUN)
        
        script = """
        var source = arguments[0];
        var target = document.querySelector('.BurgerConstructor_basket__container__2fUl3');
        
        if (source && target) {
            var evt = document.createEvent('CustomEvent');
            evt.initCustomEvent('dragstart', true, true, null);
            source.dispatchEvent(evt);
            
            evt = document.createEvent('CustomEvent');
            evt.initCustomEvent('drop', true, true, null);
            target.dispatchEvent(evt);
            
            evt = document.createEvent('CustomEvent');
            evt.initCustomEvent('dragend', true, true, null);
            source.dispatchEvent(evt);
        }
        """
        self.driver.execute_script(script, source)
        time.sleep(0.5)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_make_order(self):
        self.click(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step("Проверка видимости окна с идентификатором заказа")
    def is_order_modal_visible(self):
        return self.is_visible(MainPageLocators.ORDER_NUMBER_MODAL)
        
    @allure.step("Получение номера заказа из модального окна")
    def get_order_number_from_modal(self):
        element = self.find(MainPageLocators.ORDER_NUMBER_MODAL)
        return element.text.strip()