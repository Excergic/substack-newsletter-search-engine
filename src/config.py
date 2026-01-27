import os
from typing import ClassVar

import yaml
from pydantic import BaseModel, Field, SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


# Supabase Databse Design

class SupabaseDBSettings(BaseModel):
    table_name: str = Field(default="substack_articles", description="Supabase table name")
    host: str = Field(default="localhost", description="Database host")
    name: str = Field(default="postgres", description="Database name")
    user: str = Field(default="postgres", description="Database user")
    password: SecretStr = Field(default=SecretStr("password"), description="Database password")
    port: int = Field(default=6543, description="Database port")
    test_