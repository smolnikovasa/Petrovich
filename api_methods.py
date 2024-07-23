import allure
import datetime

import requests

from conftest import get_logger

logger = get_logger()


class ApiMethods:
    def send_get(self, url, params):
        with allure.step(f"Выполнить GET запрос к ресурсу: {url}"):
            response = requests.get(url, params=params)

        self.logger_write(response)
        self.attach_allure_report()

        return response.status_code

    def send_post(self, url, body):
        logger.info(f"Body: {body}")

        with allure.step(f"Выполнить POST запрос к ресурсу: {url}"):
            response = requests.post(url, json=body)

        self.logger_write(response)
        self.attach_allure_report()

        return response.status_code

    def logger_write(self, response):
        if response.status_code != 200:
            logger.error(f"Status code: {response.status_code}, Response: {response.json()}")
        else:
            logger.info(f"Response: {response.json()}")

    def test_get_code(self, fact_status_code, expected_status_code):
        with allure.step(f"Выполнить проверку: стутас код = {expected_status_code}"):
            assert fact_status_code == expected_status_code

    def attach_allure_report(self):
        allure.attach.file("my-log.txt", f"лог от {datetime.datetime.now()}", allure.attachment_type.JSON)
