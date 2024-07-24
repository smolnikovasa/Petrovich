import logging
import os
from logging import Formatter

LOGGER_PATH = os.path.normpath(os.path.dirname(__file__))


class Logger:
    """Логирование."""

    @staticmethod
    def get_logger(logger_name="default_log"):
        """Получить базовый логгер."""
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        filelog = logging.FileHandler("log.txt", "w", encoding="UTF-8")
        filelog.setLevel(logging.INFO)
        filelog.setFormatter(Formatter(fmt="[%(asctime)s: %(levelname)s] %(message)s"))
        logger.addHandler(filelog)
        console = logging.StreamHandler()
        console.setLevel(logging.ERROR)
        console.setFormatter(Formatter(fmt="[%(asctime)s: %(levelname)s] %(message)s"))
        logger.addHandler(console)
        return logger
