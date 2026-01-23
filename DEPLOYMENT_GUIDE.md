# 🚀 Deployment Guide - Solana Alpha Scanner

## Current Status: PWA Ready ✅

The app is now a Progressive Web App and ready for deployment and conversion to Android APK.

---

## 📱 PWA Features Implemented

- ✅ Service Worker for offline support
- ✅ Web App Manifest (manifest.json)
- ✅ Responsive design (mobile-first)
- ✅ Dark mode optimized
- ✅ Installable on mobile devices
- ✅ Apple Touch Icon support

---

## 🔧 Local Development

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m app.main
```

Backend runs on: http://localhost:8000

### Frontend
```bash
cd frontend
pnpm install
pnpm dev
```

Frontend runs on: http://localhost:3000

---

## ☁️ Production Deployment

### 1. Backend (Railway.app - Free Tier)

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Deploy backend
cd backend
railway init
railway up
```

Set environment variables in Railway dashboard:
- `DATABASE_URL` (Supabase PostgreSQL)
- `HELIUS_API_KEY`
- `REDIS_URL` (Upstash Redis)

### 2. Frontend (Vercel - Free Tier)

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy frontend
cd frontend
vercel --prod
```

Set environment variables in Vercel:
- `NEXT_PUBLIC_API_URL` (Railway backend URL)
- `NEXT_PUBLIC_RPC_URL`

---

## 📦 Convert PWA to Android APK (TWA - Trusted Web Activity)

### Option 1: Using Bubblewrap (Recommended)

```bash
# Install Bubblewrap
npm install -g @bubblewrap/cli

# Initialize TWA project
cd /DataPopOS/projects/solana-alpha-scanner
mkdir android-twa
cd android-twa

bubblewrap init --manifest=https://your-deployed-app.vercel.app/manifest.json

# Configure signing key
bubblewrap build

# Output: app-release-signed.apk
```

### Option 2: Using PWABuilder

1. Go to https://www.pwabuilder.com/
2. Enter your deployed URL
3. Click "Package for Stores"
4. Select "Android"
5. Download APK

### Option 3: Manual with Android Studio

1. Create new Android Studio project (Empty Activity)
2. Add TWA dependency to `build.gradle`
3. Configure `AndroidManifest.xml` with PWA URL
4. Generate signing key
5. Build release APK

---

## 🔑 Signing Key for dApp Store

**IMPORTANT:** Create a SEPARATE signing key for Solana dApp Store (NOT the same as Google Play)

```bash
# Generate keystore
keytool -genkey -v -keystore solana-dapp-store.keystore \
  -alias alpha-scanner \
  -keyalg RSA -keysize 2048 -validity 10000

# Save this file securely - needed for updates!
```

Sign APK:
```bash
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 \
  -keystore solana-dapp-store.keystore \
  app-release-unsigned.apk alpha-scanner

# Zipalign
zipalign -v 4 app-release-unsigned.apk SolanaAlphaScanner.apk
```

---

## 🎨 Assets Needed for dApp Store

### Icons
- ✅ 512×512 PNG (app icon) - `frontend/public/icon-512.png`
- ⏳ Need actual design (currently placeholder)

### Banners
- ⏳ 1200×600 PNG (store listing header)
- ⏳ 1200×1200 PNG (feature graphic for Editor's Choice)

### Screenshots
- ⏳ 4+ screenshots at 1080p resolution
- ⏳ All same orientation (portrait recommended)
- ⏳ Capture from actual app:
  1. Landing page
  2. Token Scanner with results
  3. Smart Money Leaderboard
  4. Recent Signals feed

### Legal Documents
- ⏳ Privacy Policy (host at: solana-alpha.app/privacy)
- ⏳ Copyright Policy (host at: solana-alpha.app/copyright)

---

## 📝 Solana dApp Store Submission

### Prerequisites
1. ✅ Release APK built and signed
2. ⏳ All assets created (icons, banners, screenshots)
3. ⏳ Privacy policy published
4. ⏳ Copyright policy published
5. ✅ Solana wallet with ~0.001 SOL for NFT minting

### Submission Steps

```bash
# 1. Install dApp Store CLI
npm install -g @solana-mobile/dapp-store-cli

# 2. Create Solana keypair for publisher
solana-keygen new --outfile ~/.config/solana/alpha-scanner-publisher.json

# 3. Create config.yaml
cat > config.yaml <<EOF
publisher:
  name: "Your Name"
  website: "https://solana-alpha.app"
  email: "dev@solana-alpha.app"

app:
  name: "Solana Alpha Scanner"
  android_package_name: "com.solanaalpha.scanner"
  urls:
    support_url: "https://solana-alpha.app/support"
    privacy_policy_url: "https://solana-alpha.app/privacy"
    copyright_policy_url: "https://solana-alpha.app/copyright"

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
      category: "FINANCE"
EOF

# 4. Mint app NFT
npx dapp-store create release \
  -k ~/.config/solana/alpha-scanner-publisher.json \
  -b /path/to/android/sdk/build-tools

# 5. Submit to store
npx dapp-store publish submit \
  -k ~/.config/solana/alpha-scanner-publisher.json \
  -u https://api.mainnet-beta.solana.com \
  --requestor-is-authorized \
  --complies-with-solana-dapp-store-policies

# 6. Join Solana Mobile Discord
# - Get developer role
# - Message #dapp-store channel
# - Wait for review contact
```

---

## 🎯 Post-Deployment Checklist

### MVP Launch
- [ ] Backend deployed to Railway
- [ ] Frontend deployed to Vercel
- [ ] Database configured (Supabase)
- [ ] Environment variables set
- [ ] Test all features in production

### PWA Testing
- [ ] Install on Android device
- [ ] Test offline mode
- [ ] Verify manifest.json loads
- [ ] Check service worker registration

### APK Testing
- [ ] Install APK on Android device
- [ ] Verify wallet adapter works
- [ ] Test token scanning
- [ ] Test smart money tracker

### dApp Store Ready
- [ ] All assets created and optimized
- [ ] Privacy & copyright policies live
- [ ] APK signed with dApp Store key
- [ ] config.yaml complete
- [ ] Submit and notify team

---

## 🔮 Future Enhancements

### Phase 2
- Telegram bot integration
- Discord notifications
- Email alerts for tracked wallets

### Phase 3
- Portfolio tracking
- Tax reporting
- Copy trading automation

### Phase 4
- NFT analysis
- Cross-chain support (Ethereum, Base)
- White-label for other projects

---

## 📊 Analytics & Monitoring

### Metrics to Track
- Daily Active Users (DAU)
- Tokens scanned per day
- Free → Pro conversion rate
- Churn rate
- API response times

### Tools
- Vercel Analytics (frontend)
- Railway Metrics (backend)
- Supabase Dashboard (database)
- Custom dashboard (build later)

---

## 💰 Monetization Tiers

### Free (Viral Growth)
- Unlimited token scans
- View top 10 smart money wallets
- 24h delayed signals

### Pro ($19.99/month)
- Real-time signals
- Track up to 10 wallets
- Telegram alerts
- Full leaderboard access

### Whale ($99.99/month)
- Track unlimited wallets
- Priority alerts
- API access
- Custom alert rules
- Portfolio analytics

---

## 🆘 Troubleshooting

### Backend Issues
```bash
# Check logs
railway logs

# Restart service
railway up --detach
```

### Frontend Issues
```bash
# Check build
vercel logs

# Rebuild
vercel --prod --force
```

### APK Issues
```bash
# Verify signing
jarsigner -verify -verbose -certs app.apk

# Check manifest
aapt dump badging app.apk
```

---

**Ready to deploy! 🚀**
