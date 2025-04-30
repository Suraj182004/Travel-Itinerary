from app.database.models import Base
from app.database.session import engine
import logging

logger = logging.getLogger(__name__)

def setup_database():
    """Create all tables in the database"""
    try:
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        raise

if __name__ == "__main__":
    setup_database() 