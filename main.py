
#ИЗВИНИТЕ, ПОЖАЛУЙСТА, Я ОЧЕНЬ СТАРАЛСЯ, НО У МЕНЯ ОЧЕНЬ КАК-ТО КРИВО ВСЁ ВЫШЛО :(
#Если можно, то напишите, пожалуйста, подробнее, как мне пофиксить проблемы с кодом. Я в отчаянии. 100% Despair

# ПО ПОВОДУ ПАПКИ TESTS:
    # ----> У МЕНЯ СТАЛА ПОЯВЛЯТЬСЯ ОШИБКА SRC. ПОЧИНИТЬ НЕ ПОЛУЧИЛОСЬ. Я БУДУ СЧАСТЛИВ ДО НЕБЕС, ЕСЛИ СКАЖЕТЕ, КАК МНЕ ПОФИКСИТЬ ПРОБЛЕМЫ
    # КОД ОШИБКИ:
    # tests\test_reg_form.py:2: in <module>
    #    from main import RECOURSE_URL
    #    ModuleNotFoundError: No module named 'main'

    # При это я подключал main. Я не знаю, как это исправить и что делать

import random as rnd

RECOURSE_URL = 'https://stellarburgers.nomoreparties.site/'
class Auth:
    def generate_login(self):
        return f"vda_17_{rnd.randint(100, 999)}@example.com"

    def generate_password(self):
        return 'vda_' + str(rnd.randint(100000, 999999))

