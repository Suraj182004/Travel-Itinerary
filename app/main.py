from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
import os
import logging

from app.config import settings
from app.api.endpoints import router as api_router
from app.mcp.server import router as mcp_router
from app.database.models import Base
from app.database.session import engine, SessionLocal

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router, prefix=f"{settings.API_PREFIX}/v1")
app.include_router(mcp_router, prefix=f"{settings.API_PREFIX}/v1/mcp")

# Create database tables
Base.metadata.create_all(bind=engine)

# Setup database with seed data if needed
def setup_database():
    from app.database.models import Trip
    
    # Check if we need to seed the database
    db = SessionLocal()
    try:
        # Check if data exists
        existing_trips = db.query(Trip).count()
        if existing_trips == 0:
            logger.info("No data found in database. Seeding with initial data...")
            # Import here to avoid circular imports
            from data.seed_data import seed_database
            seed_database()
            logger.info("Database seeded successfully!")
        else:
            logger.info(f"Database already contains {existing_trips} trips. Skipping seed operation.")
    except Exception as e:
        logger.error(f"Error checking/seeding database: {e}")
    finally:
        db.close()

# Run database setup on startup in production
if os.environ.get("RENDER") or os.environ.get("PRODUCTION"):
    logger.info("Production environment detected. Setting up database...")
    setup_database()

@app.get("/")
def read_root():
    return {
        "app": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "documentation": "/docs"
    }

# Endpoint to manually trigger database setup (can be password protected in production)
@app.post("/setup-db")
def setup_db_endpoint():
    setup_database()
    return {"message": "Database setup completed"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)