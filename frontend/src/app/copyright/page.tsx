import Link from "next/link";

export default function CopyrightPolicy() {
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
        <h1 className="text-4xl font-bold mb-8 text-white">Copyright Policy</h1>

        <div className="prose prose-invert max-w-none space-y-6 text-gray-300">
          <p className="text-sm text-gray-500">Last Updated: January 24, 2026</p>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">1. Copyright Ownership</h2>
            <p>
              All content, features, and functionality of Solana Alpha Scanner, including but not limited to:
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Software code and algorithms</li>
              <li>User interface design and layout</li>
              <li>Graphics, logos, and icons</li>
              <li>Text content and documentation</li>
              <li>Trademarks and branding</li>
            </ul>
            <p className="mt-4">
              are owned by Solana Alpha Scanner and protected by international copyright, trademark, and
              other intellectual property laws.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">2. Open Source Components</h2>
            <p>
              Portions of our software use open-source libraries and frameworks, including but not limited to:
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Next.js (MIT License)</li>
              <li>React (MIT License)</li>
              <li>Solana Web3.js (Apache 2.0)</li>
              <li>FastAPI (MIT License)</li>
              <li>TailwindCSS (MIT License)</li>
            </ul>
            <p className="mt-4">
              These components retain their original licenses and are used in compliance with their terms.
              Full attribution and licenses can be found in our GitHub repository.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">3. User Content</h2>
            <p>
              Users retain copyright to any content they create or upload (if applicable). By using our service,
              you grant us a non-exclusive, worldwide license to use your content solely for providing and
              improving our service.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">4. Blockchain Data</h2>
            <p>
              All blockchain data displayed in Solana Alpha Scanner is public information from the Solana
              blockchain. We do not claim ownership of blockchain data. This data is:
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Publicly available on-chain</li>
              <li>Retrieved via RPC endpoints</li>
              <li>Aggregated and analyzed by our algorithms</li>
              <li>Displayed for informational purposes</li>
            </ul>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">5. DMCA Compliance</h2>
            <p>
              We respect the intellectual property rights of others and comply with the Digital Millennium
              Copyright Act (DMCA). If you believe your copyrighted work has been copied in a way that
              constitutes infringement, please notify us with:
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Description of the copyrighted work</li>
              <li>Location of the infringing material</li>
              <li>Your contact information</li>
              <li>A statement of good faith belief</li>
              <li>A statement of accuracy under penalty of perjury</li>
              <li>Your physical or electronic signature</li>
            </ul>
            <p className="mt-4">
              Send DMCA notices to: <span className="text-purple-400">dmca@solana-alpha.app</span>
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">6. Counter-Notification</h2>
            <p>
              If you believe content was removed in error, you may file a counter-notification containing:
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Your name, address, and phone number</li>
              <li>Description of the removed content</li>
              <li>Statement under penalty of perjury that removal was a mistake</li>
              <li>Consent to jurisdiction in your district</li>
              <li>Your physical or electronic signature</li>
            </ul>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">7. Trademark Policy</h2>
            <p>
              "Solana Alpha Scanner" and associated logos are trademarks. You may not use our trademarks
              without prior written permission, except for:
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Fair use in reviews or commentary</li>
              <li>Referencing our service in an accurate, non-misleading way</li>
              <li>Educational or research purposes</li>
            </ul>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">8. Third-Party Trademarks</h2>
            <p>
              We display various third-party trademarks and logos, including:
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Solana Foundation logos and trademarks</li>
              <li>Wallet provider logos (Phantom, Solflare, etc.)</li>
              <li>Token logos and symbols</li>
            </ul>
            <p className="mt-4">
              These trademarks are property of their respective owners. Their use is purely for identification
              and does not imply endorsement.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">9. Acceptable Use</h2>
            <p>
              You may use Solana Alpha Scanner for lawful purposes only. You may NOT:
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Reverse engineer, decompile, or disassemble our software</li>
              <li>Remove copyright or proprietary notices</li>
              <li>Use our service to create competing products</li>
              <li>Scrape or harvest data via automated means</li>
              <li>Redistribute or resell our service</li>
              <li>Violate any applicable laws or regulations</li>
            </ul>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">10. API and Data Usage</h2>
            <p>
              If you use our API (Whale tier):
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>You receive a limited license to access data via API</li>
              <li>You must attribute data to Solana Alpha Scanner</li>
              <li>You cannot redistribute raw API data</li>
              <li>Commercial use requires separate agreement</li>
            </ul>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">11. Reporting Infringement</h2>
            <p>
              To report copyright infringement or trademark violations:
            </p>
            <ul className="list-none space-y-2 mt-4">
              <li>Email: <span className="text-purple-400">dmca@solana-alpha.app</span></li>
              <li>GitHub: <a href="https://github.com/agds-alt/solana-alpha-scanner/issues" className="text-purple-400 hover:underline">File an issue</a></li>
            </ul>
            <p className="mt-4">
              We will investigate all valid claims within 48 hours and take appropriate action.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">12. Repeat Infringers</h2>
            <p>
              We maintain a policy of terminating accounts of users who repeatedly infringe copyrights,
              in appropriate circumstances and at our sole discretion.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">13. Modifications</h2>
            <p>
              We reserve the right to modify this copyright policy at any time. Changes will be posted
              with an updated "Last Updated" date. Your continued use after changes constitutes acceptance.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">14. Contact Information</h2>
            <p>For copyright-related inquiries:</p>
            <ul className="list-none space-y-2 mt-4">
              <li>DMCA Agent: <span className="text-purple-400">dmca@solana-alpha.app</span></li>
              <li>General Copyright: <span className="text-purple-400">legal@solana-alpha.app</span></li>
              <li>GitHub: <a href="https://github.com/agds-alt/solana-alpha-scanner" className="text-purple-400 hover:underline">github.com/agds-alt/solana-alpha-scanner</a></li>
            </ul>
          </section>

          <section>
            <h2 className="text-2xl font-bold text-white mb-4">15. Open Source License</h2>
            <p>
              Our backend code is available under MIT License. See our GitHub repository for full license text.
              This means you can:
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Use the code for personal or commercial projects</li>
              <li>Modify and distribute the code</li>
              <li>Include it in proprietary software</li>
            </ul>
            <p className="mt-4">
              With the following conditions:
            </p>
            <ul className="list-disc pl-6 space-y-2">
              <li>Include the original copyright notice</li>
              <li>Include the MIT License text</li>
              <li>No warranty is provided</li>
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
