from http import HTTPStatus

import pytest
import allure  # Импортируем allure
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import GetExerciseResponseSchema, CreateExerciseRequestSchema, \
    CreateExerciseResponseSchema, UpdateExerciseResponseSchema, UpdateExerciseRequestSchema, GetExercisesQuerySchema, \
    GetExercisesResponseSchema, GetExercisesListResponseSchema
from allure_commons.types import Severity  # Импортируем enum Severity из Allure

from httpx_get_user import get_user_response_data
from tools.allure.epics import AllureEpic  # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature  # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory  # Импортируем enum AllureStory
from tools.allure.tags import AllureTag  # Импортируем enum с тегами
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.users_schema import CreateUserRequestSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.errors import assert_internal_error_response
from tools.assertions.exercises import assert_create_exercise_response, assert_exercise, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)  # Добавили теги
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.EXERCISES)  # Добавили feature
@allure.parent_suite(AllureEpic.LMS)  # allure.parent_suite == allure.epic
@allure.suite(AllureFeature.EXERCISES)  # allure.suite == allure.feature
class TestExercises:
    @allure.tag(AllureTag.CREATE_ENTITY)  # Добавили тег
    @allure.story(AllureStory.CREATE_ENTITY)  # Добавили story
    @allure.sub_suite(AllureStory.CREATE_ENTITY)  # allure.sub_suite == allure.story
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    @allure.title("Create exercise")  # Добавили заголовок
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
    #def test_create_exercise(self, function_exercise: ExerciseFixture):
        #assert_create_exercise_response(function_exercise.request, function_exercise.response)

        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)

        create_exercise_response = exercises_client.create_exercise_api(request)

        response_data = CreateExerciseResponseSchema.model_validate_json(create_exercise_response.text)
        assert_status_code(create_exercise_response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)
        validate_json_schema(create_exercise_response.json(), response_data.model_json_schema())


    @allure.tag(AllureTag.GET_ENTITY)  # Добавили тег
    @allure.story(AllureStory.GET_ENTITY)  # Добавили story
    @allure.sub_suite(AllureStory.GET_ENTITY)  # allure.sub_suite == allure.story
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    @allure.title("Get exercise")  # Добавили заголовок
    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):

        get_exercise_response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        get_exercise_response_data = GetExerciseResponseSchema.model_validate_json(get_exercise_response.text)

        assert_status_code(get_exercise_response.status_code, HTTPStatus.OK)
        assert_exercise(get_exercise_response_data.exercise, function_exercise.response.exercise) #перепроверить, по факту сравниваем схемы, зачем, если проверку они проходят при трансфармации в схему
        validate_json_schema(get_exercise_response.json(), get_exercise_response_data.model_json_schema())



    @allure.tag(AllureTag.UPDATE_ENTITY)  # Добавили тег
    @allure.story(AllureStory.UPDATE_ENTITY)  # Добавили story
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)  # allure.sub_suite == allure.story
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    @allure.title("Update exercise")  # Добавили заголовок
    def test_update_exercise( self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):

        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(function_exercise.response.exercise.id, request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        assert_update_exercise_response(response_data,request)
        validate_json_schema(response.json(), GetExerciseResponseSchema.model_json_schema())



    @allure.tag(AllureTag.DELETE_ENTITY)  # Добавили тег
    @allure.story(AllureStory.DELETE_ENTITY)  # Добавили story
    @allure.sub_suite(AllureStory.DELETE_ENTITY)  # allure.sub_suite == allure.story
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    @allure.title("Delete exercise")  # Добавили заголовок
    def test_delete_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):

        delete_response = exercises_client.delete_exercise_api(function_exercise.response.exercise.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)

        get_user_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_exercise_not_found_response(get_user_response_data)

        validate_json_schema(get_response.json(), InternalErrorResponseSchema.model_json_schema())



    @allure.tag(AllureTag.GET_ENTITIES)  # Добавили тег
    @allure.story(AllureStory.GET_ENTITIES)  # Добавили story
    @allure.sub_suite(AllureStory.GET_ENTITIES)  # allure.sub_suite == allure.story
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    @allure.title("Get exercises")  # Добавили заголовок
    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture,
            function_exercise: ExerciseFixture
    ):


        query = GetExercisesQuerySchema(course_id=function_course.response.course.id)
        get_response = exercises_client.get_exercises_api(query.model_dump(by_alias=True))
        get_response_data = GetExercisesListResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.OK)

        assert_get_exercises_response(get_response_data, [function_exercise.response])
        validate_json_schema(get_response.json(), GetExercisesListResponseSchema.model_json_schema())







