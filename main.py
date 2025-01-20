import random as rnd

RECOURSE_URL = 'https://stellarburgers.nomoreparties.site/'
class Auth:
    def generate_login(self):
        return f"vda_17_{rnd.randint(100, 999)}@example.com"

    def generate_password(self):
        return 'vda_' + str(rnd.randint(100000, 999999))

#user_auth = Auth()
#random_login = user_auth.generate_login()
#random_password = user_auth.generate_password()
#print(random_login)
#print(random_password)

