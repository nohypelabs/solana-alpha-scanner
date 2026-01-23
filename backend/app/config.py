"""Configuration management"""
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Solana RPC
    SOLANA_RPC_URL: str = "https://api.mainnet-beta.solana.com"
    HELIUS_API_KEY: str = ""
    HELIUS_RPC_URL: str = ""

    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./solana_alpha.db"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # API
    BACKEND_PORT: int = 8000
    FRONTEND_URL: str = "http://localhost:3000"
    CORS_ORIGINS: str = "http://localhost:3000"

    # External APIs
    DEXSCREENER_API_URL: str = "https://api.dexscreener.com/latest"
    JUPITER_API_URL: str = "https://quote-api.jup.ag/v6"
    BIRDEYE_API_KEY: str = ""
    BIRDEYE_API_URL: str = "https://public-api.birdeye.so"

    # Stripe
    STRIPE_SECRET_KEY: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""

    # Smart Money Tracker
    SMART_MONEY_UPDATE_INTERVAL: int = 300  # 5 minutes
    MIN_WALLET_VOLUME_SOL: float = 100.0
    LEADERBOARD_SIZE: int = 100

    # Token Scanner
    RISK_SCORE_CACHE_TTL: int = 3600  # 1 hour
    MAX_SCANS_FREE_TIER: int = 100

    class Config:
        env_file = ".env"
        case_sensitive = True

    @property
    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]

    @property
    def helius_rpc(self) -> str:
        """Get Helius RPC URL with API key"""
        if self.HELIUS_API_KEY:
            return f"https://mainnet.helius-rpc.com/?api-key={self.HELIUS_API_KEY}"
        return self.HELIUS_RPC_URL or self.SOLANA_RPC_URL

settings = Settings()
