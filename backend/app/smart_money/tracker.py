"""Smart money wallet tracking and analysis"""
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc, and_

from ..models import SmartMoneyWallet, Trade
from ..solana_client import solana_client

logger = logging.getLogger(__name__)


class SmartMoneyTracker:
    """Track and analyze profitable Solana wallets"""

    def __init__(self):
        self.min_trades_for_ranking = 10
        self.min_win_rate = 50.0  # 50%

    async def analyze_wallet(
        self,
        wallet_address: str,
        db: AsyncSession
    ) -> Dict[str, Any]:
        """
        Analyze a wallet's performance

        Returns profitability metrics
        """
        try:
            # Get all trades for this wallet
            stmt = (
                select(Trade)
                .where(Trade.wallet_address == wallet_address)
                .order_by(desc(Trade.timestamp))
            )
            result = await db.execute(stmt)
            trades = result.scalars().all()

            if not trades:
                return {
                    "wallet_address": wallet_address,
                    "total_trades": 0,
                    "error": "No trades found"
                }

            # Calculate metrics
            total_trades = len(trades)
            buy_trades = [t for t in trades if t.trade_type == "buy"]
            sell_trades = [t for t in trades if t.trade_type == "sell"]

            # Calculate PnL (simplified - assumes matched buy/sell pairs)
            total_pnl = self._calculate_pnl(buy_trades, sell_trades)

            # Calculate win rate
            winning_trades = sum(1 for t in sell_trades if t.amount_sol > 0)
            win_rate = (winning_trades / len(sell_trades) * 100) if sell_trades else 0

            # Get last 30 days trades
            thirty_days_ago = datetime.utcnow() - timedelta(days=30)
            recent_trades = [t for t in trades if t.timestamp >= thirty_days_ago]
            recent_pnl = self._calculate_pnl(
                [t for t in recent_trades if t.trade_type == "buy"],
                [t for t in recent_trades if t.trade_type == "sell"]
            )

            # Average return
            avg_return = (total_pnl / len(sell_trades)) if sell_trades else 0

            return {
                "wallet_address": wallet_address,
                "total_trades": total_trades,
                "total_pnl": total_pnl,
                "win_rate": win_rate,
                "avg_return": avg_return,
                "last_30d_pnl": recent_pnl,
                "recent_trades": [
                    {
                        "token": t.token_symbol or t.token_address[:8],
                        "type": t.trade_type,
                        "amount": t.amount_token,
                        "price_sol": t.price_sol,
                        "timestamp": t.timestamp.isoformat()
                    }
                    for t in recent_trades[:5]
                ]
            }

        except Exception as e:
            logger.error(f"Error analyzing wallet {wallet_address}: {e}")
            return {
                "wallet_address": wallet_address,
                "error": str(e)
            }

    def _calculate_pnl(
        self,
        buy_trades: List[Trade],
        sell_trades: List[Trade]
    ) -> float:
        """Calculate profit/loss from buy/sell trades"""
        total_bought_sol = sum(t.amount_sol for t in buy_trades)
        total_sold_sol = sum(t.amount_sol for t in sell_trades)
        return total_sold_sol - total_bought_sol

    async def update_leaderboard(self, db: AsyncSession) -> int:
        """
        Update smart money wallet leaderboard

        Returns number of wallets updated
        """
        try:
            # Get all unique wallets with trades
            stmt = select(Trade.wallet_address).distinct()
            result = await db.execute(stmt)
            wallet_addresses = [row[0] for row in result.all()]

            logger.info(f"Updating leaderboard for {len(wallet_addresses)} wallets")

            updated = 0
            for wallet_address in wallet_addresses:
                metrics = await self.analyze_wallet(wallet_address, db)

                if "error" in metrics:
                    continue

                # Only include wallets meeting minimum criteria
                if (metrics["total_trades"] < self.min_trades_for_ranking or
                    metrics["win_rate"] < self.min_win_rate):
                    continue

                # Find or create smart money wallet record
                stmt = select(SmartMoneyWallet).where(
                    SmartMoneyWallet.wallet_address == wallet_address
                )
                result = await db.execute(stmt)
                wallet = result.scalar_one_or_none()

                if not wallet:
                    wallet = SmartMoneyWallet(wallet_address=wallet_address)
                    db.add(wallet)

                # Update metrics
                wallet.total_pnl = metrics["total_pnl"]
                wallet.win_rate = metrics["win_rate"]
                wallet.total_trades = metrics["total_trades"]
                wallet.avg_return = metrics["avg_return"]
                wallet.last_30d_pnl = metrics["last_30d_pnl"]
                wallet.last_updated = datetime.utcnow()
                wallet.is_active = True

                updated += 1

            await db.commit()

            # Assign ranks based on total_pnl
            await self._assign_ranks(db)

            logger.info(f"Leaderboard updated: {updated} wallets")
            return updated

        except Exception as e:
            logger.error(f"Error updating leaderboard: {e}")
            await db.rollback()
            return 0

    async def _assign_ranks(self, db: AsyncSession):
        """Assign ranks to wallets based on total PnL"""
        stmt = (
            select(SmartMoneyWallet)
            .where(SmartMoneyWallet.is_active == True)
            .order_by(desc(SmartMoneyWallet.total_pnl))
        )
        result = await db.execute(stmt)
        wallets = result.scalars().all()

        for idx, wallet in enumerate(wallets, start=1):
            wallet.rank = idx

        await db.commit()

    async def get_wallet_recent_activity(
        self,
        wallet_address: str,
        db: AsyncSession,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Get recent trading activity for a wallet"""
        try:
            stmt = (
                select(Trade)
                .where(Trade.wallet_address == wallet_address)
                .order_by(desc(Trade.timestamp))
                .limit(limit)
            )
            result = await db.execute(stmt)
            trades = result.scalars().all()

            return [
                {
                    "token_address": trade.token_address,
                    "token_symbol": trade.token_symbol,
                    "trade_type": trade.trade_type,
                    "amount_token": trade.amount_token,
                    "amount_sol": trade.amount_sol,
                    "price_sol": trade.price_sol,
                    "signature": trade.signature,
                    "timestamp": trade.timestamp.isoformat()
                }
                for trade in trades
            ]

        except Exception as e:
            logger.error(f"Error getting wallet activity: {e}")
            return []


# Global instance
smart_money_tracker = SmartMoneyTracker()
