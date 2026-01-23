"use client";

import { useState, useEffect } from "react";
import { useWallet } from "@solana/wallet-adapter-react";
import { WalletMultiButton } from "@solana/wallet-adapter-react-ui";
import Link from "next/link";
import { smartMoneyApi, LeaderboardEntry, RecentSignal } from "@/lib/smartMoneyApi";

export default function TrackerPage() {
  const { publicKey } = useWallet();
  const [leaderboard, setLeaderboard] = useState<LeaderboardEntry[]>([]);
  const [signals, setSignals] = useState<RecentSignal[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<"leaderboard" | "signals">("leaderboard");

  useEffect(() => {
    loadData();
  }, [activeTab]);

  const loadData = async () => {
    setLoading(true);
    setError(null);

    try {
      if (activeTab === "leaderboard") {
        const data = await smartMoneyApi.getLeaderboard(100);
        setLeaderboard(data);
      } else {
        const data = await smartMoneyApi.getRecentSignals(50);
        setSignals(data);
      }
    } catch (err: any) {
      setError(err.response?.data?.detail || "Failed to load data");
    } finally {
      setLoading(false);
    }
  };

  const formatPnL = (pnl: number) => {
    const sign = pnl >= 0 ? "+" : "";
    return `${sign}${pnl.toFixed(2)} SOL`;
  };

  const getPnLColor = (pnl: number) => {
    return pnl >= 0 ? "text-green-500" : "text-red-500";
  };

  const formatTimestamp = (timestamp: string) => {
    const date = new Date(timestamp);
    const now = new Date();
    const diffMs = now.getTime() - date.getTime();
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMs / 3600000);
    const diffDays = Math.floor(diffMs / 86400000);

    if (diffMins < 60) return `${diffMins}m ago`;
    if (diffHours < 24) return `${diffHours}h ago`;
    return `${diffDays}d ago`;
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 to-black">
      {/* Header */}
      <header className="border-b border-gray-800">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <Link href="/" className="text-2xl font-bold text-white">
            Solana Alpha Scanner
          </Link>
          <WalletMultiButton />
        </div>
      </header>

      <main className="container mx-auto px-4 py-12 max-w-7xl">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-4xl font-bold text-white">Smart Money Tracker</h1>
          <Link
            href="/scan"
            className="px-6 py-2 bg-gray-800 hover:bg-gray-700 text-white rounded-lg transition-colors"
          >
            Token Scanner
          </Link>
        </div>

        {/* Tabs */}
        <div className="flex gap-4 mb-8">
          <button
            onClick={() => setActiveTab("leaderboard")}
            className={`px-6 py-3 rounded-lg font-semibold transition-colors ${
              activeTab === "leaderboard"
                ? "bg-purple-600 text-white"
                : "bg-gray-800 text-gray-400 hover:text-white"
            }`}
          >
            Leaderboard
          </button>
          <button
            onClick={() => setActiveTab("signals")}
            className={`px-6 py-3 rounded-lg font-semibold transition-colors ${
              activeTab === "signals"
                ? "bg-purple-600 text-white"
                : "bg-gray-800 text-gray-400 hover:text-white"
            }`}
          >
            Recent Signals
          </button>
        </div>

        {/* Error */}
        {error && (
          <div className="mb-8 p-4 bg-red-900/50 border border-red-700 rounded-lg text-red-200">
            {error}
          </div>
        )}

        {/* Loading */}
        {loading && (
          <div className="text-center py-20">
            <div className="text-xl text-gray-400">Loading...</div>
          </div>
        )}

        {/* Leaderboard Tab */}
        {!loading && activeTab === "leaderboard" && (
          <div className="bg-gray-800 rounded-lg border border-gray-700 overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-gray-900">
                  <tr>
                    <th className="px-6 py-4 text-left text-gray-400 font-semibold">
                      Rank
                    </th>
                    <th className="px-6 py-4 text-left text-gray-400 font-semibold">
                      Wallet
                    </th>
                    <th className="px-6 py-4 text-right text-gray-400 font-semibold">
                      Total P&L
                    </th>
                    <th className="px-6 py-4 text-right text-gray-400 font-semibold">
                      30D P&L
                    </th>
                    <th className="px-6 py-4 text-right text-gray-400 font-semibold">
                      Win Rate
                    </th>
                    <th className="px-6 py-4 text-right text-gray-400 font-semibold">
                      Trades
                    </th>
                    <th className="px-6 py-4 text-right text-gray-400 font-semibold">
                      Avg Return
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {leaderboard.map((wallet) => (
                    <tr
                      key={wallet.wallet_address}
                      className="border-t border-gray-700 hover:bg-gray-750 transition-colors"
                    >
                      <td className="px-6 py-4">
                        <div className="flex items-center gap-2">
                          {wallet.rank <= 3 && (
                            <span className="text-2xl">
                              {wallet.rank === 1 ? "🥇" : wallet.rank === 2 ? "🥈" : "🥉"}
                            </span>
                          )}
                          <span className="text-white font-bold">#{wallet.rank}</span>
                        </div>
                      </td>
                      <td className="px-6 py-4">
                        <span className="text-purple-400 font-mono text-sm">
                          {wallet.wallet_address.slice(0, 6)}...
                          {wallet.wallet_address.slice(-4)}
                        </span>
                      </td>
                      <td className={`px-6 py-4 text-right font-bold ${getPnLColor(wallet.total_pnl)}`}>
                        {formatPnL(wallet.total_pnl)}
                      </td>
                      <td className={`px-6 py-4 text-right font-bold ${getPnLColor(wallet.last_30d_pnl)}`}>
                        {formatPnL(wallet.last_30d_pnl)}
                      </td>
                      <td className="px-6 py-4 text-right text-white">
                        {wallet.win_rate.toFixed(1)}%
                      </td>
                      <td className="px-6 py-4 text-right text-white">
                        {wallet.total_trades}
                      </td>
                      <td className={`px-6 py-4 text-right font-bold ${getPnLColor(wallet.avg_return)}`}>
                        {formatPnL(wallet.avg_return)}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>

              {leaderboard.length === 0 && (
                <div className="text-center py-12 text-gray-400">
                  No smart money wallets found. Trade data will appear here soon.
                </div>
              )}
            </div>
          </div>
        )}

        {/* Signals Tab */}
        {!loading && activeTab === "signals" && (
          <div className="space-y-4">
            {signals.map((signal, idx) => (
              <div
                key={`${signal.wallet_address}-${signal.timestamp}-${idx}`}
                className="bg-gray-800 p-6 rounded-lg border border-gray-700 hover:border-purple-500 transition-colors"
              >
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <div className="flex items-center gap-3 mb-2">
                      {signal.wallet_rank && signal.wallet_rank <= 10 && (
                        <span className="px-3 py-1 bg-purple-900 text-purple-300 rounded-full text-sm font-bold">
                          #{signal.wallet_rank}
                        </span>
                      )}
                      <span className="text-purple-400 font-mono text-sm">
                        {signal.wallet_address.slice(0, 6)}...
                        {signal.wallet_address.slice(-4)}
                      </span>
                    </div>
                    <div className="text-gray-400 text-sm">
                      {formatTimestamp(signal.timestamp)}
                    </div>
                  </div>
                  <div
                    className={`px-4 py-2 rounded-lg font-bold ${
                      signal.trade_type === "buy"
                        ? "bg-green-900 text-green-300"
                        : "bg-red-900 text-red-300"
                    }`}
                  >
                    {signal.trade_type.toUpperCase()}
                  </div>
                </div>

                <div className="flex justify-between items-center">
                  <div>
                    <div className="text-white font-semibold mb-1">
                      {signal.token_symbol || "Unknown Token"}
                    </div>
                    <div className="text-gray-400 text-sm font-mono">
                      {signal.token_address.slice(0, 8)}...
                      {signal.token_address.slice(-8)}
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="text-white font-bold text-xl">
                      {signal.amount_sol.toFixed(2)} SOL
                    </div>
                  </div>
                </div>
              </div>
            ))}

            {signals.length === 0 && (
              <div className="text-center py-12 text-gray-400 bg-gray-800 rounded-lg">
                No recent signals. Trading activity will appear here.
              </div>
            )}
          </div>
        )}
      </main>
    </div>
  );
}
