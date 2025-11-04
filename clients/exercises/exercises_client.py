import allure
from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import APIRoutes  # Импортируем enum APIRoutes
from clients.api_coverage import tracker  # Импортируем трекер

class ExercisesClient(APIClient):

    @allure.step("Get exercises")
    # Добавили сбор покрытия для эндпоинта GET /api/v1/exercises
    @tracker.track_coverage_httpx(APIRoutes.EXERCISES)
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        return self.get(APIRoutes.EXERCISES, params=query)

    @allure.step("Get exercise")
    # Добавили сбор покрытия для эндпоинта GET /api/v1/exercises/{exercise_id}
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Сreate exercise")
    # Добавили сбор покрытия для эндпоинта POST /api/v1/exercises
    @tracker.track_coverage_httpx(APIRoutes.EXERCISES)
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    @allure.step("Greate exercises")
    # Добавили сбор покрытия для эндпоинта PATCH /api/v1/exercises/{exercise_id}
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        return self.patch(f"{APIRoutes.EXERCISES}/{exercise_id}",json=request.model_dump(by_alias=True))

    @allure.step("Delete exercises")
    # Добавили сбор покрытия для эндпоинта DELETE /api/v1/exercises/{exercise_id}
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")



    def get_exercises(self, query: GetExercisesQuerySchema):
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExercisesResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema):
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

    def delete_exercise(self, exercise_id: str):
        response = self.delete_exercise_api(exercise_id)
        return response.json()

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))