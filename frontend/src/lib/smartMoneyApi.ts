import api from "./api";

export interface LeaderboardEntry {
  rank: number;
  wallet_address: string;
  total_pnl: number;
  win_rate: number;
  total_trades: number;
  avg_return: number;
  last_30d_pnl: number;
}

export interface WalletDetails {
  wallet_address: string;
  rank: number | null;
  total_pnl: number;
  win_rate: number;
  total_trades: number;
  avg_return: number;
  last_30d_pnl: number;
  recent_activity: Array<{
    token_address: string;
    token_symbol: string | null;
    trade_type: string;
    amount_token: number;
    amount_sol: number;
    price_sol: number;
    signature: string;
    timestamp: string;
  }>;
}

export interface RecentSignal {
  wallet_address: string;
  wallet_rank: number | null;
  token_address: string;
  token_symbol: string | null;
  trade_type: string;
  amount_sol: number;
  timestamp: string;
}

export const smartMoneyApi = {
  getLeaderboard: async (limit: number = 100): Promise<LeaderboardEntry[]> => {
    const response = await api.get("/api/smart-money/leaderboard", {
      params: { limit },
    });
    return response.data;
  },

  getWalletDetails: async (walletAddress: string): Promise<WalletDetails> => {
    const response = await api.get(`/api/smart-money/wallet/${walletAddress}`);
    return response.data;
  },

  trackWallet: async (
    userWallet: string,
    targetWallet: string,
    nickname?: string
  ) => {
    const response = await api.post("/api/smart-money/track", {
      user_wallet: userWallet,
      target_wallet: targetWallet,
      nickname,
      alert_on_buy: true,
      alert_on_sell: true,
      min_trade_size_sol: 1.0,
    });
    return response.data;
  },

  getTrackedWallets: async (userWallet: string) => {
    const response = await api.get("/api/smart-money/tracked", {
      params: { user_wallet: userWallet },
    });
    return response.data;
  },

  getRecentSignals: async (limit: number = 20): Promise<RecentSignal[]> => {
    const response = await api.get("/api/smart-money/signals", {
      params: { limit },
    });
    return response.data;
  },
};
