"""Main token analysis logic"""
from typing import Dict, Any
import logging
from datetime import datetime

from .cli_wrapper import cli_wrapper
from ..solana_client import solana_client

logger = logging.getLogger(__name__)


class TokenAnalyzer:
    """Comprehensive token analysis combining CLI tools and RPC data"""

    async def analyze_token(self, token_address: str) -> Dict[str, Any]:
        """
        Full token analysis combining multiple data sources

        Returns complete risk analysis with verdict
        """
        try:
            # Get data from multiple sources in parallel
            metadata = await solana_client.get_token_metadata(token_address)
            concentration = await cli_wrapper.get_concentration(token_address)
            risk_data = await cli_wrapper.get_risk_score(token_address)
            holders_data = await cli_wrapper.get_holders(token_address)

            # Combine all data
            analysis = {
                "token_address": token_address,
                "symbol": metadata.get("symbol") if metadata else "UNKNOWN",
                "name": metadata.get("name") if metadata else "Unknown Token",
                "scanned_at": datetime.utcnow().isoformat(),
            }

            # Risk scoring
            risk_score = risk_data.get("risk_score", 50)
            verdict = self._calculate_verdict(risk_score, concentration, holders_data)

            analysis["risk_score"] = risk_score
            analysis["verdict"] = verdict

            # Metrics
            analysis["metrics"] = {
                "holder_count": holders_data.get("holder_count", 0),
                "top_holder_pct": concentration.get("top_holder_pct", 0.0),
                "liquidity_usd": metadata.get("liquidity_usd", 0.0) if metadata else 0.0,
                "market_cap_usd": metadata.get("market_cap_usd", 0.0) if metadata else 0.0,
                "concentration_score": concentration.get("concentration_score", 0.0),
                "volume_24h": metadata.get("volume_24h", 0.0) if metadata else 0.0,
            }

            # Top holders
            analysis["top_holders"] = holders_data.get("top_holders", [])[:10]

            # Flags
            analysis["flags"] = self._generate_flags(
                concentration,
                analysis["metrics"],
                risk_data
            )

            # Recommendation
            analysis["recommendation"] = self._generate_recommendation(
                verdict,
                analysis["flags"]
            )

            return analysis

        except Exception as e:
            logger.error(f"Error analyzing token {token_address}: {e}")
            return {
                "error": "Analysis failed",
                "details": str(e),
                "token_address": token_address
            }

    def _calculate_verdict(
        self,
        risk_score: int,
        concentration: Dict[str, Any],
        holders: Dict[str, Any]
    ) -> str:
        """Calculate final verdict based on all metrics"""

        # Adjust risk score based on concentration
        top_holder_pct = concentration.get("top_holder_pct", 0.0)
        if top_holder_pct > 50:
            risk_score += 20
        elif top_holder_pct > 30:
            risk_score += 10

        # Adjust based on holder count
        holder_count = holders.get("holder_count", 0)
        if holder_count < 100:
            risk_score += 15
        elif holder_count < 500:
            risk_score += 5

        # Final verdict
        if risk_score < 30:
            return "SAFE"
        elif risk_score < 70:
            return "CAUTION"
        else:
            return "SCAM"

    def _generate_flags(
        self,
        concentration: Dict[str, Any],
        metrics: Dict[str, Any],
        risk_data: Dict[str, Any]
    ) -> Dict[str, bool]:
        """Generate warning flags"""
        return {
            "high_concentration": concentration.get("top_holder_pct", 0.0) > 20,
            "low_liquidity": metrics.get("liquidity_usd", 0.0) < 10000,
            "low_holder_count": metrics.get("holder_count", 0) < 500,
            "new_token": "new_token" in risk_data.get("flags", []),
            "suspicious_pattern": "suspicious" in risk_data.get("raw_output", "").lower(),
        }

    def _generate_recommendation(
        self,
        verdict: str,
        flags: Dict[str, bool]
    ) -> str:
        """Generate human-readable recommendation"""
        if verdict == "SCAM":
            return "AVOID - High risk of scam or rug pull"

        elif verdict == "CAUTION":
            warnings = []
            if flags.get("high_concentration"):
                warnings.append("high holder concentration")
            if flags.get("low_liquidity"):
                warnings.append("low liquidity")
            if flags.get("low_holder_count"):
                warnings.append("few holders")

            if warnings:
                return f"CAUTION - {', '.join(warnings)}"
            return "CAUTION - Moderate risk detected"

        else:  # SAFE
            return "SAFE - Token appears legitimate, but always DYOR"


# Global instance
token_analyzer = TokenAnalyzer()
