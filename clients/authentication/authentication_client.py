from httpx import Response
from clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
from clients.api_client import APIClient
import allure
from clients.public_http_builder import get_public_http_client
from tools.routes import APIRoutes


class AuthenticationClient(APIClient):
    """
    Client for working with /api/v1/authentication
    """
    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Method for authenticating user

        :param request: Dictionary with email and password
        :return: Server response as httpx.Response object
        """
        return self.post(
            f"{APIRoutes.AUTHENTICATION}/login",
            json=request.model_dump(by_alias=True)
        )


    @allure.step("Refresh authentication token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Method for refreshing authorization token

        :param request: Dictionary with refreshToken
        :return: Server response as httpx.Response object
        """
        return self.post(
            f"{APIRoutes.AUTHENTICATION}/refresh",
            json=request.model_dump(by_alias=True)
        )


    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """
        Authenticates user and returns validated response schema

        :param request: Authentication data (email and password)
        :return: Validated response schema LoginResponseSchema with tokens
        """
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """
    Creates an instance of AuthenticationClient with pre-configured HTTP client

    :return: Ready-to-use AuthenticationClient
    """
    return AuthenticationClient(client=get_public_http_client())
