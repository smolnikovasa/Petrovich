import allure

from api_methods import ApiMethods
from base_data import dict_user, BASE_URL, LOGIN, PASSWORD, METHOD_POST, METHOD_GET, METHOD_PUT, METHOD_DELETE
from values.users_dto import UserDTO


@allure.parent_suite("Пользователи")
class TestUserAPI:

    @allure.title("Авторизация")
    def test_login(self, logger):
        api_method = ApiMethods(logger)
        with allure.step(f"Авториpизоваться пользователем {LOGIN}"):
            params = {
                "username": LOGIN,
                "password": PASSWORD,
            }

            api_method.assert_code(api_method.send_requests(METHOD_GET, f"{BASE_URL}/login", params=params), 200)

    @allure.title("Разлогин")
    def test_logout(self, logger):
        api_method = ApiMethods(logger)
        with allure.step("Выйти из системы"):
            api_method.assert_code(api_method.send_requests(METHOD_GET, f"{BASE_URL}/logout"), 200)

    @allure.title("Создание списка пользователей")
    def test_create_list_user(self, logger):
        api_method = ApiMethods(logger)
        api_method.assert_code(
            api_method.send_requests(METHOD_POST, f"{BASE_URL}/createWithList", [dict_user(UserDTO())] * 3), 200
        )

    @allure.title("Получение данных пользователя")
    def test_get_user_info(self, username, logger):
        api_method = ApiMethods(logger)
        api_method.assert_code(api_method.send_requests(METHOD_GET, f"{BASE_URL}/{username}"), 200)

    @allure.title("Обновление данных пользователя")
    def test_update_user(self, username, logger):
        api_method = ApiMethods(logger)
        user_dto = UserDTO()
        user_dto.username = username

        api_method.assert_code(api_method.send_requests(METHOD_PUT, f"{BASE_URL}/{username}", dict_user(user_dto)), 200)

    @allure.title("Удаление поьзователя")
    def test_delete_user(self, username, logger):
        api_method = ApiMethods(logger)
        api_method.assert_code(
            api_method.send_requests(METHOD_DELETE, f"{BASE_URL}/{username}", params=f"'username': '{username}'"),
            200,
        )
