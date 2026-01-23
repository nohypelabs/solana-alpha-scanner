"use client";

import { useState } from "react";
import { useWallet } from "@solana/wallet-adapter-react";
import { WalletMultiButton } from "@solana/wallet-adapter-react-ui";
import { tokenApi, TokenScanResponse } from "@/lib/api";
import Link from "next/link";

export default function ScanPage() {
  const { publicKey } = useWallet();
  const [tokenAddress, setTokenAddress] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<TokenScanResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleScan = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const data = await tokenApi.scanToken({
        token_address: tokenAddress,
        wallet_address: publicKey?.toString(),
      });
      setResult(data);
    } catch (err: any) {
      setError(err.response?.data?.detail || "Scan failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const getVerdictColor = (verdict: string) => {
    switch (verdict) {
      case "SAFE":
        return "text-green-500";
      case "CAUTION":
        return "text-yellow-500";
      case "SCAM":
        return "text-red-500";
      default:
        return "text-gray-500";
    }
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

      <main className="container mx-auto px-4 py-12 max-w-4xl">
        <h1 className="text-4xl font-bold mb-8 text-white">Token Scanner</h1>

        {/* Scan Form */}
        <form onSubmit={handleScan} className="mb-8">
          <div className="flex gap-4">
            <input
              type="text"
              value={tokenAddress}
              onChange={(e) => setTokenAddress(e.target.value)}
              placeholder="Enter token address (e.g., 9Avytn...)"
              className="flex-1 px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:border-purple-500"
              disabled={loading}
            />
            <button
              type="submit"
              disabled={loading || !tokenAddress}
              className="px-8 py-3 bg-purple-600 hover:bg-purple-700 disabled:bg-gray-700 text-white rounded-lg font-semibold transition-colors"
            >
              {loading ? "Scanning..." : "Scan"}
            </button>
          </div>
        </form>

        {/* Error */}
        {error && (
          <div className="mb-8 p-4 bg-red-900/50 border border-red-700 rounded-lg text-red-200">
            {error}
          </div>
        )}

        {/* Results */}
        {result && (
          <div className="space-y-6">
            {/* Header */}
            <div className="bg-gray-800 p-6 rounded-lg border border-gray-700">
              <div className="flex justify-between items-start mb-4">
                <div>
                  <h2 className="text-2xl font-bold text-white mb-1">
                    {result.name} ({result.symbol})
                  </h2>
                  <p className="text-gray-400 text-sm font-mono">
                    {result.token_address}
                  </p>
                </div>
                <div className="text-right">
                  <div className={`text-3xl font-bold ${getVerdictColor(result.verdict)}`}>
                    {result.verdict}
                  </div>
                  <div className="text-gray-400 text-sm mt-1">
                    Risk Score: {result.risk_score}/100
                  </div>
                </div>
              </div>

              <div className="bg-gray-900 p-4 rounded-lg">
                <p className="text-white">{result.recommendation}</p>
              </div>
            </div>

            {/* Metrics */}
            <div className="bg-gray-800 p-6 rounded-lg border border-gray-700">
              <h3 className="text-xl font-bold mb-4 text-white">Metrics</h3>
              <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                <div>
                  <div className="text-gray-400 text-sm">Holders</div>
                  <div className="text-white font-bold text-xl">
                    {result.metrics.holder_count.toLocaleString()}
                  </div>
                </div>
                <div>
                  <div className="text-gray-400 text-sm">Top Holder</div>
                  <div className="text-white font-bold text-xl">
                    {result.metrics.top_holder_pct.toFixed(2)}%
                  </div>
                </div>
                <div>
                  <div className="text-gray-400 text-sm">Liquidity</div>
                  <div className="text-white font-bold text-xl">
                    ${result.metrics.liquidity_usd.toLocaleString()}
                  </div>
                </div>
                <div>
                  <div className="text-gray-400 text-sm">Market Cap</div>
                  <div className="text-white font-bold text-xl">
                    ${result.metrics.market_cap_usd.toLocaleString()}
                  </div>
                </div>
                <div>
                  <div className="text-gray-400 text-sm">24h Volume</div>
                  <div className="text-white font-bold text-xl">
                    ${result.metrics.volume_24h.toLocaleString()}
                  </div>
                </div>
                <div>
                  <div className="text-gray-400 text-sm">Concentration</div>
                  <div className="text-white font-bold text-xl">
                    {result.metrics.concentration_score.toFixed(1)}/10
                  </div>
                </div>
              </div>
            </div>

            {/* Flags */}
            <div className="bg-gray-800 p-6 rounded-lg border border-gray-700">
              <h3 className="text-xl font-bold mb-4 text-white">Warning Flags</h3>
              <div className="space-y-2">
                {Object.entries(result.flags).map(([key, value]) => (
                  <div key={key} className="flex items-center gap-2">
                    <div className={`w-3 h-3 rounded-full ${value ? "bg-red-500" : "bg-green-500"}`} />
                    <span className="text-white capitalize">
                      {key.replace(/_/g, " ")}
                    </span>
                  </div>
                ))}
              </div>
            </div>

            {/* Top Holders */}
            <div className="bg-gray-800 p-6 rounded-lg border border-gray-700">
              <h3 className="text-xl font-bold mb-4 text-white">Top Holders</h3>
              <div className="space-y-2">
                {result.top_holders.map((holder, idx) => (
                  <div
                    key={holder.address}
                    className="flex justify-between items-center p-3 bg-gray-900 rounded"
                  >
                    <span className="text-gray-400">#{idx + 1}</span>
                    <span className="text-white font-mono text-sm">
                      {holder.address.slice(0, 4)}...{holder.address.slice(-4)}
                    </span>
                    <span className="text-purple-400 font-bold">
                      {holder.percentage.toFixed(2)}%
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
