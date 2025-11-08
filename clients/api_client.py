from typing import Any
from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles
import allure




class APIClient:
    """
    Base client for making HTTP requests to API

    Provides methods for executing GET, POST, PATCH and DELETE requests
    using httpx.Client
    """
    def __init__(self, client: Client):
        """
        Initializes APIClient with HTTP client

        :param client: Instance of httpx.Client for making requests
        """
        self.client = client


    @allure.step("Make GET request to {url}")
    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Executes GET request

        :param url: Endpoint URL
        :param params: GET request parameters (e.g., ?key=value)
        :return: Response object with response data
        """
        return self.client.get(url, params=params)


    @allure.step("Make POST request to {url}")
    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """
        Executes POST request

        :param url: Endpoint URL
        :param json: Data in JSON format
        :param data: Formatted form data (e.g., application/x-www-form-urlencoded)
        :param files: Files to upload to the server
        :return: Response object with response data
        """
        return self.client.post(url, json=json, data=data, files=files)


    @allure.step("Make PATCH request to {url}")
    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Executes PATCH request (partial data update)

        :param url: Endpoint URL
        :param json: Data for update in JSON format
        :return: Response object with response data
        """
        return self.client.patch(url, json=json)


    @allure.step("Make DELETE request to {url}")
    def delete(self, url: URL | str) -> Response:
        """
        Executes DELETE request (data deletion)

        :param url: Endpoint URL
        :return: Response object with response data
        """
        return self.client.delete(url)