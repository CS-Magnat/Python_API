import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture

# Модель для агрегации возвращаемых данных фикстурой function_exercise
# удобный способ объединить запрос и ответ для упражнения в тестах
class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema # Схема запроса создания упражнения
    response: CreateExerciseResponseSchema # Схема ответа с данными упражнения

# Создаем новый API клиент для работы с упражнениями
@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:  # Изменено с user на function_user
    return get_exercises_client(function_user.authentication_user)

# Используем фикстуры function_course и exercises_client для создания упражнения
@pytest.fixture
def function_exercise(function_course: CourseFixture, exercises_client: ExercisesClient) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(course_id=function_course.response.course.id) # Создаем запрос на создание упражнения с course_id из фикстуры курса
    response = exercises_client.create_exercise(request) # Выполняем запрос создания упражнения через API клиент
    return ExerciseFixture(request=request, response=response)