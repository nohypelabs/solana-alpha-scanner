import axios from "axios";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export interface TokenScanRequest {
  token_address: string;
  wallet_address?: string;
}

export interface TokenScanResponse {
  token_address: string;
  symbol: string;
  name: string;
  risk_score: number;
  verdict: "SAFE" | "CAUTION" | "SCAM";
  metrics: {
    holder_count: number;
    top_holder_pct: number;
    liquidity_usd: number;
    market_cap_usd: number;
    concentration_score: number;
    volume_24h: number;
  };
  top_holders: Array<{
    address: string;
    percentage: number;
  }>;
  flags: {
    high_concentration: boolean;
    low_liquidity: boolean;
    low_holder_count: boolean;
    new_token: boolean;
    suspicious_pattern: boolean;
  };
  recommendation: string;
  scanned_at: string;
}

export const tokenApi = {
  scanToken: async (data: TokenScanRequest): Promise<TokenScanResponse> => {
    const response = await api.post("/api/scan/token", data);
    return response.data;
  },

  getScanHistory: async (walletAddress: string, limit: number = 20) => {
    const response = await api.get("/api/scan/history", {
      params: { wallet_address: walletAddress, limit },
    });
    return response.data;
  },

  getScanStats: async () => {
    const response = await api.get("/api/scan/stats");
    return response.data;
  },
};

export default api;
