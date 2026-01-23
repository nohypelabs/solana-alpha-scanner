# 🎨 Asset Creation Guide - Solana dApp Store

## Required Assets Checklist

### Icons ✅ (Priority 1)
- [ ] **512×512 PNG** - App launcher icon
- [ ] **192×192 PNG** - PWA icon (smaller)

### Banners ⚠️ (Priority 2)
- [ ] **1200×600 PNG** - Store listing header
- [ ] **1200×1200 PNG** - Feature Graphic (Editor's Choice eligible)

### Screenshots 📱 (Priority 3)
- [ ] **4+ screenshots** at 1080p (1920×1080 landscape OR 1080×1920 portrait)
- [ ] All same orientation
- [ ] All same aspect ratio

### Optional 🎬
- [ ] Demo video (30-60 seconds, MP4)

---

## 🎯 Icon Design (512×512)

### Design Specifications
- **Size:** 512×512 pixels
- **Format:** PNG with transparency
- **Safe zone:** Keep important elements within 448×448 center
- **Corners:** Will be rounded by system (design with rounded corners)

### Design Ideas

**Option 1: Scanner Icon**
```
Background: Purple gradient (#9333ea to #ec4899)
Icon: White magnifying glass with "Solana logo" inside
Text: "ALPHA" below in bold white
```

**Option 2: Minimal Logo**
```
Background: Dark purple (#581c87)
Icon: Stylized "A" (for Alpha) in neon green (#10b981)
Accent: Small Solana triangle in corner
```

**Option 3: Token + Wallet**
```
Background: Black to purple gradient
Icon: Solana token (S symbol) + wallet icon combined
Glow effect: Purple glow around icons
```

### Tools to Use

**Free Tools:**
1. **Canva** (easiest)
   - Templates for app icons
   - Drag-and-drop design
   - Export as PNG
   - URL: canva.com

2. **Figma** (professional)
   - More control
   - Vector-based
   - Free tier available
   - URL: figma.com

3. **GIMP** (open source)
   - Photoshop alternative
   - Linux compatible
   - Free forever

**AI Tools:**
1. **DALL-E 3** (via ChatGPT Plus)
   - Prompt: "App icon for crypto token scanner, purple gradient, Solana theme, modern minimal, 512x512"

2. **Midjourney**
   - Similar prompts

### Quick Template (Figma)

1. Create 512×512 frame
2. Add purple gradient background (#9333ea → #ec4899)
3. Add white magnifying glass icon (from icons8.com)
4. Add "ALPHA" text (Poppins Bold, 72px, white)
5. Add subtle shadow/glow
6. Export as PNG (2x for high DPI)

---

## 📐 Banner Design (1200×600)

### Design Specifications
- **Size:** 1200×600 pixels
- **Format:** PNG or JPG
- **Text safe zone:** Keep text within center 1000×400
- **File size:** < 1MB

### Design Template

```
Layout:
┌────────────────────────────────────────┐
│  [Logo]  Solana Alpha Scanner          │
│           Scan Tokens. Track Winners.  │
│                                         │
│  [Screenshot]  [Screenshot]             │
│   Token Scan   Leaderboard              │
└────────────────────────────────────────┘
```

### Content
- **Left 1/3:** App logo + name
- **Center:** Tagline "Scan Tokens. Track Winners. Copy Profits."
- **Right 2/3:** 2-3 small screenshots of UI
- **Background:** Purple gradient with Solana-themed graphics

---

## 🏆 Feature Graphic (1200×1200)

**This unlocks "Editor's Choice" eligibility!**

### Design Specifications
- **Size:** 1200×1200 pixels
- **Format:** PNG or JPG
- **Important:** No text in outer 10% (Solana may overlay badges)

### Design Ideas

**Hero Layout:**
```
┌──────────────────────────┐
│                          │
│    [Large Phone Mock]    │
│   showing Token Scan     │
│                          │
│  "Find Alpha Before      │
│   Everyone Else"         │
│                          │
│  ⭐⭐⭐⭐⭐ 5-star        │
└──────────────────────────┘
```

**Stats-Focused:**
```
┌──────────────────────────┐
│  10,000+ Tokens Scanned  │
│  500+ Smart Wallets      │
│  $2M+ Rugs Avoided       │
│                          │
│  [App Screenshots]       │
│                          │
│  "Your Edge in Solana    │
│   Token Trading"         │
└──────────────────────────┘
```

---

## 📸 Screenshots Guide

### Requirements
- **Minimum:** 4 screenshots
- **Resolution:** 1080p (1920×1080 or 1080×1920)
- **Orientation:** ALL must be same (recommend portrait)
- **Aspect ratio:** ALL must be equal
- **Format:** PNG or JPG

### Screenshot Ideas

**Screenshot 1: Landing Page**
- Show hero section
- Wallet connect button prominent
- Feature highlights visible
- Caption: "Professional Token Analysis"

**Screenshot 2: Token Scanner Results**
- Show completed token scan
- Risk score clearly visible (preferably "SAFE" or "CAUTION")
- Metrics displayed (holders, liquidity, etc.)
- Top holders list
- Caption: "Instant Risk Analysis"

**Screenshot 3: Smart Money Leaderboard**
- Show leaderboard with top 10 wallets
- Green P&L numbers visible
- Medal emojis for top 3
- Caption: "Track Profitable Wallets"

**Screenshot 4: Recent Signals**
- Show trading signals feed
- Mix of BUY/SELL indicators
- Wallet ranks visible
- Timestamps showing recency
- Caption: "Real-time Trading Signals"

**Screenshot 5 (Optional): Wallet Details**
- Individual wallet deep dive
- Performance metrics
- Recent activity
- Caption: "Copy Smart Money Trades"

### How to Capture

**Desktop (Chrome DevTools):**
```bash
1. Open app in Chrome
2. Press F12 (DevTools)
3. Toggle device toolbar (Ctrl+Shift+M)
4. Select device: "Pixel 5" (1080×2340)
5. Navigate to page
6. Right-click → "Capture screenshot"
7. Save as PNG
```

**Android Device:**
```bash
1. Connect device via USB
2. Enable USB debugging
3. Use: adb shell screencap -p /sdcard/screenshot.png
4. Pull: adb pull /sdcard/screenshot.png
```

**Emulator:**
```bash
# Android Studio emulator has built-in screenshot button
# Or use: adb emu screenrecord start
```

### Screenshot Enhancement

**Add text overlays (Figma/Canva):**
1. Import screenshot
2. Add dark gradient overlay (bottom 20%)
3. Add feature title in white text
4. Add 1-line description
5. Export as PNG

**Example:**
```
┌─────────────────────┐
│                     │
│  [App Screenshot]   │
│                     │
│  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │ ← Gradient overlay
│  Risk Analysis      │ ← Title
│  Instant results    │ ← Description
└─────────────────────┘
```

---

## 🎬 Demo Video (Optional)

### Specifications
- **Length:** 30-60 seconds
- **Format:** MP4
- **Min resolution:** 720×720
- **Max file size:** 15MB

### Script Example

```
0:00 - Logo animation + app name
0:05 - "Scan any Solana token"
0:10 - Show token scan in action
0:15 - Risk score appears (SAFE/CAUTION/SCAM)
0:20 - "Track profitable wallets"
0:25 - Show smart money leaderboard
0:30 - "Get real-time signals"
0:35 - Show recent trades feed
0:40 - "Download now on Solana dApp Store"
0:45 - End screen with logo
```

### Tools
- **OBS Studio** (screen recording)
- **ScreenToGif** (simple recordings)
- **DaVinci Resolve** (editing, free)
- **Canva Video** (simple edits)

---

## 🚀 Quick Start (15 Minutes)

**Minimum Viable Assets:**

1. **Icon (5 min - Canva)**
   - Use template: "App Icon"
   - Purple gradient background
   - Add magnifying glass icon
   - Add "ALPHA" text
   - Export 512×512 PNG

2. **Screenshots (5 min - Chrome DevTools)**
   - Landing page
   - Token scan result
   - Leaderboard
   - Signals feed
   - Export as 1080×1920 PNG

3. **Banner (5 min - Canva)**
   - Use template: "App Store Feature Graphic"
   - Add app name + tagline
   - Add 2 screenshots
   - Export 1200×600 PNG

**Done! Ready for submission.**

---

## 📋 Asset Checklist Template

```
Assets Created:
✅ Icon 512×512 PNG
✅ Icon 192×192 PNG
✅ Banner 1200×600 PNG
✅ Feature Graphic 1200×1200 PNG
✅ Screenshot 1 (Landing)
✅ Screenshot 2 (Scanner)
✅ Screenshot 3 (Leaderboard)
✅ Screenshot 4 (Signals)
⬜ Screenshot 5 (Optional)
⬜ Demo Video (Optional)

File Sizes:
Icon: ____ KB (< 100KB recommended)
Banner: ____ KB (< 500KB recommended)
Feature: ____ KB (< 1MB recommended)
Screenshots: ____ KB each (< 500KB each)

Quality Check:
✅ All PNG/JPG format
✅ Correct dimensions
✅ No text cutoff
✅ High resolution
✅ Consistent branding
```

---

## 🎯 Design Principles

### Color Palette
- **Primary:** Purple #9333ea
- **Secondary:** Pink #ec4899
- **Accent:** Green #10b981
- **Background:** Black #0a0a0a
- **Text:** White #ffffff

### Typography
- **Headings:** Poppins Bold
- **Body:** Inter Regular
- **Monospace:** JetBrains Mono (for wallet addresses)

### Style Guide
- Modern, sleek, professional
- Crypto/DeFi aesthetic
- Dark mode optimized
- Purple/pink gradients
- Glowing effects
- Minimal but impactful

---

**Ready to create! 🎨**

Tools needed: Canva (free) + Chrome DevTools
Time needed: 15-30 minutes
Difficulty: Easy

After creating assets, save to:
`/DataPopOS/projects/solana-alpha-scanner/assets/`
