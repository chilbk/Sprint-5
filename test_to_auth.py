import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import ToAuth
from main import RECOURSE_URL

RECOURSE_MAIN = RECOURSE_URL
RECOURSE_LOGIN = RECOURSE_URL
RECOURSE_REG = RECOURSE_URL + 'register'
RECOURSE_RECOVERY = RECOURSE_URL + 'forgot-password'
EXPECTED_URL = RECOURSE_LOGIN + 'login'
class TestAuthNavigation:

    @pytest.fixture(scope="function")
    def browser(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    @pytest.mark.parametrize("start_url, auth_locator, expected_url", [
        (RECOURSE_MAIN, ToAuth.MAIN_SCREEN_AUTH, EXPECTED_URL),       # Главная страница
        (RECOURSE_MAIN, ToAuth.LOGIN_SCREEN_AUTH, EXPECTED_URL),      # Главная страница. Кнопка Личный кабинет
        (RECOURSE_REG, ToAuth.REG_SCREEN_AUTH, EXPECTED_URL),         # Экран регистрации
        (RECOURSE_RECOVERY, ToAuth.RECOVERY_SCREEN_AUTH, EXPECTED_URL), # Экран восстановления
    ])

    # Сверяем ОР и ФР по URL
    def test_navigation_to_auth(self, browser, start_url, auth_locator, expected_url):
        browser.get(start_url)
        expected_url = EXPECTED_URL
        try:
            auth_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(auth_locator))
            auth_button.click()

            WebDriverWait(browser, 10).until(EC.url_to_be(expected_url))
            assert browser.current_url == expected_url, f'Ожидалось {expected_url}, но текущий URL: {browser.current_url}'
        except TimeoutException:
            pytest.fail(f'Кнопка не стала кликабельной или переход не произошёл на {expected_url}')