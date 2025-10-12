from http import HTTPStatus

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
import allure  # Импортируем библиотеку allure
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture  # Заменяем импорт
# Импортируем функцию для валидации JSON Schema
from tools.assertions.schema import validate_json_schema
# Импортируем функцию проверки статус-кода
from tools.assertions.base import assert_status_code
# Импортируем функцию для проверки ответа создания юзера
from tools.assertions.users import assert_create_user_response, assert_get_user_response
import pytest  # Импортируем библиотеку pytest

from tools.fakers import fake


@pytest.mark.users  # Добавили маркировку users
@pytest.mark.regression  # Добавили маркировку regression
class TestUsers:
    @pytest.mark.parametrize('email', ["mail.ru", "gmail.com", "example.com"])
    @allure.title("Create user")  # Добавляем человекочитаемый заголовок
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):# Используем фикстуру API клиента

        # Формируем тело запроса на создание пользователя
        request = CreateUserRequestSchema(email=fake.email(email))
        # Отправляем запрос на создание пользователя
        response = public_users_client.create_user_api(request)
        # Инициализируем модель ответа на основе полученного JSON в ответе
        # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
        response_data = CreateUserResponseSchema.model_validate_json(response.text)


        # Используем функцию для проверки статус-кода
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Используем функцию для проверки ответа создания юзера
        assert_create_user_response(request, response_data)
        # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get user me")  # Добавляем человекочитаемый заголовок
    def test_get_user_me(self, private_users_client: PrivateUsersClient, function_user: UserFixture):

        response_user_me_api = private_users_client.get_user_me_api()
        response_user_me_api_data = GetUserResponseSchema.model_validate_json(response_user_me_api.text)

        assert_status_code(response_user_me_api.status_code, HTTPStatus.OK)
        assert_get_user_response(GetUserResponseSchema.model_validate_json(response_user_me_api.text), function_user.response)
        validate_json_schema(response_user_me_api.json(), response_user_me_api_data.model_json_schema())