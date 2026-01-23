"""Database models"""
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    """User model"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    subscription_tier = Column(String, default="free")  # free, pro, whale
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, default=datetime.utcnow)

    # Relationships
    scans = relationship("TokenScan", back_populates="user")
    tracked_wallets = relationship("TrackedWallet", back_populates="user")


class TokenScan(Base):
    """Token scan history"""
    __tablename__ = "token_scans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    token_address = Column(String, index=True, nullable=False)
    symbol = Column(String, nullable=True)
    name = Column(String, nullable=True)
    risk_score = Column(Integer, nullable=False)
    verdict = Column(String, nullable=False)  # SAFE, CAUTION, SCAM

    # Metrics
    holder_count = Column(Integer, nullable=True)
    top_holder_pct = Column(Float, nullable=True)
    liquidity_usd = Column(Float, nullable=True)
    market_cap_usd = Column(Float, nullable=True)
    concentration_score = Column(Float, nullable=True)

    # Flags
    flags = Column(JSON, nullable=True)

    # Metadata
    scanned_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="scans")


class SmartMoneyWallet(Base):
    """Smart money wallet leaderboard"""
    __tablename__ = "smart_money_wallets"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, unique=True, index=True, nullable=False)
    rank = Column(Integer, nullable=True)

    # Performance metrics
    total_pnl = Column(Float, default=0.0)
    win_rate = Column(Float, default=0.0)
    total_trades = Column(Integer, default=0)
    avg_return = Column(Float, default=0.0)
    last_30d_pnl = Column(Float, default=0.0)

    # Metadata
    first_seen = Column(DateTime, default=datetime.utcnow)
    last_updated = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)


class TrackedWallet(Base):
    """User's tracked wallets"""
    __tablename__ = "tracked_wallets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    wallet_address = Column(String, nullable=False)
    nickname = Column(String, nullable=True)

    # Alert settings
    alert_on_buy = Column(Boolean, default=True)
    alert_on_sell = Column(Boolean, default=True)
    min_trade_size_sol = Column(Float, default=1.0)

    # Metadata
    added_at = Column(DateTime, default=datetime.utcnow)
    last_alert = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="tracked_wallets")


class Trade(Base):
    """Trade signals from smart money wallets"""
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, index=True, nullable=False)
    token_address = Column(String, index=True, nullable=False)
    token_symbol = Column(String, nullable=True)

    # Trade details
    trade_type = Column(String, nullable=False)  # buy, sell
    amount_token = Column(Float, nullable=False)
    amount_sol = Column(Float, nullable=False)
    price_sol = Column(Float, nullable=False)

    # Transaction
    signature = Column(String, unique=True, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    # Metadata
    detected_at = Column(DateTime, default=datetime.utcnow)


class Subscription(Base):
    """Subscription management"""
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tier = Column(String, nullable=False)  # pro, whale

    # Stripe
    stripe_customer_id = Column(String, unique=True, nullable=True)
    stripe_subscription_id = Column(String, unique=True, nullable=True)

    # Status
    status = Column(String, default="active")  # active, cancelled, expired
    current_period_start = Column(DateTime, nullable=False)
    current_period_end = Column(DateTime, nullable=False)

    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
