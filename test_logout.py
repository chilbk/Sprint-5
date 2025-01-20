import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Logout
from main import RECOURSE_URL
from locators import AuthForm
from locators import TopOfPage
from locators import ComponentSelection

EXPECTED_URL = RECOURSE_URL + 'login'
ACCOUNT_URL = RECOURSE_URL + 'account/profile'

class TestLogout:

    @pytest.fixture(scope="function")
    def browser(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def login(self, browser):
        browser.get(EXPECTED_URL)
        # Ввод логина - email
        email_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AuthForm.AUTH_EMAIL) )
        email_input.send_keys('vd3322@mail.ru')
        # Ввод пароля - password
        pass_input = browser.find_element(*AuthForm.AUTH_PASS)
        pass_input.send_keys('qwe123')
        # Нажатие на клавишу
        login_button = browser.find_element(*AuthForm.AUTH_BUTTON)
        login_button.click()

        WebDriverWait(browser, 10).until(EC.url_to_be(ACCOUNT_URL))

    def test_logout_and_check_account(self, browser):
        # Выполняем авторизацию
        self.login(browser)

        # Я искренне не понимаю, как сделать этот код рабочим. Что здесь не так? Я пытался ждать прогрузки, пытался ждать, когда элемент станет кликабельным. Что не так в конце концов
        #Я 3 часа убил на это, но не знаю, что делать. Просто 0 понимания
        WebDriverWait(browser, 20).until(EC.visibility_of_element_located(ComponentSelection.CHOICE_OF_BUNN))
        browser.find_element(TopOfPage.ACCOUNT_ELM).click()

        WebDriverWait(browser, 20).until(EC.element_to_be_clickable(TopOfPage.ACCOUNT_ELM)).click()

        # Выполняем логаут
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable(Logout.LOGOUT_FROM_ACCOUNT)).click()

        # Проверяем, что текущий URL соответствует ожидаемому
        WebDriverWait(browser, 3).until(EC.url_to_be(EXPECTED_URL))
        assert browser.current_url == EXPECTED_URL, f'Ожидалось {EXPECTED_URL}, но текущий URL: {browser.current_url}'
