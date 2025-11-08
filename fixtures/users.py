import pytest
from pydantic import BaseModel, EmailStr
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client, PrivateUsersClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema




class UserFixture(BaseModel):
    """
    Фикстура для хранения данных пользователя.

    Содержит запрос на создание пользователя и ответ от сервера.
    Предоставляет свойства для доступа к email, password и authentication_user.
    """
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema


    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    """
    Фикстура для создания публичного клиента пользователей.

    :return: Настроенный PublicUsersClient для работы с публичными эндпоинтами.
    """
    return get_public_users_client()


@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    """
    Фикстура для создания пользователя в рамках тестовой функции.

    :param public_users_client: Публичный клиент для создания пользователя.
    :return: Фикстура с данными созданного пользователя.
    """
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)


@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    """
    Фикстура для создания приватного клиента пользователей с аутентификацией.

    :param function_user: Фикстура пользователя для аутентификации.
    :return: Настроенный PrivateUsersClient с аутентификацией.
    """
    return get_private_users_client(function_user.authentication_user)

