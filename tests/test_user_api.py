
from utils.api import UserRegister
from requests import Response
import json
from utils.cheking import Checking

"""" Створення, зміна та видалення нової локації"""

class Test_create_user():

    def test_create_new_user(self):
        print("Метод POST")
        result_post: Response = UserRegister.create_new_user()
        check_post = result_post.json()
        user_id = check_post.get("user_id")
        # Checking.check_status_code(result_post, 200)
      
        result_post: Response = UserRegister.signin_new_user()
        check_post = result_post.json()
        user_id = check_post.get("user_id")

        print("Метод Get - перевірка методу post ")
        result_get: Response = UserRegister.get_new_user(user_id)
        # Checking.check_status_code(result_get, 200)

        print("Метод PUT")
        result_put: Response = UserRegister.put_edit_user(user_id)
        # Checking.check_status_code(result_put, 200)

        print("Метод Get-перевірка методу PUT")
        result_get: Response = UserRegister.get_new_user(user_id)
        # Checking.check_status_code(result_get, 200)

        print("Метод DELETE")
        result_delete: Response = UserRegister.delete_new_user(user_id)
        # Checking.check_status_code(result_delete, 200)

        print("Метод Get-перевірка методу Delete")
        result_get: Response = UserRegister.get_new_user(user_id)
        # Checking.check_status_code(result_get, 200)


