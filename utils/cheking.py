"""  Методи для перевірки наших запитів"""
from requests import Response
import json

class Checking():

    """ Метод для перевірки статус коду"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Успішно! статус код = " + str(response.status_code))
        else:
            print("Халепа! статус код = " + str(response.status_code))


