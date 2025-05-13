"""
Main FastAPI application for FFLIQ backend.
Sets up app, routers, database connections, and middleware.
"""
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.db.database import get_db
from app.config import settings

# Import API routers
# These will be uncommented as they are implemented
# from app.api.users import router as users_router
# from app.api.teams import router as teams_router
# from app.api.players import router as players_router
# from app.api.leagues import router as leagues_router
# from app.api.ai import router as ai_router

# Configure logging
logging.basicConfig(
    level=logging.INFO if settings.DEBUG else logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="FFLIQ API",
    description="AI-powered fantasy football assistant API",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "ok", "version": "0.1.0"}

# Database test endpoint
@app.get("/db-test")
def db_test(db=Depends(get_db)):
    """Test database connection."""
    try:
        # Just test if we can use the session
        db.execute("SELECT 1")
        return {"status": "ok", "message": "Database connection successful"}
    except Exception as e:
        logger.error(f"Database connection error: {e}")
        return {"status": "error", "message": str(e)}

# Register routers - will be uncommented as they are implemented
# app.include_router(users_router, prefix="/api/users", tags=["users"])
# app.include_router(teams_router, prefix="/api/teams", tags=["teams"])
# app.include_router(players_router, prefix="/api/players", tags=["players"])
# app.include_router(leagues_router, prefix="/api/leagues", tags=["leagues"])
# app.include_router(ai_router, prefix="/api/ai", tags=["ai"])

# Startup and shutdown events
@app.on_event("startup")
async def startup_event():
    """Run on application startup."""
    logger.info("Starting FFLIQ API")

@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown."""
    logger.info("Shutting down FFLIQ API")