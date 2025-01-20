import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

#Здесь тоже не знаю почему не прожимается профиль. Перепробовал вообще всё, что можно, но не могу нажать на этот дурацкий профиль. Хз. Я в отчаянии
    # Переход на вкладку 'account/profile'
    def burgers_account(self, browser):
        self.login(browser)

        WebDriverWait(browser, 20).until(EC.visibility_of_element_located(ComponentSelection.CHOICE_OF_SAUCE))
        browser.find_element(TopOfPage.ACCOUNT_ELM).click()

        WebDriverWait(browser, 20).until(EC.visibility_of_element_located(TopOfPage.ACCOUNT_ELM)).click()
        WebDriverWait(browser, 3).until(EC.url_to_be(EXPECTED_URL))

        assert browser.current_url == EXPECTED_URL, f'Ожидалось {EXPECTED_URL}, но текущий URL: {browser.current_url}'