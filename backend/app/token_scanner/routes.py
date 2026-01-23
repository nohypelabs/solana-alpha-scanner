"""Token Scanner API routes"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

from .analyzer import token_analyzer
from ..database import get_db
from ..models import TokenScan, User

router = APIRouter()


class ScanRequest(BaseModel):
    """Token scan request"""
    token_address: str = Field(..., min_length=32, max_length=44)
    wallet_address: Optional[str] = None


class ScanResponse(BaseModel):
    """Token scan response"""
    token_address: str
    symbol: str
    name: str
    risk_score: int
    verdict: str
    metrics: dict
    top_holders: List[dict]
    flags: dict
    recommendation: str
    scanned_at: str


class ScanHistoryItem(BaseModel):
    """Scan history item"""
    id: int
    token_address: str
    symbol: Optional[str]
    name: Optional[str]
    risk_score: int
    verdict: str
    scanned_at: datetime


@router.post("/token", response_model=ScanResponse, status_code=status.HTTP_200_OK)
async def scan_token(
    request: ScanRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Scan a token for risk analysis

    Free tier: Unlimited scans
    Pro/Whale: Same scans, just faster access to other features
    """
    try:
        # Perform analysis
        analysis = await token_analyzer.analyze_token(request.token_address)

        if "error" in analysis:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=analysis.get("details", "Analysis failed")
            )

        # Save to database
        user_id = None
        if request.wallet_address:
            # Try to find or create user
            stmt = select(User).where(User.wallet_address == request.wallet_address)
            result = await db.execute(stmt)
            user = result.scalar_one_or_none()

            if not user:
                user = User(wallet_address=request.wallet_address)
                db.add(user)
                await db.flush()

            user_id = user.id

        # Create scan record
        scan = TokenScan(
            user_id=user_id,
            token_address=analysis["token_address"],
            symbol=analysis.get("symbol"),
            name=analysis.get("name"),
            risk_score=analysis["risk_score"],
            verdict=analysis["verdict"],
            holder_count=analysis["metrics"].get("holder_count"),
            top_holder_pct=analysis["metrics"].get("top_holder_pct"),
            liquidity_usd=analysis["metrics"].get("liquidity_usd"),
            market_cap_usd=analysis["metrics"].get("market_cap_usd"),
            concentration_score=analysis["metrics"].get("concentration_score"),
            flags=analysis["flags"]
        )
        db.add(scan)
        await db.commit()

        return ScanResponse(**analysis)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Scan failed: {str(e)}"
        )


@router.get("/history", response_model=List[ScanHistoryItem])
async def get_scan_history(
    wallet_address: str,
    limit: int = 20,
    db: AsyncSession = Depends(get_db)
):
    """
    Get scan history for a wallet

    Returns recent scans for authenticated user
    """
    try:
        # Find user
        stmt = select(User).where(User.wallet_address == wallet_address)
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()

        if not user:
            return []

        # Get scan history
        stmt = (
            select(TokenScan)
            .where(TokenScan.user_id == user.id)
            .order_by(desc(TokenScan.scanned_at))
            .limit(limit)
        )
        result = await db.execute(stmt)
        scans = result.scalars().all()

        return [
            ScanHistoryItem(
                id=scan.id,
                token_address=scan.token_address,
                symbol=scan.symbol,
                name=scan.name,
                risk_score=scan.risk_score,
                verdict=scan.verdict,
                scanned_at=scan.scanned_at
            )
            for scan in scans
        ]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get history: {str(e)}"
        )


@router.get("/stats")
async def get_scan_stats(db: AsyncSession = Depends(get_db)):
    """
    Get global scan statistics

    Returns total scans, common verdicts, etc.
    """
    try:
        # Total scans
        stmt = select(TokenScan)
        result = await db.execute(stmt)
        all_scans = result.scalars().all()

        total_scans = len(all_scans)
        safe_count = len([s for s in all_scans if s.verdict == "SAFE"])
        caution_count = len([s for s in all_scans if s.verdict == "CAUTION"])
        scam_count = len([s for s in all_scans if s.verdict == "SCAM"])

        return {
            "total_scans": total_scans,
            "verdicts": {
                "safe": safe_count,
                "caution": caution_count,
                "scam": scam_count
            },
            "safe_percentage": round((safe_count / total_scans * 100) if total_scans > 0 else 0, 2)
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get stats: {str(e)}"
        )
