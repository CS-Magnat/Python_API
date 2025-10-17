from http import HTTPStatus

import pytest
import allure  # Импортируем allure
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import PublicUsersClient
from allure_commons.types import Severity  # Импортируем enum Severity из Allure
from clients.users.users_schema import CreateUserRequestSchema
from fixtures.users import UserFixture  # Заменяем импорт
from tools.allure.tags import AllureTag  # Импортируем enum с тегами
from tools.allure.epics import AllureEpic  # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature  # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory  # Импортируем enum AllureStory
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema

@pytest.mark.authentication
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHENTICATION)  # Добавили теги
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.AUTHENTICATION)  # Добавили feature
@allure.parent_suite(AllureEpic.LMS)  # allure.parent_suite == allure.epic
@allure.suite(AllureFeature.AUTHENTICATION)  # allure.suite == allure.feature
class TestAuthentication:
    @allure.story(AllureStory.LOGIN)  # Добавили story
    @allure.sub_suite(AllureStory.LOGIN)  # allure.sub_suite == allure.story
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    @allure.title("Login with correct email and password")  # Добавили заголовок
    def test_login(
            self,
            function_user: UserFixture,  # Используем фикстуру для создания пользователя
            public_users_client: PublicUsersClient,
            authentication_client: AuthenticationClient
    ):

        # Запрос на логин (login_request -> request)
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        # Выполняем логин (login_response -> response)
        response = authentication_client.login_api(request)
        # Валидация ответа (login_response_data -> response_data)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())