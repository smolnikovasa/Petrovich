import allure

from api_methods import ApiMethods
from base_data import dict_user, BASE_URL, LOGIN, PASSWORD, METHOD_POST, METHOD_GET, METHOD_PUT, METHOD_DELETE
from values.users_dto import UserDTO
from conftest import get_logger

logger = get_logger()
API_METHODS = ApiMethods(logger)


@allure.parent_suite("Пользователи")
@allure.title("Авторизация")
def test_login():
    with allure.step("Авторизация"):
        params = {
            "username": LOGIN,
            "password": PASSWORD,
        }
        API_METHODS.assert_code(API_METHODS.send_requests(METHOD_GET, f"{BASE_URL}/login", params=params), 200)


@allure.parent_suite("Пользователи")
@allure.title("Выход из системы")
def test_logout():
    with allure.step("Выйти из системы"):
        API_METHODS.assert_code(API_METHODS.send_requests(METHOD_GET, f"{BASE_URL}/logout"), 200)


@allure.parent_suite("Пользователи")
@allure.title("Создание списка пользователей")
def test_create_list_user():
    API_METHODS.assert_code(
        API_METHODS.send_requests(METHOD_POST, f"{BASE_URL}/createWithList", [dict_user(UserDTO())] * 3), 200
    )


@allure.parent_suite("Пользователи")
@allure.title("Получение данных пользователя")
def test_get_user_info(username):
    API_METHODS.assert_code(API_METHODS.send_requests(METHOD_GET, f"{BASE_URL}/{username}"), 200)


@allure.parent_suite("Пользователи")
@allure.title("Обновление данных пользователя")
def test_update_user(username):
    user_dto = UserDTO()
    user_dto.username = username

    API_METHODS.assert_code(API_METHODS.send_requests(METHOD_PUT, f"{BASE_URL}/{username}", dict_user(user_dto)), 200)


@allure.parent_suite("Пользователи")
@allure.title("Удаление поьзователя")
def test_delete_user(username):
    API_METHODS.assert_code(
        API_METHODS.send_requests(METHOD_DELETE, f"{BASE_URL}/{username}", params=f"'username': '{username}'"), 200
    )
