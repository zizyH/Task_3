from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from config.config import DEFAULT_TIMEOUT
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def wait_for_overlay_to_disappear(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element_located(BasePageLocators.MODAL_OVERLAY)
            )
        except TimeoutException:
            pass

    def find(self, locator):
        self.wait_for_overlay_to_disappear()
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait_for_overlay_to_disappear()
        element = self.wait.until(EC.presence_of_element_located(locator))
        
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def fill(self, locator, text):
        self.wait_for_overlay_to_disappear()
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def is_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))