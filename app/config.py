import os

class Settings:
    PROJECT_NAME: str = "Travel Itinerary API"
    PROJECT_VERSION: str = "1.0.0"
    
    # Database configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./travel_itinerary.db")
    
    # Fix for PostgreSQL URLs in Render (they start with postgres:// instead of postgresql://)
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    
    # CORS configuration
    CORS_ORIGINS: list = ["*"]
    
    # API configuration
    API_PREFIX: str = "/api"

settings = Settings()
