import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, GetExercisesResponseDictSchema
from clients.private_http_builder import AuthenticationUserSchema
from fixtures.courses import CourseFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: GetExercisesResponseDictSchema


@pytest.fixture
def exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return get_exercises_client(user)

@pytest.fixture
def function_exercise(function_course: CourseFixture, exercises_client: ExercisesClient) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)