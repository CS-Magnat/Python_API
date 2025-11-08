import allure
from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.logger import get_logger

logger = get_logger("ERRORS_ASSERTIONS")


@allure.step("Check validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Checks that validation error object matches expected value

    :param actual: Actual error
    :param expected: Expected error
    :raises AssertionError: If field values don't match
    """
    logger.info("Check validation error")
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")


@allure.step("Check validation error response")
def assert_validation_error_response(
        actual: ValidationErrorResponseSchema,
        expected: ValidationErrorResponseSchema
):
    """
    Checks that API response object with validation errors (ValidationErrorResponseSchema) matches expected value

    :param actual: Actual API response
    :param expected: Expected API response
    :raises AssertionError: If field values don't match
    """
    logger.info("Check validation error response")
    assert_length(actual.details, expected.details, "details")
    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)


@allure.step("Check internal error response")
def assert_internal_error_response(
        actual: InternalErrorResponseSchema,
        expected: InternalErrorResponseSchema
):
    """
    Checks internal error, for example 404 error (File not found)

    :param actual: Actual API response
    :param expected: Expected API response
    :raises AssertionError: If field values don't match
    """
    logger.info("Check internal error response")
    assert_equal(actual.details, expected.details, "details")


