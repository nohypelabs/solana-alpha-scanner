"use client";

import Link from "next/link";
import { WalletMultiButton } from "@solana/wallet-adapter-react-ui";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 to-black">
      {/* Header */}
      <header className="border-b border-gray-800">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-white">
            Solana Alpha Scanner
          </h1>
          <WalletMultiButton />
        </div>
      </header>

      {/* Hero Section */}
      <main className="container mx-auto px-4 py-20">
        <div className="text-center max-w-4xl mx-auto">
          <h2 className="text-6xl font-bold mb-6 bg-gradient-to-r from-purple-400 to-pink-600 text-transparent bg-clip-text">
            Scan Tokens. Track Winners. Copy Profits.
          </h2>

          <p className="text-xl text-gray-400 mb-12">
            Avoid rug pulls and find profitable wallets with Solana Alpha Scanner.
            Real-time token analysis and smart money tracking.
          </p>

          <div className="flex gap-4 justify-center mb-16">
            <Link
              href="/scan"
              className="px-8 py-4 bg-purple-600 hover:bg-purple-700 text-white rounded-lg font-semibold text-lg transition-colors"
            >
              Scan Token
            </Link>
            <Link
              href="/tracker"
              className="px-8 py-4 bg-gray-800 hover:bg-gray-700 text-white rounded-lg font-semibold text-lg transition-colors"
            >
              Smart Money Tracker
            </Link>
          </div>

          {/* Features Grid */}
          <div className="grid md:grid-cols-3 gap-8 mt-20">
            <div className="p-6 bg-gray-800/50 rounded-xl border border-gray-700">
              <div className="text-4xl mb-4">🔍</div>
              <h3 className="text-xl font-bold mb-2">Token Scanner</h3>
              <p className="text-gray-400">
                Instant risk analysis for any SPL token. Check holder concentration, liquidity, and red flags.
              </p>
            </div>

            <div className="p-6 bg-gray-800/50 rounded-xl border border-gray-700">
              <div className="text-4xl mb-4">💰</div>
              <h3 className="text-xl font-bold mb-2">Smart Money Tracker</h3>
              <p className="text-gray-400">
                Track profitable wallets and copy their trades. See what smart money is buying.
              </p>
            </div>

            <div className="p-6 bg-gray-800/50 rounded-xl border border-gray-700">
              <div className="text-4xl mb-4">⚡</div>
              <h3 className="text-xl font-bold mb-2">Real-time Alerts</h3>
              <p className="text-gray-400">
                Get instant notifications when tracked wallets make moves. Never miss alpha again.
              </p>
            </div>
          </div>

          {/* Stats */}
          <div className="grid md:grid-cols-3 gap-8 mt-16 text-center">
            <div>
              <div className="text-4xl font-bold text-purple-400">10k+</div>
              <div className="text-gray-400 mt-2">Tokens Scanned</div>
            </div>
            <div>
              <div className="text-4xl font-bold text-purple-400">500+</div>
              <div className="text-gray-400 mt-2">Smart Money Wallets</div>
            </div>
            <div>
              <div className="text-4xl font-bold text-purple-400">$2M+</div>
              <div className="text-gray-400 mt-2">Rugs Avoided</div>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-gray-800 mt-20">
        <div className="container mx-auto px-4 py-8 text-center text-gray-500">
          <p>Built on Solana. Always DYOR.</p>
        </div>
      </footer>
    </div>
  );
}
