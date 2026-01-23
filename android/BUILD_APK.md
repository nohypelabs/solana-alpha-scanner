# 📦 Building Android APK from PWA

## Prerequisites

1. **Node.js & npm** (already installed)
2. **Java JDK 11+** (for keytool and jarsigner)
3. **Android SDK** (optional but recommended)
4. **Bubblewrap CLI**

---

## Step 1: Install Bubblewrap CLI

```bash
npm install -g @bubblewrap/cli

# Verify installation
bubblewrap --version
```

---

## Step 2: Initialize Bubblewrap Project

**Option A: Using existing twa-manifest.json**

```bash
cd /DataPopOS/projects/solana-alpha-scanner/android

# Initialize from manifest
bubblewrap init --manifest=./twa-manifest.json

# This will create the TWA project structure
```

**Option B: Interactive setup**

```bash
cd /DataPopOS/projects/solana-alpha-scanner/android

# Interactive initialization
bubblewrap init

# Follow prompts:
# - Domain: solana-alpha-scanner.vercel.app
# - Package ID: com.solanaalpha.scanner
# - App Name: Solana Alpha Scanner
# - Launcher Name: Alpha Scanner
# - Theme Color: #9333ea
# - Background Color: #0a0a0a
```

---

## Step 3: Generate Signing Key

**IMPORTANT:** This key is ONLY for Solana dApp Store (NOT Google Play)

```bash
cd /DataPopOS/projects/solana-alpha-scanner/android

# Generate keystore
keytool -genkey -v \
  -keystore solana-dapp-store.keystore \
  -alias alpha-scanner \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000

# You'll be prompted for:
# - Keystore password: [CREATE STRONG PASSWORD]
# - First and last name: Your Name
# - Organization: Solana Alpha
# - City, State, Country: Your details

# SAVE THIS PASSWORD AND FILE SECURELY!
# You'll need it for every app update!
```

**Backup the keystore:**
```bash
cp solana-dapp-store.keystore ~/Backups/
# Or upload to secure cloud storage
```

---

## Step 4: Update Manifest with Signing Key

Edit `twa-manifest.json`:
```json
{
  "signingKey": {
    "path": "./solana-dapp-store.keystore",
    "alias": "alpha-scanner"
  }
}
```

---

## Step 5: Build APK

```bash
cd /DataPopOS/projects/solana-alpha-scanner/android

# Build the APK
bubblewrap build

# You'll be prompted for keystore password
# Output: app-release-signed.apk
```

**Build output location:**
```
android/app/build/outputs/apk/release/app-release-signed.apk
```

---

## Step 6: Verify APK

```bash
# Check APK signing
jarsigner -verify -verbose -certs app-release-signed.apk

# View APK details
aapt dump badging app-release-signed.apk | grep -E "package|launchable-activity|application-label"

# Expected output:
# package: name='com.solanaalpha.scanner'
# application-label:'Alpha Scanner'
```

---

## Step 7: Test APK

**Install on Android device/emulator:**

```bash
# Connect Android device via USB (enable USB debugging)
adb devices

# Install APK
adb install app-release-signed.apk

# Or drag-and-drop APK to emulator
```

**Test checklist:**
- [ ] App launches successfully
- [ ] Shows splash screen
- [ ] Loads PWA content
- [ ] Wallet adapter works
- [ ] Token scanner works
- [ ] Navigation works
- [ ] Offline mode works (airplane mode)

---

## Alternative: PWABuilder Method

If Bubblewrap doesn't work, use PWABuilder:

1. Go to https://www.pwabuilder.com/
2. Enter URL: `https://solana-alpha-scanner.vercel.app`
3. Click "Package for Stores"
4. Select "Android"
5. Configure options:
   - Package ID: `com.solanaalpha.scanner`
   - App name: `Solana Alpha Scanner`
   - Theme color: `#9333ea`
6. Generate signing key (or upload existing)
7. Download APK

---

## Troubleshooting

### Error: "JDK not found"
```bash
# Install OpenJDK 11
sudo apt install openjdk-11-jdk

# Set JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

### Error: "Android SDK not found"
```bash
# Bubblewrap can work WITHOUT Android SDK
# Just use: bubblewrap build --skipSdkCheck
```

### Error: "Manifest fetch failed"
```bash
# Make sure your PWA is deployed first
# Verify manifest.json is accessible:
curl https://solana-alpha-scanner.vercel.app/manifest.json
```

### APK won't install
```bash
# Check minimum Android version (should be 5.0+)
# Verify signature:
jarsigner -verify app-release-signed.apk
```

---

## File Structure After Build

```
android/
├── twa-manifest.json          # TWA configuration
├── solana-dapp-store.keystore # Signing key (KEEP SECURE!)
├── app/
│   └── build/
│       └── outputs/
│           └── apk/
│               └── release/
│                   └── app-release-signed.apk  # FINAL APK
```

---

## Next Steps

1. ✅ Test APK thoroughly on real device
2. ⏳ Create dApp Store assets (icons, screenshots)
3. ⏳ Submit to Solana dApp Store

**APK is ready for dApp Store submission! 🎉**
