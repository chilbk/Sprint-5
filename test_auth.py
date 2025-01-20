import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import AuthForm
from main import RECOURSE_URL

RESOURCE = RECOURSE_URL + 'login'

class TestAuth:

    @pytest.fixture(scope="function")
    def browser(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

#Подскажите, пожалуйста, как мне сделать так, чтобы в случае неверного пароля отображался код ошибки, но тест был успешным :((((((((((((((((((((
    @pytest.mark.parametrize("email, password, should_succeed", [
        ("vd3322@mail.ru", "qwe123", True),
        ("vd3322@mail.ru", "qwe1233", False),])
    def test_login(self, browser, email, password, should_succeed):
        browser.get(RESOURCE)

        #Вводим логин
        email_input = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(AuthForm.AUTH_EMAIL))
        email_input.send_keys(email)

        #Вводим пароль
        pass_input = browser.find_element(*AuthForm.AUTH_PASS)
        pass_input.send_keys(password)

        #Кнопка входа
        login_button = browser.find_element(*AuthForm.AUTH_BUTTON)
        login_button.click()

        if should_succeed:
            try:
                WebDriverWait(browser, 3).until(
                    EC.url_changes(RESOURCE)
                )
            except TimeoutException:
                raise AssertionError('Не удалось войти: ошибка авторизации.')

            assert browser.current_url != RESOURCE, 'Не удалось войти: ошибка авторизации.'