"""Smart Money Tracker API routes"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc, and_
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

from .tracker import smart_money_tracker
from ..database import get_db
from ..models import SmartMoneyWallet, TrackedWallet, User, Trade

router = APIRouter()


class LeaderboardEntry(BaseModel):
    """Leaderboard entry"""
    rank: int
    wallet_address: str
    total_pnl: float
    win_rate: float
    total_trades: int
    avg_return: float
    last_30d_pnl: float


class WalletDetailsResponse(BaseModel):
    """Wallet details response"""
    wallet_address: str
    rank: Optional[int]
    total_pnl: float
    win_rate: float
    total_trades: int
    avg_return: float
    last_30d_pnl: float
    recent_activity: List[dict]


class TrackWalletRequest(BaseModel):
    """Track wallet request"""
    user_wallet: str = Field(..., description="User's wallet address")
    target_wallet: str = Field(..., description="Wallet to track")
    nickname: Optional[str] = None
    alert_on_buy: bool = True
    alert_on_sell: bool = True
    min_trade_size_sol: float = 1.0


class RecentSignal(BaseModel):
    """Recent trading signal"""
    wallet_address: str
    wallet_rank: Optional[int]
    token_address: str
    token_symbol: Optional[str]
    trade_type: str
    amount_sol: float
    timestamp: datetime


@router.get("/leaderboard", response_model=List[LeaderboardEntry])
async def get_leaderboard(
    limit: int = Query(default=100, le=500),
    db: AsyncSession = Depends(get_db)
):
    """
    Get smart money wallet leaderboard

    Free tier: Top 10 wallets
    Pro tier: Top 100 wallets
    Whale tier: Unlimited
    """
    try:
        stmt = (
            select(SmartMoneyWallet)
            .where(SmartMoneyWallet.is_active == True)
            .order_by(SmartMoneyWallet.rank)
            .limit(limit)
        )
        result = await db.execute(stmt)
        wallets = result.scalars().all()

        return [
            LeaderboardEntry(
                rank=wallet.rank or 0,
                wallet_address=wallet.wallet_address,
                total_pnl=wallet.total_pnl,
                win_rate=wallet.win_rate,
                total_trades=wallet.total_trades,
                avg_return=wallet.avg_return,
                last_30d_pnl=wallet.last_30d_pnl
            )
            for wallet in wallets
        ]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get leaderboard: {str(e)}"
        )


@router.get("/wallet/{wallet_address}", response_model=WalletDetailsResponse)
async def get_wallet_details(
    wallet_address: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Get detailed information about a specific wallet

    Returns performance metrics and recent activity
    """
    try:
        # Get wallet from database
        stmt = select(SmartMoneyWallet).where(
            SmartMoneyWallet.wallet_address == wallet_address
        )
        result = await db.execute(stmt)
        wallet = result.scalar_one_or_none()

        if not wallet:
            # Wallet not in leaderboard, try to analyze it
            metrics = await smart_money_tracker.analyze_wallet(wallet_address, db)

            if "error" in metrics:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Wallet not found or has no trading activity"
                )

            # Get recent activity
            recent_activity = await smart_money_tracker.get_wallet_recent_activity(
                wallet_address, db, limit=10
            )

            return WalletDetailsResponse(
                wallet_address=wallet_address,
                rank=None,
                total_pnl=metrics["total_pnl"],
                win_rate=metrics["win_rate"],
                total_trades=metrics["total_trades"],
                avg_return=metrics["avg_return"],
                last_30d_pnl=metrics["last_30d_pnl"],
                recent_activity=recent_activity
            )

        # Get recent activity
        recent_activity = await smart_money_tracker.get_wallet_recent_activity(
            wallet_address, db, limit=10
        )

        return WalletDetailsResponse(
            wallet_address=wallet.wallet_address,
            rank=wallet.rank,
            total_pnl=wallet.total_pnl,
            win_rate=wallet.win_rate,
            total_trades=wallet.total_trades,
            avg_return=wallet.avg_return,
            last_30d_pnl=wallet.last_30d_pnl,
            recent_activity=recent_activity
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get wallet details: {str(e)}"
        )


@router.post("/track", status_code=status.HTTP_201_CREATED)
async def track_wallet(
    request: TrackWalletRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Track a wallet for alerts

    Pro tier: Track up to 10 wallets
    Whale tier: Track unlimited wallets
    """
    try:
        # Find or create user
        stmt = select(User).where(User.wallet_address == request.user_wallet)
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()

        if not user:
            user = User(wallet_address=request.user_wallet)
            db.add(user)
            await db.flush()

        # Check if already tracking
        stmt = select(TrackedWallet).where(
            and_(
                TrackedWallet.user_id == user.id,
                TrackedWallet.wallet_address == request.target_wallet
            )
        )
        result = await db.execute(stmt)
        existing = result.scalar_one_or_none()

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Already tracking this wallet"
            )

        # Check tier limits (simplified - always allow for demo)
        # In production, check user.subscription_tier and enforce limits

        # Create tracked wallet
        tracked = TrackedWallet(
            user_id=user.id,
            wallet_address=request.target_wallet,
            nickname=request.nickname,
            alert_on_buy=request.alert_on_buy,
            alert_on_sell=request.alert_on_sell,
            min_trade_size_sol=request.min_trade_size_sol
        )
        db.add(tracked)
        await db.commit()

        return {
            "status": "success",
            "message": f"Now tracking wallet {request.target_wallet}",
            "tracked_wallet": {
                "wallet_address": tracked.wallet_address,
                "nickname": tracked.nickname,
                "added_at": tracked.added_at.isoformat()
            }
        }

    except HTTPException:
        raise
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to track wallet: {str(e)}"
        )


@router.get("/tracked", response_model=List[dict])
async def get_tracked_wallets(
    user_wallet: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Get list of wallets tracked by user

    Returns all wallets being tracked with alert settings
    """
    try:
        # Find user
        stmt = select(User).where(User.wallet_address == user_wallet)
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()

        if not user:
            return []

        # Get tracked wallets
        stmt = (
            select(TrackedWallet)
            .where(TrackedWallet.user_id == user.id)
            .order_by(desc(TrackedWallet.added_at))
        )
        result = await db.execute(stmt)
        tracked = result.scalars().all()

        return [
            {
                "id": t.id,
                "wallet_address": t.wallet_address,
                "nickname": t.nickname,
                "alert_on_buy": t.alert_on_buy,
                "alert_on_sell": t.alert_on_sell,
                "min_trade_size_sol": t.min_trade_size_sol,
                "added_at": t.added_at.isoformat(),
                "last_alert": t.last_alert.isoformat() if t.last_alert else None
            }
            for t in tracked
        ]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get tracked wallets: {str(e)}"
        )


@router.get("/signals", response_model=List[RecentSignal])
async def get_recent_signals(
    limit: int = Query(default=20, le=100),
    db: AsyncSession = Depends(get_db)
):
    """
    Get recent trading signals from smart money wallets

    Free tier: 24h delayed signals
    Pro tier: Real-time signals
    """
    try:
        # Get recent trades from top wallets
        stmt = (
            select(Trade)
            .join(SmartMoneyWallet, Trade.wallet_address == SmartMoneyWallet.wallet_address)
            .where(SmartMoneyWallet.is_active == True)
            .order_by(desc(Trade.timestamp))
            .limit(limit)
        )
        result = await db.execute(stmt)
        trades = result.scalars().all()

        # Get wallet ranks
        wallet_ranks = {}
        stmt = select(SmartMoneyWallet).where(SmartMoneyWallet.is_active == True)
        result = await db.execute(stmt)
        wallets = result.scalars().all()
        for w in wallets:
            wallet_ranks[w.wallet_address] = w.rank

        return [
            RecentSignal(
                wallet_address=trade.wallet_address,
                wallet_rank=wallet_ranks.get(trade.wallet_address),
                token_address=trade.token_address,
                token_symbol=trade.token_symbol,
                trade_type=trade.trade_type,
                amount_sol=trade.amount_sol,
                timestamp=trade.timestamp
            )
            for trade in trades
        ]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get signals: {str(e)}"
        )


@router.post("/update-leaderboard")
async def update_leaderboard_endpoint(db: AsyncSession = Depends(get_db)):
    """
    Manually trigger leaderboard update

    Admin endpoint - should be called periodically by cron job
    """
    try:
        updated = await smart_money_tracker.update_leaderboard(db)
        return {
            "status": "success",
            "wallets_updated": updated,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to update leaderboard: {str(e)}"
        )
