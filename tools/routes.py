from enum import Enum


class APIRoutes(str, Enum):
    """
    Перечисление маршрутов API.

    Содержит все базовые пути к эндпоинтам API.
    """
    USERS = "/api/v1/users"
    FILES = "/api/v1/files"
    COURSES = "/api/v1/courses"
    EXERCISES = "/api/v1/exercises"
    AUTHENTICATION = "/api/v1/authentication"

    def __str__(self):
        """
        Возвращает значение маршрута в виде строки.

        :return: Значение маршрута API.
        """
        return self.value