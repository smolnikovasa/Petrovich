import datetime

import allure
import pytest

from api_methods import ApiMethods
from base_data import METHOD_POST, BASE_URL, dict_user
from logger import Logger
from values.users_dto import UserDTO

_logger = None


@pytest.fixture()
def logger():
    """Получить базовый логгер."""
    global _logger
    if _logger is None:
        _logger = Logger.get_logger()
    return _logger


@pytest.fixture(autouse=True)
def run_tests():
    yield
    allure.attach.file("log.txt", f"лог от {datetime.datetime.now()}", allure.attachment_type.JSON, ".txt")
    with open("log.txt", "w"):
        pass


@allure.title("Preconditions")
@pytest.fixture()
def username(logger):
    api_method = ApiMethods(logger)
    user_dto = UserDTO()

    with allure.step(f"Cоздать нового пользователя с логином: {user_dto.username}"):
        if api_method.send_requests(METHOD_POST, BASE_URL, dict_user(user_dto)) == 200:
            return user_dto.username
