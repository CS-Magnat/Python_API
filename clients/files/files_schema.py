from pydantic import BaseModel, HttpUrl, Field, FilePath
from tools.fakers import fake




class FileSchema(BaseModel):
    """
    File structure description
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str



class CreateFileRequestSchema(BaseModel):
    """
    File creation request structure description
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: FilePath



class CreateFileResponseSchema(BaseModel):
    """
    File creation response structure description
    """
    file: FileSchema



class GetFileResponseSchema(BaseModel):
    """
    Get file request structure description
    """
    file: FileSchema