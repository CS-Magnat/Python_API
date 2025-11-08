import pytest
from pydantic import BaseModel
from clients.files.files_client import get_files_client, FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from config import settings
from fixtures.users import UserFixture




class FileFixture(BaseModel):
    """
    Фикстура для хранения данных файла.

    Содержит запрос на создание файла и ответ от сервера.
    """
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema


@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    """
    Фикстура для создания клиента файлов с аутентификацией пользователя.

    :param function_user: Фикстура пользователя для аутентификации.
    :return: Настроенный FilesClient для работы с файлами.
    """
    return get_files_client(function_user.authentication_user)


@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    """
    Фикстура для создания файла в рамках тестовой функции.

    :param files_client: Клиент для работы с файлами.
    :return: Фикстура с данными созданного файла.
    """
    request = CreateFileRequestSchema(upload_file=settings.test_data.image_png_file)
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)