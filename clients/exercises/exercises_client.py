from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQueryDictSchema, CreateExercisesRequestDictSchema, \
    UpdateExercisesRequestDictSchema, GetExercisesResponseDictSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema



class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQueryDictSchema) -> Response:
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"/api/v1/exercises{exercise_id}")

    def create_exercises_api(self, request: CreateExercisesRequestDictSchema) -> Response:
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercises_api(self, exercise_id: str, request: UpdateExercisesRequestDictSchema) -> Response:
        return self.patch(f"/api/v1/exercises{exercise_id}",json=request.model_dump(by_alias=True))

    def deleted_exercises_api(self, exercise_id: str) -> Response:
        return self.delete(f"/api/v1/exercises{exercise_id}")



    def get_exercises(self, query: GetExercisesQueryDictSchema) -> GetExercisesResponseDictSchema:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExercisesResponseDictSchema:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExercisesRequestDictSchema) -> GetExercisesResponseDictSchema:
        response = self.create_exercises_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestDictSchema) -> GetExercisesResponseDictSchema:
        response = self.update_exercises_api(exercise_id, request)
        return response.json()

    def deleted_exercise(self, exercise_id: str) -> str:
        response = self.deleted_exercises_api(exercise_id)
        return response.json()

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))