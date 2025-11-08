import logging


def get_logger(name: str) -> logging.Logger:
    """
    Создает и настраивает логгер с указанным именем.

    Настраивает логгер с уровнем DEBUG, добавляет обработчик для вывода
    в консоль с форматированием: время, имя логгера, уровень и сообщение.

    :param name: Имя логгера.
    :return: Настроенный объект logging.Logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger