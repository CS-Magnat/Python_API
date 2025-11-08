import pytest
from pydantic import BaseModel
from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture




class CourseFixture(BaseModel):
    """
    Фикстура для хранения данных курса.

    Содержит запрос на создание курса и ответ от сервера.
    """
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    """
    Фикстура для создания клиента курсов с аутентификацией пользователя.

    :param function_user: Фикстура пользователя для аутентификации.
    :return: Настроенный CoursesClient для работы с курсами.
    """
    return get_courses_client(function_user.authentication_user)


@pytest.fixture
def function_course(courses_client: CoursesClient, function_user: UserFixture, function_file: FileFixture) -> CourseFixture:
    """
    Фикстура для создания курса в рамках тестовой функции.

    :param courses_client: Клиент для работы с курсами.
    :param function_user: Фикстура пользователя, создающего курс.
    :param function_file: Фикстура файла для превью курса.
    :return: Фикстура с данными созданного курса.
    """
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)