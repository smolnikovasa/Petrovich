import allure
import datetime
import pytest

from base_data import METHOD_POST, BASE_URL, dict_user
from api_methods import ApiMethods
from logger import Logger
from values.users_dto import UserDTO

logger = None


def get_logger():
    """Получить базовый логгер."""
    global logger
    if logger is None:
        logger = Logger.get_logger()
    return logger


@pytest.fixture()
def username():
    user_dto = UserDTO()
    with allure.step(f"Preconditions: создание нового пользователя с логином: {user_dto.username}"):
        if ApiMethods(logger).send_requests(METHOD_POST, BASE_URL, dict_user(user_dto)) == 200:
            yield user_dto.username


@pytest.fixture(autouse=True)
def attach_allure_report():
    yield
    allure.attach.file("log.txt", f"лог от {datetime.datetime.now()}", allure.attachment_type.JSON, ".txt")
