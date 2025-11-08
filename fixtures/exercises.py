import pytest
from pydantic import BaseModel
from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture




class ExerciseFixture(BaseModel):
    """
    Фикстура для хранения данных упражнения.

    Содержит запрос на создание упражнения и ответ от сервера.
    """
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    """
    Создает клиент для работы с упражнениями с аутентификацией пользователя.

    :param function_user: Фикстура пользователя для аутентификации
    :return: Настроенный клиент для работы с упражнениями
    """
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(function_course: CourseFixture, exercises_client: ExercisesClient) -> ExerciseFixture:
    """
    Фикстура для создания упражнения в рамках тестовой функции.

    :param function_course: Фикстура курса, к которому привязано упражнение.
    :param exercises_client: Клиент для работы с упражнениями.
    :return: Фикстура с данными созданного упражнения.
    """
    request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)