from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT_BUN = (By.XPATH, "//img[@alt='Краторная булка N-200i']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")