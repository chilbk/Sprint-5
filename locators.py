from selenium.webdriver.common.by import By

#Локаторы формы Регистрации
class RegistrationForm:
    #Поле ввода имени на форме Регистрации
    REGISTRATION_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    #Поле ввода почты на форме Регистрации
    REGISTRATION_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    #Поле ввода пароля на форме Регистрации
    REGISTRATION_PASS = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    #Кнопка регистрации на форме Регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//*[contains(@class,'button_button__33qZ0')]")

    #Локаторы формы Аутентификации
class AuthForm:
    #Поле ввода почты на форме Аутентификации
    AUTH_EMAIL = (By.XPATH, "//input[@type='text']")
    #Поле ввода пароля на форме Аутентификации
    AUTH_PASS = (By.XPATH, "//input[@type='password']")
    #Кнопка входа на форме Аутентификации
    AUTH_BUTTON = (By.XPATH, "//form/button")
    #Кнопка регистрации на форме Аутентификации
    AUTH_REG_BUTTON = (By.XPATH, "//a[@href='/register']")
    #Кнопка восстановления пароля на форме Аутентификации
    AUTH_PASS_RECOVERY = (By.XPATH, "//a[@href='/forgot-password']")
    #Ошбика Некорректный пароль
    AUTH_PASS_ERROR = (By.XPATH, "//p[contains(., 'Некорректный')]")

    #Локаторы верхней части страницы
class TopOfPage:
    #Кнопка для перехода на Конструктор
    CONSTRUCTOR_ELM = (By.XPATH, "//a[contains(., 'Конструктор')]")
    #Кнопка для перехода на Конструктор по Логотипу
    LOGO_ELM = (By.XPATH, "//div/a[@href='/']")
    #Кнопка для перехода на экран Заказов
    ORDER_FEED_ELM = (By.XPATH, "//a[contains(., 'Лента Заказов')]")
    #Кнопка для перехода в Личный кабинет
    ACCOUNT_ELM = (By.XPATH, ".//*[@href='/account']")

    #Локаторы настройки бургера
class ComponentSelection:
    #Кнопка для перехода на выбор Булки
    CHOICE_OF_BUNN = (By.XPATH, "//span[text()='Булки']")
    #Кнопка для перехода на выбор Начинки
    CHOICE_OF_SAUCE = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    #Кнопка для перехода на выбор Соусов
    CHOICE_OF_FILLING = (By.XPATH, "//span[contains(text(), 'Начинки')]")

class ToAuth:
    #Переход на форму Авторизации из главного окна
    MAIN_SCREEN_AUTH = (By.XPATH, "//button[text()='Войти в аккаунт']")
    #Переход на форму Авторизации по нажатию на 'Личный кабинет'
    LOGIN_SCREEN_AUTH = (By.XPATH, ".//*[@href='/account']")
    #Переход на форму Авторизации на экране регистрации
    REG_SCREEN_AUTH = (By.XPATH, "//a[@href='/login']")
    #Переход на форму Авторизации на экране восстановления пароля
    RECOVERY_SCREEN_AUTH = (By.XPATH, "//a[@href='/login']")

class Logout:
    LOGOUT_FROM_ACCOUNT = (By.XPATH, "//button[contains(., 'Выход')]")