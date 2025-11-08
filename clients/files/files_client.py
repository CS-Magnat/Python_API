from httpx import Response
from clients.api_client import APIClient
import allure
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from tools.routes import APIRoutes




class FilesClient(APIClient):
    """
    Client for working with /api/v1/files
    """

    @allure.step("Get file by id {file_id}")
    def get_file_api(self, file_id: str) -> Response:
        """
        Method for getting file

        :param file_id: File identifier
        :return: Server response as httpx.Response object
        """
        return self.get(f"{APIRoutes.FILES}/{file_id}")


    @allure.step("Create file")
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Method for creating file

        :param request: Dictionary with filename, directory, upload_file
        :return: Server response as httpx.Response object
        """
        return self.post(
            APIRoutes.FILES,
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={"upload_file": request.upload_file.read_bytes()}
        )


    @allure.step("Delete file by id {file_id}")
    def delete_file_api(self, file_id: str) -> Response:
        """
        Method for deleting file

        :param file_id: File identifier
        :return: Server response as httpx.Response object
        """
        return self.delete(f"{APIRoutes.FILES}/{file_id}")


    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Creates file and returns validated response schema

        :param request: Data for creating file
        :return: Validated response schema CreateFileResponseSchema
        """
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)



def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Creates an instance of FilesClient with pre-configured HTTP client

    :return: Ready-to-use FilesClient
    """
    return FilesClient(client=get_private_http_client(user))




