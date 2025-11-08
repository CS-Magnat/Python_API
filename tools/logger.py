import logging


def get_logger(name: str) -> logging.Logger:
    """
    Creates and configures logger with specified name

    Configures logger with DEBUG level, adds handler for console output
    with formatting: time, logger name, level and message

    :param name: Logger name
    :return: Configured logging.Logger object
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger