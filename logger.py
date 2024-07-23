import logging
import os
import sys
from datetime import datetime

LOGGER_PATH = os.path.normpath(os.path.dirname(__file__))


class Logger:
    """Логирование."""
    def __init__(self, worker_name: str):
        self.worker_name = worker_name

    @staticmethod
    def get_logger(logger_name="default_log"):
        """Получить базовый логгер."""
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        return logger
