from enum import Enum


class APIRoutes(str, Enum):
    """
    API routes enumeration

    Contains all base paths to API endpoints
    """
    USERS = "/api/v1/users"
    FILES = "/api/v1/files"
    COURSES = "/api/v1/courses"
    EXERCISES = "/api/v1/exercises"
    AUTHENTICATION = "/api/v1/authentication"

    def __str__(self):
        """
        Returns route value as string

        :return: API route value
        """
        return self.value