from http import HTTPStatus

import pytest
import allure  # Импортируем allure
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import GetExercisesResponseSchema, CreateExerciseRequestSchema, \
    CreateExerciseResponseSchema
from tools.allure.tags import AllureTag  # Импортируем enum с тегами
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.users_schema import CreateUserRequestSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)  # Добавили теги
class TestExercises:
    @allure.tag(AllureTag.CREATE_ENTITY)  # Добавили тег
    @allure.title("Create exercise")  # Добавили заголовок
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
    #def test_create_exercise(self, function_exercise: ExerciseFixture):
        #assert_create_exercise_response(function_exercise.request, function_exercise.response)

        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)

        create_exercise_response = exercises_client.create_exercise_api(request)

        response_data = CreateExerciseResponseSchema.model_validate_json(create_exercise_response.text)
        assert_status_code(create_exercise_response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

    @allure.tag(AllureTag.GET_ENTITY)  # Добавили тег
    @allure.title("Get exercise")  # Добавили заголовок
    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):

        get_exercise_response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)

        assert_status_code(get_exercise_response.status_code, HTTPStatus.OK)

    @allure.tag(AllureTag.UPDATE_ENTITY)  # Добавили тег
    @allure.title("Update exercise")  # Добавили заголовок
    def test_update_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        ...

    @allure.tag(AllureTag.DELETE_ENTITY)  # Добавили тег
    @allure.title("Delete exercise")  # Добавили заголовок
    def test_delete_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        ...

    @allure.tag(AllureTag.GET_ENTITIES)  # Добавили тег
    @allure.title("Get exercises")  # Добавили заголовок
    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture,
            function_exercise: ExerciseFixture
    ):
        ...

