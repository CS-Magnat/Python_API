import allure
from httpx import Response
from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import APIRoutes

class ExercisesClient(APIClient):
    """
    Client for working with /api/v1/exercises
    """
    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Method for getting list of exercises

        :param query: Query parameters for filtering exercises
        :return: Server response as httpx.Response object
        """
        return self.get(APIRoutes.EXERCISES, params=query)


    @allure.step("Get exercise")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Method for getting exercise by identifier

        :param exercise_id: Exercise identifier
        :return: Server response as httpx.Response object
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")


    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Method for creating exercise

        :param request: Data for creating exercise
        :return: Server response as httpx.Response object
        """
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))


    @allure.step("Update exercise")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Method for updating exercise

        :param exercise_id: Exercise identifier
        :param request: Data for updating exercise
        :return: Server response as httpx.Response object
        """
        return self.patch(f"{APIRoutes.EXERCISES}/{exercise_id}",json=request.model_dump(by_alias=True))


    @allure.step("Delete exercise")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Method for deleting exercise

        :param exercise_id: Exercise identifier
        :return: Server response as httpx.Response object
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")



    def get_exercises(self, query: GetExercisesQuerySchema):
        """
        Gets list of exercises and returns them as JSON

        :param query: Query parameters for filtering exercises
        :return: List of exercises in JSON format
        """
        response = self.get_exercises_api(query)
        return response.json()


    def get_exercise(self, exercise_id: str) -> GetExercisesResponseSchema:
        """
        Gets exercise by identifier and returns validated schema

        :param exercise_id: Exercise identifier
        :return: Validated response schema GetExercisesResponseSchema
        """
        response = self.get_exercise_api(exercise_id)
        return GetExercisesResponseSchema.model_validate_json(response.text)


    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Creates exercise and returns validated response schema

        :param request: Data for creating exercise
        :return: Validated response schema CreateExerciseResponseSchema
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)


    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema):
        """
        Updates exercise and returns response as JSON

        :param exercise_id: Exercise identifier
        :param request: Data for updating exercise
        :return: Server response in JSON format
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


    def delete_exercise(self, exercise_id: str):
        """
        Deletes exercise and returns response as JSON

        :param exercise_id: Exercise identifier
        :return: Server response in JSON format
        """
        response = self.delete_exercise_api(exercise_id)
        return response.json()


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Creates an instance of ExercisesClient with pre-configured HTTP client

    :param user: AuthenticationUserSchema object with user email and password
    :return: Ready-to-use ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))