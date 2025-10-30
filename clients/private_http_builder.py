from pydantic import BaseModel, EmailStr
from httpx import Client

from clients.authentication.authentication_client import get_authentication_client
# Импортируем модель LoginRequestSchema
from clients.authentication.authentication_schema import LoginRequestSchema
from functools import lru_cache  # Импортируем функцию для кеширования

# Импортируем хуки логирования запроса и ответа
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook # Импортируем event hook

from config import settings  # Импортируем настройки




# Добавили суффикс Schema вместо Dict
class AuthenticationUserSchema(BaseModel, frozen=True):  # Добавили параметр frozen=True \ Структура данных пользователя для авторизации # Наследуем от BaseModel вместо TypedDict
    email: str
    password: str


# Создаем private builder
@lru_cache(maxsize=None)  # Кешируем возвращаемое значение
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Инициализируем AuthenticationClient для аутентификации
    authentication_client = get_authentication_client()

    # Инициализируем запрос на аутентификацию
    # Используем модель LoginRequestSchema
    # Значения теперь извлекаем не по ключу, а через атрибуты
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    # Выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=settings.http_client.timeout,  # Используем значение таймаута из настроек
        base_url=settings.http_client.client_url,  # Используем значение адреса сервера из настроек
        headers = {"Authorization": f"Bearer {login_response.token.access_token}"}, # Добавляем заголовок авторизации / Значения теперь извлекаем не по ключу, а через атрибуты
        event_hooks = {
            "request": [curl_event_hook, log_request_event_hook],  # Логируем исходящие HTTP-запросы # Добавляем event hook для запрос
            "response": [log_response_event_hook]  # Логируем полученные HTTP-ответы
        }
    )


