import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, GetExercisesResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from fixtures.courses import CourseFixture

# Модель для агрегации возвращаемых данных фикстурой function_exercise
# удобный способ объединить запрос и ответ для упражнения в тестах
class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema # Схема запроса создания упражнения
    response: GetExercisesResponseSchema # Схема ответа с данными упражнения

# Создаем новый API клиент для работы с упражнениями
@pytest.fixture
def exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return get_exercises_client(user)

# Используем фикстуры function_course и exercises_client для создания упражнения
@pytest.fixture
def function_exercise(function_course: CourseFixture, exercises_client: ExercisesClient) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(course_id=function_course.response.course.id) # Создаем запрос на создание упражнения с course_id из фикстуры курса
    response = exercises_client.create_exercise(request) # Выполняем запрос создания упражнения через API клиент
    return ExerciseFixture(request=request, response=response)