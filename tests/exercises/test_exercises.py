from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import GetExercisesResponseSchema, CreateExerciseRequestSchema, \
    CreateExerciseResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.users_schema import CreateUserRequestSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:

    def test_create_exercise(self, function_course: CourseFixture, function_user: UserFixture):
        exercises_client = get_exercises_client(function_user.authentication_user)

        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)

        create_exercise_response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(create_exercise_response.text)
        assert_status_code(create_exercise_response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)