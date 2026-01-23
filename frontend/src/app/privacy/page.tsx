import Link from "next/link";

export default function PrivacyPolicy() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 to-black">
      <header className="border-b border-gray-800">
        <div className="container mx-auto px-4 py-4">
          <Link href="/" className="text-2xl font-bold text-white">
            Solana Alpha Scanner
          </Link>
        </div>
      </header>

      <main className="container mx-auto px-4 py-12 max-w-4xl">
        <h1 className="text-4xl font-bold mb-8 text-white">Privacy Policy</h1>

        <div className="prose prose-invert max-w-none space-y-6 text-gray-300">
          <p className="text-sm text-gray-500">Last Updated: January 24, 2026</p>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">1. Introduction</h2>
            <p>
              Solana Alpha Scanner ("we", "our", or "us") respects your privacy and is committed to protecting
              your personal data. This privacy policy explains how we collect, use, and safeguard your information
              when you use our application.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">2. Information We Collect</h2>

            <h3 className="text-xl font-semibold text-white mb-2">2.1 Wallet Address</h3>
            <p>
              When you connect your Solana wallet, we collect your public wallet address for the following purposes:
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Associating your token scan history with your account</li>
              <li>Managing your tracked wallets and alert preferences</li>
              <li>Providing personalized features based on your subscription tier</li>
            </ul>

            <h3 className="text-xl font-semibold text-white mb-2 mt-4">2.2 Usage Data</h3>
            <p>We automatically collect certain information including:</p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Token addresses you scan</li>
              <li>Pages you visit within the app</li>
              <li>Device type and browser information</li>
              <li>IP address and general location (country/region)</li>
              <li>Time and date of your visits</li>
            </ul>

            <h3 className="text-xl font-semibold text-white mb-2 mt-4">2.3 Blockchain Data</h3>
            <p>
              All blockchain transactions and wallet activities are public information retrieved from the
              Solana blockchain. We do not control or own this data.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">3. How We Use Your Information</h2>
            <p>We use collected information for:</p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Providing and maintaining our service</li>
              <li>Analyzing token risk and displaying results</li>
              <li>Tracking smart money wallets and generating signals</li>
              <li>Managing your subscription and preferences</li>
              <li>Sending alerts for tracked wallets (if enabled)</li>
              <li>Improving our algorithms and user experience</li>
              <li>Preventing fraud and abuse</li>
              <li>Complying with legal obligations</li>
            </ul>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">4. Data Security</h2>
            <p>We implement industry-standard security measures to protect your data:</p>
            <ul className="list-disc pl-6 space-y-2">
              <li>HTTPS encryption for all data transmission</li>
              <li>Secure database storage with encryption at rest</li>
              <li>Regular security audits and updates</li>
              <li>Access controls and authentication</li>
              <li>We NEVER ask for or store your private keys</li>
            </ul>
            <p className="mt-4 font-semibold text-yellow-400">
              IMPORTANT: We are a non-custodial service. We never have access to your wallet's private keys
              or the ability to move your funds.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">5. Data Sharing</h2>
            <p>We do NOT sell your personal data. We may share data with:</p>
            <ul className="list-disc pl-6 space-y-2">
              <li>
                <strong>Service Providers:</strong> Third-party services that help us operate (hosting, analytics)
              </li>
              <li>
                <strong>Blockchain Networks:</strong> Public wallet addresses are visible on Solana blockchain
              </li>
              <li>
                <strong>Legal Authorities:</strong> When required by law or to protect our rights
              </li>
            </ul>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">6. Cookies and Tracking</h2>
            <p>
              We use local storage and session storage to enhance your experience. We may use third-party
              analytics services (e.g., Vercel Analytics) to understand how users interact with our app.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">7. Your Rights</h2>
            <p>You have the right to:</p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Access your personal data</li>
              <li>Request data deletion</li>
              <li>Opt-out of alerts and communications</li>
              <li>Disconnect your wallet at any time</li>
              <li>Export your scan history</li>
            </ul>
            <p className="mt-4">
              To exercise these rights, contact us at: <span className="text-purple-400">privacy@solana-alpha.app</span>
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">8. Children's Privacy</h2>
            <p>
              Our service is not intended for users under 18 years of age. We do not knowingly collect
              data from children. If you believe a child has provided us with personal data, please contact us.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">9. International Users</h2>
            <p>
              Our service is available globally. By using our app, you consent to the transfer of your
              information to our servers (currently hosted in the United States and EU).
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">10. Changes to This Policy</h2>
            <p>
              We may update this privacy policy from time to time. We will notify you of significant changes
              by posting the new policy with an updated "Last Updated" date. Continued use of the service
              after changes constitutes acceptance of the new policy.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">11. Disclaimer</h2>
            <p className="text-yellow-400 font-semibold">
              Solana Alpha Scanner provides analysis tools for informational purposes only. We are not
              financial advisors. All trading and investment decisions are your own responsibility.
              Cryptocurrency trading involves significant risk. Never invest more than you can afford to lose.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">12. Contact Us</h2>
            <p>If you have questions about this privacy policy, contact us at:</p>
            <ul className="list-none space-y-2 mt-4">
              <li>Email: <span className="text-purple-400">privacy@solana-alpha.app</span></li>
              <li>GitHub: <a href="https://github.com/agds-alt/solana-alpha-scanner" className="text-purple-400 hover:underline">github.com/agds-alt/solana-alpha-scanner</a></li>
              <li>Discord: Coming soon</li>
            </ul>
          </section>
        </div>

        <div className="mt-12 pt-8 border-t border-gray-800">
          <Link href="/" className="text-purple-400 hover:underline">
            ← Back to Home
          </Link>
        </div>
      </main>
    </div>
  );
}
