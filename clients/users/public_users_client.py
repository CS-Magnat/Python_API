from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient

class UserRequestDict(TypedDict):

        email: str
        password: str
        lastName: str
        firstName: str
        middleName: str


class PublicUsersClient(APIClient):

    def create_user_api(self, request: UserRequestDict) -> Response:
        return self.post("/api/v1/users", json=request)