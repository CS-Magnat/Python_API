import pytest
from pydantic import BaseModel
from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture




class CourseFixture(BaseModel):
    """
    Fixture for storing course data

    Contains course creation request and server response
    """
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    """
    Fixture for creating courses client with user authentication

    :param function_user: User fixture for authentication
    :return: Configured CoursesClient for working with courses
    """
    return get_courses_client(function_user.authentication_user)


@pytest.fixture
def function_course(courses_client: CoursesClient, function_user: UserFixture, function_file: FileFixture) -> CourseFixture:
    """
    Fixture for creating course within test function

    :param courses_client: Client for working with courses
    :param function_user: User fixture creating the course
    :param function_file: File fixture for course preview
    :return: Fixture with created course data
    """
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)