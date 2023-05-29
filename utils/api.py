from utils.http_method import Http_method


"""" Методи для тестування API """
base_url = "https://qauto2.forstudy.space/api"

class UserRegister():
   # метод для створення нової юзера (або нових даних старого юзера)
    @staticmethod
    def create_new_user():

        json_for_new_user= {
            "name": "Jn",
            "lastName": "Du",
            "email": "test333@test.com",
            "password": "Qwerty1234589",
            "repeatPassword": "Qwerty1234589"
            }

        post_resource = "/auth/signup"  # ресурс методу post
        post_url = base_url + post_resource
        print(post_url)
        result_post= Http_method.post(post_url, json_for_new_user)
        print(result_post.text)
        return result_post


    @staticmethod
    def signin_new_user():

        json_for_signin_user= {
            "email": "test@test.com",
            "password": "Qwerty12345",
            "remember": False
            }

        post_resource = "/auth/signin"  # ресурс методу post
        post_url = base_url + post_resource
        print(post_url)
        result_post= Http_method.post(post_url, json_for_signin_user)
        print(result_post.text)
        return result_post


     # метод для перевірки нового юзера
    @staticmethod
    def get_new_user(user_id):

        get_resource = "/users/current"  # Ресурс метода Get
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_method.get(get_url)
        print(result_get.text)
        return result_get

        # метод для зміни даних юзера
    @staticmethod
    def put_edit_user(user_id):
        put_resource = "/users/profile"  # Ресурс метода Put
        put_url = base_url + put_resource
        print(put_url)
        json_for_update = {
            "photo": "user-1621352948859.jpg",
            "name": "John",
            "lastName": "Dou",
            "dateBirth": "2021-03-17T15:21:05.000Z",
            "country": "Ukraine"
            }
        result_put = Http_method.put(put_url, json_for_update)
        print(result_put.text)
        return result_put

    # метод для видалення юзера
    @staticmethod
    def delete_new_user(user_id):
        delete_resource = "/users"  # Ресурс метода Delete
        put_url = base_url + delete_resource
        print(put_url)
        json_for_delete = {
            "user_id": user_id
        }
        result_delete = Http_method.delete(put_url, json_for_delete)
        print(result_delete.text)
        return result_delete

