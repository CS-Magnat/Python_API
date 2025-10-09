from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import GetExercisesResponseDictSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:

    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        create_exercise_response = exercises_client.get_exercise_api(function_course.response.course.id)
        response_data = GetExercisesResponseDictSchema.model_validate_json(create_exercise_response.text)
        assert_status_code(create_exercise_response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(create_exercise_response.json(), response_data.model_json_schema())