from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine

from app.config import settings
from app.api.endpoints import router as api_router
from app.mcp.server import router as mcp_router
from app.database.models import Base
from app.database.session import engine

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

@app.get("/")
def read_root():
    return {
        "app": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "documentation": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)