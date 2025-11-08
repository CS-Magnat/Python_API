from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class CourseSchema(BaseModel):
    """
    Course structure description
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    previewFile: FileSchema
    estimated_time: str = Field(alias="estimatedTime")
    createdByUser: UserSchema


class GetCoursesResponseSchema(BaseModel):
    """
    Get courses list response structure description
    """
    courses: list[CourseSchema]


class GetCoursesQuerySchema(BaseModel):
    """
    Get courses list request structure description
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class CreateCourseResponseSchema(BaseModel):
    """
    Course creation response structure description
    """
    course: CourseSchema


class CreateCourseRequestSchema(BaseModel):
    """
    Course creation request structure description
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)


class UpdateCourseRequestSchema(BaseModel):
    """
    Course update request structure description
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateCourseResponseSchema(BaseModel):
    """
    Course update response structure description
    """
    course: CourseSchema


