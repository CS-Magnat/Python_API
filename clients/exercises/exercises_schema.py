from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake



class ExercisesSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class ExerciseSchema(BaseModel):
    """Схема для одного упражнения"""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    course_id: str = Field(alias = "courseId")


class GetExercisesListResponseSchema(BaseModel):
    """Схема для получения списка упражнений"""
    model_config = ConfigDict(populate_by_name=True)
    exercises: list[ExercisesSchema]


class GetExerciseResponseSchema(BaseModel):
    """Схема для получения одного упражнения"""
    exercise: ExerciseSchema
"""Обе схемы ссылаются на одну ExerciseSchema, потому что и создание, и получение упражнения возвращают 
одинаковую структуру данных - одно упражнение с теми же полями."""

class CreateExerciseResponseSchema(BaseModel):
    """Схема ответа создания упражнения"""
    exercise: ExerciseSchema
"""Обе схемы ссылаются на одну ExerciseSchema, потому что и создание, и получение упражнения возвращают 
одинаковую структуру данных - одно упражнение с теми же полями."""


class CreateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema