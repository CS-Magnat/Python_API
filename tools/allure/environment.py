import platform
import sys

from config import settings


def create_allure_environment_file():
    """
    Создает файл environment.properties для Allure отчета.

    Собирает информацию о настройках приложения, операционной системе
    и версии Python, затем записывает в файл environment.properties
    в директории allure-results.
    """
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]

    os_info = f'{platform.system()}, {platform.release()}'
    python_version = sys.version
    items.extend([
        f'os_info={os_info}',
        f'python_version={python_version}',
    ])

    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)