"""FastAPI main application"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from .config import settings
from .database import init_db

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    # Startup
    logger.info("Starting Solana Alpha Scanner API...")
    await init_db()
    logger.info("Database initialized")

    yield

    # Shutdown
    logger.info("Shutting down...")


app = FastAPI(
    title="Solana Alpha Scanner API",
    description="Token Scanner + Smart Money Tracker for Solana",
    version="0.1.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "service": "Solana Alpha Scanner API",
        "version": "0.1.0"
    }


@app.get("/health")
async def health():
    """Detailed health check"""
    return {
        "status": "healthy",
        "database": "connected",
        "solana_rpc": settings.helius_rpc,
    }


# Import routers
from .token_scanner.routes import router as scanner_router
from .smart_money.routes import router as smart_money_router
# from .subscription.routes import router as subscription_router

app.include_router(scanner_router, prefix="/api/scan", tags=["Token Scanner"])
app.include_router(smart_money_router, prefix="/api/smart-money", tags=["Smart Money"])
# app.include_router(subscription_router, prefix="/api/subscription", tags=["Subscription"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.BACKEND_PORT,
        reload=True
    )
