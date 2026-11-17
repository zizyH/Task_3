import pytest
from selenium import webdriver
from config.config import BASE_URL
from helpers.api_client import ApiClient
from pages.account_page import AccountPage
from pages.login_page import LoginPage

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(BASE_URL)
    yield browser
    browser.quit()

@pytest.fixture
def test_user():
    user = ApiClient.register_user()
    yield user
    ApiClient.delete_user(user["access_token"])


@pytest.fixture
def logged_in_driver(driver, test_user):
    account_page = AccountPage(driver)
    
    # 1. Переход на форму логина
    account_page.click_personal_account()
    
    # 2. Логин
    login_page = LoginPage(driver)
    login_page.login(test_user["email"], test_user["password"])
    
    # 3. Ждем, пока залогинимся (URL перестанет содержать /login)
    account_page.wait.until(lambda d: "/login" not in d.current_url)
    
    # 4. Снова кликаем на "Личный кабинет", чтобы попасть в профиль
    account_page.click_personal_account()
    account_page.wait.until(lambda d: "/account/profile" in d.current_url)
    
    yield driver