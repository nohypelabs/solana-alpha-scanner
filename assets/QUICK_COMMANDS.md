# ⚡ Quick Commands Cheat Sheet

## 🔨 Build APK

```bash
# Navigate to android folder
cd /DataPopOS/projects/solana-alpha-scanner/android

# Option 1: Using Bubblewrap (Recommended)
npm install -g @bubblewrap/cli
bubblewrap init --manifest=./twa-manifest.json
bubblewrap build

# Option 2: Using PWABuilder
# Visit: https://www.pwabuilder.com/
# Enter URL: your-deployed-url.vercel.app
# Download APK

# Generate signing key (FIRST TIME ONLY)
keytool -genkey -v -keystore solana-dapp-store.keystore \
  -alias alpha-scanner -keyalg RSA -keysize 2048 -validity 10000
```

**Output:** `app/build/outputs/apk/release/app-release-signed.apk`

---

## 📸 Capture Screenshots

```bash
# Using Chrome DevTools
# 1. Open app in Chrome
# 2. Press F12
# 3. Ctrl+Shift+M (device toolbar)
# 4. Select "Pixel 5" (1080×2340)
# 5. Right-click → Capture screenshot

# Or using Android device
adb shell screencap -p /sdcard/screenshot.png
adb pull /sdcard/screenshot.png ./assets/
```

**Pages to capture:**
1. http://localhost:3000/ (Landing)
2. http://localhost:3000/scan (with token address entered)
3. http://localhost:3000/tracker (Leaderboard tab)
4. http://localhost:3000/tracker (Signals tab)

---

## 🎨 Convert SVG Icon to PNG

```bash
# Using ImageMagick
cd /DataPopOS/projects/solana-alpha-scanner/assets

# Install ImageMagick (if not installed)
sudo apt install imagemagick

# Convert SVG to PNG
convert -background none icon-template.svg -resize 512x512 icon-512.png
convert -background none icon-template.svg -resize 192x192 icon-192.png

# Or use online tool: https://svgtopng.com/
```

---

## 🚀 Deploy to Production

```bash
# Frontend (Vercel)
cd /DataPopOS/projects/solana-alpha-scanner/frontend
npm install -g vercel
vercel --prod

# Backend (Railway)
cd /DataPopOS/projects/solana-alpha-scanner/backend
npm install -g @railway/cli
railway login
railway init
railway up
```

---

## 🧪 Test APK

```bash
# Install on device
adb install app-release-signed.apk

# View logs
adb logcat | grep -i "alpha"

# Uninstall
adb uninstall com.solanaalpha.scanner

# Check device
adb devices
```

---

## ✅ Verify Assets

```bash
cd /DataPopOS/projects/solana-alpha-scanner/assets

# Check icon sizes
identify icon-512.png  # Should be 512x512
identify icon-192.png  # Should be 192x192

# Check screenshot sizes
identify screenshot-*.png  # Should be 1080x1920 or 1920x1080

# Check banner sizes
identify banner.png  # Should be 1200x600
identify feature-graphic.png  # Should be 1200x1200

# Check file sizes
ls -lh *.png
# Icons: < 100KB
# Screenshots: < 500KB each
# Banners: < 1MB
```

---

## 📦 Package for dApp Store

```bash
# Install dApp Store CLI
npm install -g @solana-mobile/dapp-store-cli

# Create publisher keypair
solana-keygen new --outfile ~/.config/solana/alpha-scanner-publisher.json

# Mint app NFT
npx dapp-store create release \
  -k ~/.config/solana/alpha-scanner-publisher.json \
  -b /path/to/android-sdk/build-tools

# Submit to store
npx dapp-store publish submit \
  -k ~/.config/solana/alpha-scanner-publisher.json \
  -u https://api.mainnet-beta.solana.com \
  --requestor-is-authorized \
  --complies-with-solana-dapp-store-policies
```

---

## 🔍 Debug Commands

```bash
# Check manifest.json accessibility
curl https://your-app.vercel.app/manifest.json

# Verify APK signature
jarsigner -verify -verbose app-release-signed.apk

# View APK contents
aapt dump badging app-release-signed.apk

# Check Java version
java -version  # Should be 11+

# Check Android SDK
echo $ANDROID_HOME
```

---

## 📋 Pre-Submission Checklist

```bash
# Run this before submitting
cd /DataPopOS/projects/solana-alpha-scanner

# 1. Check all files exist
ls -la assets/icon-512.png
ls -la assets/icon-192.png
ls -la assets/banner.png
ls -la assets/feature-graphic.png
ls -la assets/screenshot-*.png
ls -la android/app/build/outputs/apk/release/app-release-signed.apk

# 2. Verify APK
jarsigner -verify android/app/build/outputs/apk/release/app-release-signed.apk

# 3. Test on device
adb install android/app/build/outputs/apk/release/app-release-signed.apk

# 4. Check deployment
curl https://your-app.vercel.app/
curl https://your-api.railway.app/health
```

---

## 🎯 One-Liner Commands

```bash
# Build everything
cd /DataPopOS/projects/solana-alpha-scanner && \
  cd frontend && pnpm build && cd .. && \
  cd android && bubblewrap build

# Deploy everything
cd /DataPopOS/projects/solana-alpha-scanner && \
  cd frontend && vercel --prod && cd .. && \
  cd backend && railway up

# Generate all icons from SVG
convert -background none assets/icon-template.svg -resize 512x512 assets/icon-512.png && \
  convert -background none assets/icon-template.svg -resize 192x192 assets/icon-192.png && \
  convert -background none assets/icon-template.svg -resize 1200x1200 assets/feature-graphic.png
```

---

## 🆘 Common Issues & Fixes

**Issue: "JDK not found"**
```bash
sudo apt install openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

**Issue: "Android SDK not found"**
```bash
# Download Android SDK
wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip
unzip commandlinetools-linux-9477386_latest.zip
export ANDROID_HOME=$PWD/cmdline-tools
```

**Issue: "Manifest not found"**
```bash
# Make sure app is deployed first
vercel --prod
# Then verify:
curl https://your-app.vercel.app/manifest.json
```

**Issue: "APK won't install"**
```bash
# Enable USB debugging on phone
# Settings → About Phone → Tap "Build Number" 7 times
# Settings → Developer Options → Enable USB Debugging

# Then reconnect device
adb kill-server
adb start-server
adb devices
```

---

**Save this file for quick reference! 💾**
