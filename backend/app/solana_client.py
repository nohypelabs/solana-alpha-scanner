"""Solana RPC client wrapper"""
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Confirmed
from solders.pubkey import Pubkey
from typing import Optional, Dict, Any
import logging
import httpx

from .config import settings

logger = logging.getLogger(__name__)


class SolanaClient:
    """Wrapper for Solana RPC operations"""

    def __init__(self):
        self.rpc_url = settings.helius_rpc
        self.client = AsyncClient(self.rpc_url, commitment=Confirmed)
        self.http_client = httpx.AsyncClient(timeout=30.0)

    async def get_token_supply(self, token_address: str) -> Optional[int]:
        """Get token total supply"""
        try:
            pubkey = Pubkey.from_string(token_address)
            response = await self.client.get_token_supply(pubkey)
            if response.value:
                return int(response.value.amount)
            return None
        except Exception as e:
            logger.error(f"Error getting token supply for {token_address}: {e}")
            return None

    async def get_token_accounts(self, token_address: str) -> Optional[list]:
        """Get all token accounts for a token"""
        try:
            pubkey = Pubkey.from_string(token_address)
            response = await self.client.get_token_accounts_by_owner(
                pubkey,
                {"programId": Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA")}
            )
            if response.value:
                return response.value
            return []
        except Exception as e:
            logger.error(f"Error getting token accounts for {token_address}: {e}")
            return []

    async def get_account_balance(self, wallet_address: str) -> Optional[float]:
        """Get SOL balance of a wallet"""
        try:
            pubkey = Pubkey.from_string(wallet_address)
            response = await self.client.get_balance(pubkey)
            if response.value is not None:
                return response.value / 1e9  # Convert lamports to SOL
            return None
        except Exception as e:
            logger.error(f"Error getting balance for {wallet_address}: {e}")
            return None

    async def get_token_metadata(self, token_address: str) -> Optional[Dict[str, Any]]:
        """Get token metadata from DexScreener"""
        try:
            url = f"{settings.DEXSCREENER_API_URL}/dex/tokens/{token_address}"
            response = await self.http_client.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get("pairs"):
                    pair = data["pairs"][0]
                    return {
                        "symbol": pair.get("baseToken", {}).get("symbol"),
                        "name": pair.get("baseToken", {}).get("name"),
                        "price_usd": float(pair.get("priceUsd", 0)),
                        "liquidity_usd": float(pair.get("liquidity", {}).get("usd", 0)),
                        "market_cap_usd": float(pair.get("fdv", 0)),
                        "volume_24h": float(pair.get("volume", {}).get("h24", 0)),
                    }
            return None
        except Exception as e:
            logger.error(f"Error getting token metadata for {token_address}: {e}")
            return None

    async def get_wallet_transactions(
        self,
        wallet_address: str,
        limit: int = 100
    ) -> list:
        """Get recent transactions for a wallet"""
        try:
            pubkey = Pubkey.from_string(wallet_address)
            response = await self.client.get_signatures_for_address(
                pubkey,
                limit=limit
            )
            if response.value:
                return response.value
            return []
        except Exception as e:
            logger.error(f"Error getting transactions for {wallet_address}: {e}")
            return []

    async def get_helius_parsed_transactions(
        self,
        wallet_address: str,
        limit: int = 100
    ) -> Optional[list]:
        """Get parsed transactions from Helius API"""
        if not settings.HELIUS_API_KEY:
            logger.warning("Helius API key not configured")
            return None

        try:
            url = f"https://api.helius.xyz/v0/addresses/{wallet_address}/transactions"
            params = {
                "api-key": settings.HELIUS_API_KEY,
                "limit": limit
            }
            response = await self.http_client.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            logger.error(f"Error getting Helius transactions for {wallet_address}: {e}")
            return None

    async def close(self):
        """Close connections"""
        await self.client.close()
        await self.http_client.aclose()


# Global client instance
solana_client = SolanaClient()
