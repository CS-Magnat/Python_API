from httpx import Response
# Добавили импорт моделей
from clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
from clients.api_client import APIClient
import allure  # Импортируем allure
from clients.public_http_builder import get_public_http_client # Импортируем builder
from tools.routes import APIRoutes  # Импортируем enum APIRoutes


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    @allure.step("Authenticate user")  # Добавили allure шаг
    # Теперь используем pydantic-модель для аннотации
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        # Вместо /api/v1/authentication используем APIRoutes.AUTHENTICATION
        return self.post(
            f"{APIRoutes.AUTHENTICATION}/login",
            # Сериализуем модель в словарь с использованием alias
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Refresh authentication token")  # Добавили allure шаг
    # Теперь используем pydantic-модель для аннотации
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        # Вместо /api/v1/authentication используем APIRoutes.AUTHENTICATION
        return self.post(
            f"{APIRoutes.AUTHENTICATION}/refresh",
            # Сериализуем модель в словарь с использованием alias
            json=request.model_dump(by_alias=True)
        )

    # Теперь используем pydantic-модель для аннотации
    # Добавили метод login
    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)  # Отправляем запрос на аутентификацию
        # Инициализируем модель через валидацию JSON строки
        return LoginResponseSchema.model_validate_json(response.text)

# Добавляем builder для AuthenticationClient
def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
