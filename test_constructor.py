import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ComponentSelection
from main import RECOURSE_URL

class TestComponentNavigation:
    @pytest.fixture(scope="function")
    def browser(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_navigation_tabs(self, browser):
        # Переход на главную страницу
        browser.get(RECOURSE_URL)

        wait = WebDriverWait(browser, 10)

        # Переход на вкладку Соусы. Если нет такой вкладки - выдаёт ошибку
        sauce_tab = wait.until(EC.element_to_be_clickable(ComponentSelection.CHOICE_OF_SAUCE))
        sauce_tab.click()
        assert 'Соусы' in browser.page_source, 'Вкладка 'Соусы' не активировалась.'

        # Переход на вкладку Булки. Если нет такой вкладки - выдаёт ошибку
        buns_tab = wait.until(EC.element_to_be_clickable(ComponentSelection.CHOICE_OF_BUNN))
        buns_tab.click()
        assert 'Булки' in browser.page_source, 'Вкладка 'Булки' не активировалась.'

        # Переход на вкладку Начинки. Если нет такой вкладки - выдаёт ошибку
        fillings_tab = wait.until(EC.element_to_be_clickable(ComponentSelection.CHOICE_OF_FILLING))
        fillings_tab.click()
        assert 'Начинки' in browser.page_source, 'Вкладка 'Начинки' не активировалась.'
