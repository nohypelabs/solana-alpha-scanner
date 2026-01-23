"use client";

import { WalletMultiButton } from "@solana/wallet-adapter-react-ui";
import Link from "next/link";

export default function TrackerPage() {
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

      <main className="container mx-auto px-4 py-12 max-w-6xl">
        <h1 className="text-4xl font-bold mb-8 text-white">
          Smart Money Tracker
        </h1>

        <div className="text-center py-20">
          <div className="text-6xl mb-4">🚧</div>
          <h2 className="text-2xl font-bold text-white mb-4">
            Coming Soon
          </h2>
          <p className="text-gray-400 mb-8">
            Smart Money Tracker is under development.
            <br />
            Soon you'll be able to track profitable wallets and copy their trades.
          </p>
          <Link
            href="/scan"
            className="inline-block px-8 py-4 bg-purple-600 hover:bg-purple-700 text-white rounded-lg font-semibold transition-colors"
          >
            Try Token Scanner
          </Link>
        </div>
      </main>
    </div>
  );
}
