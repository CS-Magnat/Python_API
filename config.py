from typing import Self
from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict





class HTTPClientConfig(BaseModel):
    """
    Configuration for HTTP client

    Contains URL and timeout settings for HTTP requests
    """
    url: HttpUrl
    timeout: float



    @property
    def client_url(self) -> str:
        """
        Returns client URL as string

        :return: URL address as string
        """
        return str(self.url)


class TestDataConfig(BaseModel):
    """
    Configuration for test data

    Contains paths to files used in tests
    """
    image_png_file: FilePath



class Settings(BaseSettings):
    """
    Main application settings

    Loads configuration from environment variables and .env file
    Contains settings for HTTP client, test data and Allure results directory
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
        Initializes application settings

        Creates directory for Allure results if it doesn't exist

        :return: Settings class instance with initialized settings
        """
        allure_results_dir = DirectoryPath("./allure-results")
        allure_results_dir.mkdir(exist_ok=True)

        return Settings(allure_results_dir=allure_results_dir)


settings = Settings.initialize()