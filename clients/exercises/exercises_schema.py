from pydantic import BaseModel, Field, EmailStr, ConfigDict


class GetExercisesQueryDictSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias = "courseId")

class GetExercisesResponseDictSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class AuthenticationUserDictSchema(BaseModel):  # Структура данных пользователя для авторизации
    email: EmailStr
    password: str


class CreateExercisesRequestDictSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class UpdateExercisesRequestDictSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")