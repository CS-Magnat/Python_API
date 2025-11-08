import pytest
from pydantic import BaseModel
from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture




class ExerciseFixture(BaseModel):
    """
    Fixture for storing exercise data

    Contains exercise creation request and server response
    """
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    """
    Creates client for working with exercises with user authentication

    :param function_user: User fixture for authentication
    :return: Configured client for working with exercises
    """
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(function_course: CourseFixture, exercises_client: ExercisesClient) -> ExerciseFixture:
    """
    Fixture for creating exercise within test function

    :param function_course: Course fixture to which exercise is bound
    :param exercises_client: Client for working with exercises
    :return: Fixture with created exercise data
    """
    request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)