import allure
from httpx import Response
from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import APIRoutes

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Параметры запроса для фильтрации упражнений.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(APIRoutes.EXERCISES, params=query)

    @allure.step("Get exercise")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения по идентификатору.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Сreate exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания упражнения.

        :param request: Данные для создания упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    @allure.step("Greate exercises")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Данные для обновления упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"{APIRoutes.EXERCISES}/{exercise_id}",json=request.model_dump(by_alias=True))

    @allure.step("Delete exercises")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")



    def get_exercises(self, query: GetExercisesQuerySchema):
        """
        Получает список упражнений и возвращает их в виде JSON.

        :param query: Параметры запроса для фильтрации упражнений.
        :return: Список упражнений в формате JSON.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExercisesResponseSchema:
        """
        Получает упражнение по идентификатору и возвращает валидированную схему.

        :param exercise_id: Идентификатор упражнения.
        :return: Валидированная схема ответа GetExercisesResponseSchema.
        """
        response = self.get_exercise_api(exercise_id)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Создает упражнение и возвращает валидированную схему ответа.

        :param request: Данные для создания упражнения.
        :return: Валидированная схема ответа CreateExerciseResponseSchema.
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema):
        """
        Обновляет упражнение и возвращает ответ в виде JSON.

        :param exercise_id: Идентификатор упражнения.
        :param request: Данные для обновления упражнения.
        :return: Ответ от сервера в формате JSON.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

    def delete_exercise(self, exercise_id: str):
        """
        Удаляет упражнение и возвращает ответ в виде JSON.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в формате JSON.
        """
        response = self.delete_exercise_api(exercise_id)
        return response.json()

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))