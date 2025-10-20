from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema



class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercises_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        return self.patch(f"/api/v1/exercises/{exercise_id}",json=request.model_dump(by_alias=True))

    def delete_exercises_api(self, exercise_id: str) -> Response:
        return self.delete(f"/api/v1/exercises/{exercise_id}")



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
        response = self.update_exercises_api(exercise_id, request)
        return response.json()

    def delete_exercise(self, exercise_id: str):
        response = self.delete_exercises_api(exercise_id)
        return response.json()

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))