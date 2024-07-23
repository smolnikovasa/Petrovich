import allure
import requests

from api_methods import ApiMethods

BASE_URL = "https://petstore.swagger.io/v2/user/"
API_METODS = ApiMethods()

@allure.parent_suite("Пользователи")
@allure.suite("1111111")
@allure.feature("2222")
class TestAPI:
    @allure.title("Авторизация")
    def test_login(self):
        with allure.step("Авторизация"):
            params = {
                "username": "api_key",
                "password": "special-key"
            }
            url = f"{BASE_URL}login"
            status_code = API_METODS.send_get(url, params)
            API_METODS.test_get_code(status_code, 200)


    @allure.title("Создание списка пользователей")
    def test_create_with_list(self):
        list_users = [
            {
                "id": 0,
                "username": "string",
                "firstName": "string",
                "lastName": "string",
                "email": "string",
                "password": "string",
                "phone": "string",
                "userStatus": 0
            }
        ]
        url = f"{BASE_URL}createWithList"
        status_code = API_METODS.send_post(url, list_users)
        API_METODS.test_get_code(status_code, 200)

    def test_update_booking(auth_token, booking_id):
        payload = {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 150,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-02-01"
            },
            "additionalneeds": "Lunch"
        }
        token = {"Cookie": f"token={auth_token}"}

        response = requests.put(f'{BASE_URL}/{booking_id}', json=payload, headers=token)
        assert response.status_code == 200
        response_2 = requests.get(f'{BASE_URL}/{booking_id}')
        print(response_2.json())
        assert response_2.json()["additionalneeds"] == "Lunch"


    def test_patch_booking(auth_token, booking_id):
        payload = {
            "totalprice": 15000,
            "additionalneeds": "Обед"
        }
        token = {"Cookie": f"token={auth_token}"}

        response = requests.patch(f'{BASE_URL}/{booking_id}', json=payload, headers=token)
        assert response.status_code == 200
        response_2 = requests.get(f'{BASE_URL}/{booking_id}')
        print(response_2.json())
        assert response_2.json()["additionalneeds"] == "Обед"
        assert response_2.json()["totalprice"] == 15000


    def test_delete_booking(booking_id, auth_token):
        token = {"Cookie": f"token={auth_token}"}
        response = requests.delete(f'{BASE_URL}/{booking_id}', headers=token)
        assert response.status_code == 201
        response_get = requests.get(f'{BASE_URL}/{booking_id}')
        assert response_get.status_code == 404
