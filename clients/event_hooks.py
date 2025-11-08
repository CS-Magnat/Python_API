import allure
from httpx import Request, Response
from tools.http.curl import make_curl_from_request
from tools.logger import get_logger

logger = get_logger("HTTP_CLIENT")



def curl_event_hook(request: Request):
    """
    Event hook for automatically attaching cURL command to Allure report

    :param request: HTTP request passed to `httpx` client
    """
    curl_command = make_curl_from_request(request)
    allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)


def log_request_event_hook(request: Request):
    """
    Logs information about sent HTTP request

    :param request: HTTPX request object
    """
    logger.info(f'Make {request.method} request to {request.url}')


def log_response_event_hook(response: Response):
    """
    Logs information about received HTTP response

    :param response: HTTPX response object
    """
    logger.info(
        f"Got response {response.status_code} {response.reason_phrase} from {response.url}"
    )