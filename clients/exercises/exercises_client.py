from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client


class GetExercisesQueryDict(TypedDict):
    courseId: str

class GetExercisesResponseDict(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class AuthenticationUserDict(TypedDict):  # Структура данных пользователя для авторизации
    email: str
    password: str


class CreateExercisesRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExercisesRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"/api/v1/exercises{exercise_id}")

    def create_exercises_api(self, request: CreateExercisesRequestDict) -> Response:
        return self.post("/api/v1/exercises", json=request)

    def update_exercises_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        return self.patch(f"/api/v1/exercises{exercise_id}",json=request)

    def deleted_exercises_api(self, exercise_id: str) -> Response:
        return self.delete(f"/api/v1/exercises{exercise_id}")



    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExercisesResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExercisesRequestDict) -> GetExercisesResponseDict:
        response = self.create_exercises_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestDict) -> GetExercisesResponseDict:
        response = self.update_exercises_api(exercise_id, request)
        return response.json()

    def deleted_exercise(self, exercise_id: str) -> str:
        response = self.deleted_exercises_api(exercise_id)
        return response.json()

def get_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))