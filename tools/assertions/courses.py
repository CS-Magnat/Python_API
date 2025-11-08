import allure
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
from tools.logger import get_logger

logger = get_logger("COURSES_ASSERTIONS")


@allure.step("Check update course response")
def assert_update_course_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    """
    Checks that course update response matches request data

    :param request: Original course update request
    :param response: API response with updated course data
    :raises AssertionError: If any field doesn't match
    """
    logger.info("Check update course response")
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")


@allure.step("Check course")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Checks that actual course data matches expected

    :param actual: Actual course data
    :param expected: Expected course data
    :raises AssertionError: If any field doesn't match
    """
    logger.info("Check course")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_file(actual.previewFile, expected.previewFile)
    assert_user(actual.createdByUser, expected.createdByUser)


@allure.step("Check get courses response")
def assert_get_courses_response(get_courses_response: GetCoursesResponseSchema, create_course_responses: list[CreateCourseResponseSchema]):
    """
    Checks that get courses response matches course creation responses

    :param get_courses_response: API response when requesting courses list
    :param create_course_responses: List of API responses when creating courses
    :raises AssertionError: If course data doesn't match
    """
    logger.info("Check get courses response")
    assert_length(get_courses_response.courses, create_course_responses, "courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_response.course)


@allure.step("Check create course response")
def assert_create_course_response(actual: CreateCourseRequestSchema, expected: CreateCourseResponseSchema):
    """
    Checks that course creation response matches request

    :param actual: Original course creation request
    :param expected: API response with course data
    :raises AssertionError: If any field doesn't match
    """
    logger.info("Check create course response")
    assert_equal(actual.title, expected.course.title, "title")
    assert_equal(actual.max_score, expected.course.max_score, "max_score")
    assert_equal(actual.min_score, expected.course.min_score, "min_score")
    assert_equal(actual.description, expected.course.description, "description")
    assert_equal(actual.estimated_time, expected.course.estimated_time, "estimated_time")
    assert_equal(actual.preview_file_id, expected.course.previewFile.id, "preview_file_id")
    assert_equal(actual.created_by_user_id, expected.course.createdByUser.id, "created_by_user_id")