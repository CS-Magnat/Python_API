from pydantic import BaseModel, Field
from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    Description of authentication tokens structure
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestSchema(BaseModel):
    """
    Description of authentication request structure
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)



class LoginResponseSchema(BaseModel):
    """
    Description of authentication response structure
    """
    token: TokenSchema



class RefreshRequestSchema(BaseModel):
    """
    Description of token refresh request structure
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)