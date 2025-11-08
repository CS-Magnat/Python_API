from typing import Any, Sized
import allure
from tools.logger import get_logger

logger = get_logger("BASE_ASSERTIONS")



@allure.step("Check that response status code equals to {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Checks that actual response status code matches expected

    :param actual: Actual response status code
    :param expected: Expected status code
    :raises AssertionError: If status codes don't match
    """
    logger.info(f"Check that response status code equals to {expected}")
    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )



@allure.step("Check that {name} equals to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    """
    Checks that actual value equals expected

    :param name: Name of the value being checked
    :param actual: Actual value
    :param expected: Expected value
    :raises AssertionError: If actual value doesn't equal expected
    """

    logger.info(f'Check that "{name}" equals to {expected}')
    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected value: {expected}. '
        f'Actual value: {actual}'
    )



@allure.step("Check that {name} is true")
def assert_is_true(actual: Any, name: str):
    """
    Checks that actual value is true

    :param name: Name of the value being checked
    :param actual: Actual value
    :raises AssertionError: If actual value is false
    """

    logger.info(f'Check that "{name}" is true')
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Checks that lengths of two objects match

    :param name: Name of the object being checked
    :param actual: Actual object
    :param expected: Expected object
    :raises AssertionError: If lengths don't match
    """
    with allure.step(f"Check that length of {name} equals to {len(expected)}"):
        logger.info(f'Check that length of "{name}" equals to {len(expected)}')

        assert len(actual) == len(expected), (
            f'Incorrect object length: "{name}". '
            f'Expected length: {len(expected)}. '
            f'Actual length: {len(actual)}'
        )