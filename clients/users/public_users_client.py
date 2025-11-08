from httpx import Response
from clients.api_client import APIClient
import allure
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema
from tools.routes import APIRoutes




class PublicUsersClient(APIClient):
    """
    Client for working with /api/v1/users
    """
    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Method for creating user

        :param request: Dictionary with email, password, lastName, firstName, middleName
        :return: Server response as httpx.Response object
        """
        return self.post(APIRoutes.USERS, json=request.model_dump(by_alias=True))


    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Creates user and returns validated response schema

        :param request: Data for creating user
        :return: Validated response schema CreateUserResponseSchema
        """
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Creates an instance of PublicUsersClient with pre-configured HTTP client

    :return: Ready-to-use PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())