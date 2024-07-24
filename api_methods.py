import allure
import requests

from base_data import METHOD_GET, METHOD_POST, METHOD_PUT, METHOD_DELETE


class ApiMethods:
    def __init__(self, logger):
        self.logger = logger

    def send_requests(self, name_method, url, body=None, params=None):
        method = {
            METHOD_GET: requests.get(url, params=params),
            METHOD_POST: requests.post(url, json=body),
            METHOD_PUT: requests.put(url, json=body),
            METHOD_DELETE: requests.delete(url),
        }

        with allure.step(f"Выполнить {name_method} запрос к ресурсу: {url}"):
            response = method[name_method]

        self.logger.info(f"Выполнен запрос к ресурсу: {url}, методом: {name_method}")
        self.logger_write_response(response)

        return response.status_code

    def logger_write_response(self, response):
        log_text = f"Получен ответ от сервера: Status code - {response.status_code}, Response - {response.json()}"
        if response.status_code != 200:
            self.logger.error(log_text)
        else:
            self.logger.info(log_text)

    @staticmethod
    def assert_code(fact_status_code, expected_status_code):
        with allure.step(f"Выполнить проверку: стутас код = {expected_status_code}"):
            assert fact_status_code == expected_status_code
