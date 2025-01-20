import pytest
from main import RECOURSE_URL
from main import Auth
from locators import RegistrationForm
from selenium import webdriver

# URL ресурса
RECOURSE = RECOURSE_URL + 'register'
#WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# Тест регистрации
def test_registration(driver):
    # Создание экземпляра класса Auth
    auth = Auth()
    # Генерирует рандомный логин
    test_email = auth.generate_login()
    # Генерирует рандомный пароль
    test_password = auth.generate_password()
    # Имя
    test_name = "Dmitry"

#URL формы регистрации
    driver.get(RECOURSE)
#Ввод параметров
    driver.find_element(*RegistrationForm.REGISTRATION_NAME).send_keys(test_name)
    driver.find_element(*RegistrationForm.REGISTRATION_EMAIL).send_keys(test_email)
    driver.find_element(*RegistrationForm.REGISTRATION_PASS).send_keys(test_password)
#Клик на кнопку Зарегистрироваться
    driver.find_element(*RegistrationForm.REGISTRATION_BUTTON).click()