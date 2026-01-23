# 📱 Solana dApp Store Submission Requirements

**Complete checklist for publishing Solana Alpha Scanner to Solana Mobile dApp Store**

---

## ✅ Technical Requirements

### 1. Android APK
- ✅ **Release build** (NOT debug build)
- ✅ **Signed with NEW signing key** (created ONLY for dApp Store)
  - ⚠️ DO NOT use Google Play signing key
  - ⚠️ SAVE this key securely (needed for updates)
- ✅ Compatible with Solana Mobile devices
- ✅ Best-in-class security & encryption

### 2. PWA Alternative (If Building Web App)
- ✅ Can submit as Progressive Web App (PWA)
- ✅ Convert PWA → APK using TWA (Trusted Web Activity)
- ✅ Follow PWA-to-APK conversion guide

### 3. Network Requirements
- ✅ Minimum upload speed: **0.25 MB/s** during submission

---

## 🎨 Asset Requirements

### Icons
- **Size:** 512px × 512px (required)
- **Format:** PNG recommended
- **Design:** Follow Google Play icon guidelines
- **Usage:** App launcher icon

### Banner Graphic
- **Size:** 1200px × 600px (required)
- **Format:** PNG/JPG
- **Usage:** Store listing header

### Feature Graphic (Optional but Recommended)
- **Size:** 1200px × 1200px
- **Format:** PNG/JPG
- **Usage:** **Editor's Choice carousel** eligibility
- ⭐ **IMPORTANT:** Include this to get featured!

### Screenshots/Videos
- **Minimum:** 4 screenshots OR videos
- **Resolution:** 1080p recommended (1920px × 1080px)
- **Minimum dimensions:** 1080px width × 1080px height
- **Orientation:** ALL must be same (landscape OR portrait)
- **Aspect ratio:** ALL must be equal
- **Video format:** MP4 only
- **Video min size:** 720px × 720px

---

## 📝 Listing Information (config.yaml)

### Publisher Section
```yaml
publisher:
  name: "Your Name / Company"
  website: "https://solana-alpha.app"
  email: "dev@solana-alpha.app"
```

### App Section
```yaml
app:
  name: "Solana Alpha Scanner"
  android_package_name: "com.solanaalpha.scanner"
  urls:
    support_url: "https://solana-alpha.app/support"
    privacy_policy_url: "https://solana-alpha.app/privacy"
    copyright_policy_url: "https://solana-alpha.app/copyright"
```

### Release Section (Localized)
```yaml
release:
  catalog:
    en_US:
      name: "Solana Alpha Scanner"
      short_description: "Scan tokens. Track smart money. Copy profits."
      full_description: |
        Avoid rug pulls and find profitable wallets with Solana Alpha Scanner.

        Features:
        - Instant token risk analysis
        - Smart money wallet tracking
        - Real-time trading signals
        - Copy profitable trades

        Free tier available. Pro features unlock advanced analytics.
      new_in_version: "Initial release - Token Scanner + Smart Money Tracker"
      category: "FINANCE" # or "PRODUCTIVITY"
```

---

## 📄 Legal Documents Required

### 1. Privacy Policy ✅
- **Must have:** URL to privacy policy
- **Host online:** solanaalpha.app/privacy
- **Content:** Data collection, usage, storage policies

### 2. Copyright Policy ✅
- **Must have:** URL to copyright policy
- **Host online:** solanaalpha.app/copyright
- **Content:** DMCA compliance, copyright notices

### 3. End-User License Agreement (EULA) ✅
- **Recommended:** Terms of service
- **Content:** User rights, limitations, liability

---

## 🚫 Prohibited Content & Policies

### Prohibited Activities
❌ Review manipulation (fake reviews, purchased reviews)
❌ False information in listing
❌ Malware or security vulnerabilities
❌ Intellectual property violations
❌ Apps for sanctioned jurisdictions (Cuba, Iran, N. Korea, Syria, Crimea, Donetsk, Luhansk)
❌ Apps targeting restricted party lists (US Treasury/Commerce)

### Quality Requirements
✅ Safe and defect-free
✅ Complies with all applicable laws
✅ Best-in-class security & encryption
✅ Accessible privacy policy
✅ Timely updates for compatibility

### Crypto/DeFi Specific
⚠️ Must acknowledge legal uncertainty around crypto
⚠️ Must conduct independent legal investigation
⚠️ Developer assumes compliance responsibility

---

## 🔧 Submission Process

### Step 1: Install CLI
```bash
npm install -g @solana-mobile/dapp-store-cli
```

### Step 2: Prepare App
- [ ] Build release APK
- [ ] Sign with dApp Store key
- [ ] Create all assets (icons, banners, screenshots)
- [ ] Write privacy policy & copyright policy
- [ ] Prepare config.yaml

### Step 3: Create Solana Keypair
```bash
solana-keygen new --outfile ~/.config/solana/dapp-store-publisher.json
```

### Step 4: Mint App NFT
```bash
npx dapp-store create release \
  -k ~/.config/solana/dapp-store-publisher.json \
  -b /path/to/android/sdk/build-tools
```

**Fee:** Default 500,000 lamports (~$0.10)
**Note:** Repeat for each new version

### Step 5: Submit to Store
```bash
npx dapp-store publish submit \
  -k ~/.config/solana/dapp-store-publisher.json \
  -u https://api.mainnet-beta.solana.com \
  --requestor-is-authorized \
  --complies-with-solana-dapp-store-policies
```

### Step 6: Notify Team
1. Join Solana Mobile Discord
2. Get developer role
3. Message `#dapp-store` channel
4. Await review contact

---

## 💰 Monetization

### Commission Structure
- **Current:** 0% commission
- **Future:** Subject to change (will notify developers)

### Our Monetization Strategy
✅ Subscription tiers (Free, Pro $19.99, Whale $99.99)
✅ Stripe payment processing (NOT in-app purchase)
✅ No dApp Store revenue share currently

---

## 📊 Categories

Recommended categories for Solana Alpha Scanner:

**Primary:** `FINANCE`
- Token analysis
- Trading tools
- Portfolio tracking

**Alternative:** `PRODUCTIVITY`
- Tools & utilities
- Analytics

**NOT:** `GAMBLING` (avoid this even if we have "smart money" features)

---

## 🎯 Optimization for Acceptance

### Must-Haves
1. ✅ **Feature Graphic (1200×1200)** → Editor's Choice eligible
2. ✅ **High-quality screenshots** → Professional presentation
3. ✅ **Clear value proposition** → "Avoid rugs, copy profits"
4. ✅ **Security audit** → Best-in-class encryption
5. ✅ **Privacy policy** → Transparent data handling

### Nice-to-Haves
1. ✅ Demo video (30-60 seconds)
2. ✅ Testimonials in description
3. ✅ Active social media (Twitter/Discord)
4. ✅ Website with documentation
5. ✅ Open source (builds trust)

---

## 🚀 Timeline to Submission

### Week 1: Build & Test
- [ ] Complete MVP (Token Scanner + Smart Money)
- [ ] Test on Android device/emulator
- [ ] Security audit & bug fixes

### Week 2: Assets & Legal
- [ ] Create all visual assets
- [ ] Write privacy policy
- [ ] Write copyright policy
- [ ] Prepare listing copy

### Week 3: Build & Sign
- [ ] Build release APK
- [ ] Generate signing key
- [ ] Sign APK
- [ ] Test signed build

### Week 4: Submit
- [ ] Install CLI
- [ ] Mint app NFT
- [ ] Submit to store
- [ ] Notify team on Discord

### Week 5+: Review
- [ ] Wait for review (typically 1-2 weeks)
- [ ] Address feedback if any
- [ ] Launch! 🎉

---

## 📋 Pre-Submission Checklist

### Technical
- [ ] Release APK built & tested
- [ ] Signed with dApp Store key (NOT Google Play key)
- [ ] App runs without crashes
- [ ] Best-in-class security implemented
- [ ] Compatible with Solana Mobile devices

### Assets
- [ ] Icon 512×512
- [ ] Banner 1200×600
- [ ] Feature Graphic 1200×1200 (for Editor's Choice)
- [ ] 4+ screenshots (1080p, same orientation)
- [ ] Optional: Demo video (MP4)

### Legal
- [ ] Privacy policy (live URL)
- [ ] Copyright policy (live URL)
- [ ] EULA/Terms (recommended)
- [ ] No prohibited content
- [ ] Complies with sanctions

### Listing
- [ ] config.yaml complete (no `<< >>` placeholders)
- [ ] Short description (<80 chars)
- [ ] Full description (compelling copy)
- [ ] Category selected (FINANCE)
- [ ] Support URL
- [ ] Publisher details

### Pre-Launch
- [ ] Solana keypair created
- [ ] CLI installed & tested
- [ ] Upload speed >0.25 MB/s
- [ ] Discord account ready
- [ ] SOL for NFT minting (~0.001 SOL)

---

## 🎨 Asset Creation Tips

### Icons
```
Tool: Figma / Adobe Illustrator
Size: 512×512
Export: PNG, transparent background
Style: Simple, recognizable at small sizes
Colors: Brand colors (suggest: purple/blue for Solana)
```

### Screenshots
```
Tool: Android emulator or real device
Resolution: 1920×1080 (portrait) or 1080×1920 (landscape)
Content:
  1. Landing page with tagline
  2. Token scan results
  3. Smart money leaderboard
  4. Wallet tracking
  5. (Optional) Subscription tiers

Tip: Add text overlays explaining features
```

### Banner
```
Size: 1200×600
Content: App name + tagline + key visual
Text: "Solana Alpha Scanner - Scan Tokens. Track Winners."
Visual: Token chart + wallet icons
```

---

## 📞 Support Contacts

- **Docs:** https://docs.solanamobile.com/dapp-publishing/intro
- **Discord:** Solana Mobile Discord (#dapp-store channel)
- **CLI Issues:** GitHub issues on dApp Store CLI repo

---

## 🔮 Post-Approval Strategy

### Launch Day
1. Announce on Twitter
2. Post in r/solana, r/solanacrypto
3. Share in Solana Discord communities
4. Press release (if big enough)

### First Week
1. Monitor reviews & ratings
2. Fix any bugs ASAP
3. Engage with users
4. Track metrics (downloads, active users)

### First Month
1. Release update with user feedback
2. Add requested features
3. Marketing push (referral program?)
4. Aim for Editor's Choice feature

---

**Ready to build & submit? Let's make Solana Alpha Scanner the #1 trading tool on Solana Mobile! 🚀**
