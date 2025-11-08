from typing import Self
from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict





class HTTPClientConfig(BaseModel):
    """
    Конфигурация для HTTP-клиента.

    Содержит настройки URL и таймаута для HTTP-запросов.
    """
    url: HttpUrl
    timeout: float



    @property
    def client_url(self) -> str:
        """
        Возвращает URL клиента в виде строки.

        :return: URL-адрес в формате строки.
        """
        return str(self.url)


class TestDataConfig(BaseModel):
    """
    Конфигурация для тестовых данных.

    Содержит пути к файлам, используемым в тестах.
    """
    image_png_file: FilePath



class Settings(BaseSettings):
    """
    Основные настройки приложения.

    Загружает конфигурацию из переменных окружения и .env файла.
    Содержит настройки для HTTP-клиента, тестовых данных и директории Allure результатов.
    """
    model_config = SettingsConfigDict(
        extra='allow',
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    test_data: TestDataConfig
    http_client: HTTPClientConfig
    allure_results_dir: DirectoryPath



    @classmethod
    def initialize(cls) -> Self:
        """
        Инициализирует настройки приложения.

        Создает директорию для результатов Allure, если она не существует.

        :return: Экземпляр класса Settings с инициализированными настройками.
        """
        allure_results_dir = DirectoryPath("./allure-results")
        allure_results_dir.mkdir(exist_ok=True)

        return Settings(allure_results_dir=allure_results_dir)


settings = Settings.initialize()