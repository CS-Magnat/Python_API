import allure

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseResponseSchema, UpdateExerciseRequestSchema, \
    GetExercisesListResponseSchema, GetExercisesResponseSchema, ExercisesSchema, ExerciseSchema
from tools.assertions.base import assert_equal, assert_is_true, assert_length
from tools.assertions.errors import assert_internal_error_response

@allure.step("Check create exercise response")
def assert_create_exercise_response(actual: CreateExerciseRequestSchema, expected: CreateExerciseResponseSchema):
    assert_equal(actual.title, expected.exercise.title, "title")
    assert_equal(actual.course_id, expected.exercise.course_id, "course_id")
    assert_equal(actual.max_score, expected.exercise.max_score, "max_score")
    assert_equal(actual.min_score, expected.exercise.min_score, "min_score")
    assert_equal(actual.order_index, expected.exercise.order_index, "order_index")
    assert_equal(actual.description, expected.exercise.description, "description")
    assert_equal(actual.estimated_time, expected.exercise.estimated_time, "estimated_time")
    # Проверяем, что в ответе есть ID (которого не было в запросе)
    assert_is_true(expected.exercise.id is not None, "exercise.id should not be None")

# def assert_exercise(actual: GetExerciseResponseSchema, expected: CreateExerciseResponseSchema):
#     assert_equal(actual.exercise.title, expected.exercise.title, "title")
#     assert_equal(actual.exercise.course_id, expected.exercise.course_id, "course_id")
#     assert_equal(actual.exercise.max_score, expected.exercise.max_score, "max_score")
#     assert_equal(actual.exercise.min_score, expected.exercise.min_score, "min_score")
#     assert_equal(actual.exercise.order_index, expected.exercise.order_index, "order_index")
#     assert_equal(actual.exercise.description, expected.exercise.description, "description")
#     assert_equal(actual.exercise.estimated_time, expected.exercise.estimated_time, "estimated_time")

@allure.step("Check cexercise")
def assert_exercise(actual: ExercisesSchema, expected: ExerciseSchema):

    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

@allure.step("Check update exercise response")
def assert_update_exercise_response(actual: UpdateExerciseResponseSchema, expected: UpdateExerciseRequestSchema):
    assert_equal(actual.exercise.title, expected.title, "title")
    #assert_equal(actual.exercise.course_id, expected.exercise.course_id, "course_id")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")

@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)

#@allure.step("Check get exercise response")
# def assert_get_exercise_response(actual: GetExerciseResponseSchema, expected: CreateExerciseResponseSchema):
#     assert_exercise(actual, expected)  #задание части 3, не совсем понятно зачем надо и без него работает

@allure.step("Check get exercises response")
def assert_get_exercises_response(actual: GetExercisesListResponseSchema, expected: list[CreateExerciseResponseSchema]):
    assert_length(actual.exercises, expected, "courses")
    for index, expected_exercise in enumerate(expected):
        assert_exercise(actual.exercises[index], expected_exercise.exercise)