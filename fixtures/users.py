import pytest
from pydantic import BaseModel, EmailStr
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client, PrivateUsersClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema




class UserFixture(BaseModel):
    """
    Fixture for storing user data

    Contains user creation request and server response
    Provides properties for accessing email, password and authentication_user
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
    Fixture for creating public users client

    :return: Configured PublicUsersClient for working with public endpoints
    """
    return get_public_users_client()


@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    """
    Fixture for creating user within test function

    :param public_users_client: Public client for creating user
    :return: Fixture with created user data
    """
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)


@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    """
    Fixture for creating private users client with authentication

    :param function_user: User fixture for authentication
    :return: Configured PrivateUsersClient with authentication
    """
    return get_private_users_client(function_user.authentication_user)

