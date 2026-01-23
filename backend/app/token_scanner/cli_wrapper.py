"""Wrapper for existing CLI token analysis tools"""
import subprocess
import json
import re
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class TokenCLIWrapper:
    """Wrapper for CLI tools at ~/.local/bin/"""

    def __init__(self):
        self.cli_path = "/home/dracarys/.local/bin"

    async def scan_token(self, token_address: str) -> Dict[str, Any]:
        """
        Run token-scan CLI and parse output

        Returns structured data about token risk analysis
        """
        try:
            result = subprocess.run(
                [f"{self.cli_path}/token-scan", token_address],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                logger.error(f"token-scan failed: {result.stderr}")
                return {"error": "Scan failed", "details": result.stderr}

            return self._parse_scan_output(result.stdout)

        except subprocess.TimeoutExpired:
            logger.error(f"token-scan timeout for {token_address}")
            return {"error": "Scan timeout"}
        except Exception as e:
            logger.error(f"Error running token-scan: {e}")
            return {"error": str(e)}

    async def get_concentration(self, token_address: str) -> Dict[str, Any]:
        """
        Run token-concentration CLI

        Returns holder concentration metrics
        """
        try:
            result = subprocess.run(
                [f"{self.cli_path}/token-concentration", token_address],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                logger.error(f"token-concentration failed: {result.stderr}")
                return {"error": "Concentration check failed"}

            return self._parse_concentration_output(result.stdout)

        except subprocess.TimeoutExpired:
            logger.error(f"token-concentration timeout for {token_address}")
            return {"error": "Timeout"}
        except Exception as e:
            logger.error(f"Error running token-concentration: {e}")
            return {"error": str(e)}

    async def get_risk_score(self, token_address: str) -> Dict[str, Any]:
        """
        Run token-risk CLI

        Returns risk scoring data
        """
        try:
            result = subprocess.run(
                [f"{self.cli_path}/token-risk", token_address],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                logger.error(f"token-risk failed: {result.stderr}")
                return {"error": "Risk check failed"}

            return self._parse_risk_output(result.stdout)

        except subprocess.TimeoutExpired:
            logger.error(f"token-risk timeout for {token_address}")
            return {"error": "Timeout"}
        except Exception as e:
            logger.error(f"Error running token-risk: {e}")
            return {"error": str(e)}

    async def get_holders(self, token_address: str) -> Dict[str, Any]:
        """
        Run token-holders CLI

        Returns top holder information
        """
        try:
            result = subprocess.run(
                [f"{self.cli_path}/token-holders", token_address],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                logger.error(f"token-holders failed: {result.stderr}")
                return {"error": "Holders check failed"}

            return self._parse_holders_output(result.stdout)

        except subprocess.TimeoutExpired:
            logger.error(f"token-holders timeout for {token_address}")
            return {"error": "Timeout"}
        except Exception as e:
            logger.error(f"Error running token-holders: {e}")
            return {"error": str(e)}

    def _parse_scan_output(self, output: str) -> Dict[str, Any]:
        """Parse token-scan CLI output"""
        # This is a placeholder - adjust based on actual CLI output format
        data = {
            "raw_output": output,
            "parsed": {}
        }

        # Try to extract JSON if present
        try:
            json_match = re.search(r'\{.*\}', output, re.DOTALL)
            if json_match:
                data["parsed"] = json.loads(json_match.group())
        except json.JSONDecodeError:
            pass

        return data

    def _parse_concentration_output(self, output: str) -> Dict[str, Any]:
        """Parse token-concentration CLI output"""
        data = {
            "concentration_score": 0.0,
            "top_holder_pct": 0.0,
            "top_10_pct": 0.0,
            "raw_output": output
        }

        # Extract concentration score
        score_match = re.search(r'Concentration Score:\s*([\d.]+)', output)
        if score_match:
            data["concentration_score"] = float(score_match.group(1))

        # Extract top holder percentage
        top_holder_match = re.search(r'Top Holder:\s*([\d.]+)%', output)
        if top_holder_match:
            data["top_holder_pct"] = float(top_holder_match.group(1))

        return data

    def _parse_risk_output(self, output: str) -> Dict[str, Any]:
        """Parse token-risk CLI output"""
        data = {
            "risk_score": 50,
            "verdict": "UNKNOWN",
            "flags": [],
            "raw_output": output
        }

        # Extract risk score
        score_match = re.search(r'Risk Score:\s*(\d+)', output)
        if score_match:
            risk_score = int(score_match.group(1))
            data["risk_score"] = risk_score

            # Determine verdict based on score
            if risk_score < 30:
                data["verdict"] = "SAFE"
            elif risk_score < 70:
                data["verdict"] = "CAUTION"
            else:
                data["verdict"] = "SCAM"

        # Extract flags
        if "high concentration" in output.lower():
            data["flags"].append("high_concentration")
        if "low liquidity" in output.lower():
            data["flags"].append("low_liquidity")
        if "new token" in output.lower():
            data["flags"].append("new_token")

        return data

    def _parse_holders_output(self, output: str) -> Dict[str, Any]:
        """Parse token-holders CLI output"""
        data = {
            "holder_count": 0,
            "top_holders": [],
            "raw_output": output
        }

        # Extract holder count
        count_match = re.search(r'Total Holders:\s*(\d+)', output)
        if count_match:
            data["holder_count"] = int(count_match.group(1))

        # Extract top holders (format: address: percentage%)
        holder_pattern = r'([A-Za-z0-9]+):\s*([\d.]+)%'
        for match in re.finditer(holder_pattern, output):
            data["top_holders"].append({
                "address": match.group(1),
                "percentage": float(match.group(2))
            })

        return data


# Global instance
cli_wrapper = TokenCLIWrapper()
