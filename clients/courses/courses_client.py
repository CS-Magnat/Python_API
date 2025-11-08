from httpx import Response
from clients.api_client import APIClient
import allure
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, \
    CreateCourseResponseSchema, UpdateCourseRequestSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from tools.routes import APIRoutes



class CoursesClient(APIClient):
    """
    Client for working with /api/v1/courses
    """
    @allure.step("Get courses")
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Method for getting list of courses

        :param query: Dictionary with userId
        :return: Server response as httpx.Response object
        """
        return self.get(APIRoutes.COURSES, params=query.model_dump(by_alias=True))


    @allure.step("Get course by id {course_id}")
    def get_course_api(self, course_id: str) -> Response:
        """
        Method for getting course

        :param course_id: Course identifier
        :return: Server response as httpx.Response object
        """
        return self.get(f"{APIRoutes.COURSES}/{course_id}")


    @allure.step("Create course")
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Method for creating course

        :param request: Dictionary with title, maxScore, minScore, description, estimatedTime, 
        previewFileId, createdByUserId
        :return: Server response as httpx.Response object
        """
        return self.post(APIRoutes.COURSES, json=request.model_dump(by_alias=True))


    @allure.step("Update course by id {course_id}")
    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Method for updating course

        :param course_id: Course identifier
        :param request: Dictionary with title, maxScore, minScore, description, estimatedTime
        :return: Server response as httpx.Response object
        """
        return self.patch(
            f"{APIRoutes.COURSES}/{course_id}",
            json=request.model_dump(by_alias=True)
        )


    @allure.step("Delete course by id {course_id}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        Method for deleting course

        :param course_id: Course identifier
        :return: Server response as httpx.Response object
        """
        return self.delete(f"{APIRoutes.COURSES}/{course_id}")


    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Creates course and returns validated response schema

        :param request: Data for creating course
        :return: Validated response schema CreateCourseResponseSchema
        """
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Creates an instance of CoursesClient with pre-configured HTTP client

    :return: Ready-to-use CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user))