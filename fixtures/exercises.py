import pytest

from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.private_http_builder import AuthenticationUserSchema


@pytest.fixture
def exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return get_exercises_client(user)

@pytest.fixture
def function_exercise(function_course):
    pass