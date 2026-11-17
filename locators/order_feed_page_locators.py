from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    # Заголовок страницы
    PAGE_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # Карточка первого заказа в ленте (для клика)
    FIRST_ORDER = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem')])[1]")
    
    # Модальное окно с деталями заказа (открывается по клику)
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    
    # Счетчики
    TOTAL_ORDERS_ALL_TIME = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")
    TOTAL_ORDERS_TODAY = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")
    
    # Раздел "В работе"
    IN_PROGRESS_LIST = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul/li")
    
    # Кнопка "Лента заказов" в шапке (для перехода из Конструктора)
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")