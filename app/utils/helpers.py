import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Travel Itinerary API"
    PROJECT_VERSION: str = "1.0.0"
    
    # Database configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./travel_itinerary.db")
    
    # CORS configuration
    CORS_ORIGINS: list = ["*"]
    
    # API configuration
    API_PREFIX: str = "/api"
    
    class Config:
        env_file = ".env"

settings = Settings()