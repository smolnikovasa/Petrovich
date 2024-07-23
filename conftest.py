import allure
import datetime
import pytest

from logger import Logger

logger = None

def allure_aatach_log():
    allure.attach("my-log.txt", f"лог от {datetime.datetime.now()}", allure.attachment_type.TEXT)

def get_logger():
    """Получить базовый логгер."""
    global logger
    if logger is None:
        logger = Logger.get_logger()
    return logger
