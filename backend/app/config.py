"""
Configuration module for FFLIQ backend.
Loads environment variables from a .env file (if present) and provides typed configuration settings
for the FastAPI app.
"""
from typing import Optional, List
import os
from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Settings(BaseSettings):
    """
    Application configuration settings loaded from environment variables.
    """
    # Database settings
    DATABASE_URL: str = Field(
        default="postgresql://ffliq_user:ffliq_pass@db:5432/ffliq"
    )
    
    # Security settings
    SECRET_KEY: str = Field(default="dev-secret-key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60)
    
    # Application settings
    DEBUG: bool = Field(default=False)
    API_PREFIX: str = "/api"
    
    # AI settings
    OPENAI_API_KEY: Optional[str] = None
    USE_LOCAL_LLM: bool = Field(default=True)
    LOCAL_LLM_URL: Optional[str] = None
    
    # CORS settings
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",  # Frontend development server
        "http://localhost:8000",  # Backend development server
    ]
    
    class Config:
        case_sensitive = True
        env_file = ".env"

# Create settings instance
settings = Settings()