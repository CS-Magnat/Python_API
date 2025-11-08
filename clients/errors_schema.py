from typing import Any
from pydantic import BaseModel, Field, ConfigDict




class ValidationErrorSchema(BaseModel):
    """
    Model describing API validation error structure
    """
    model_config = ConfigDict(populate_by_name=True)

    type: str
    input: Any
    context: dict[str, Any] = Field(alias="ctx")
    message: str = Field(alias="msg")
    location: list[str] = Field(alias="loc")


class ValidationErrorResponseSchema(BaseModel):
    """
    Model describing API response structure with validation error
    """
    model_config = ConfigDict(populate_by_name=True)

    details: list[ValidationErrorSchema] = Field(alias="detail")


class InternalErrorResponseSchema(BaseModel):
    """
    Model for describing internal error
    """

    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias="detail")