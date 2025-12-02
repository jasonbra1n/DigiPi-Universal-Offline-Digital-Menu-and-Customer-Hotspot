# DigiPi Development Progress

## Phase 1: Minimum Viable Product (MVP) - Core Functionality

### P1.1 Initial Server Setup ✅
- [x] Python/Flask app running
- [x] SQLite database implemented
- [x] Basic HTML template rendering
- [x] Virtual environment setup
- [x] Dependencies installed and configured

### P1.2 Basic Data Handling ✅
- [x] CSV parsing script using pandas
- [x] API endpoint to retrieve all data (`/api/products`)
- [x] Simple table view on the frontend
- [x] Dynamic column detection from CSV

### P1.3 Admin Panel MVP ✅
- [x] Admin route (`/admin`) established
- [x] File upload form
- [x] Display for product list
- [x] Success/error messaging
- [x] Product count display

### P1.4 Network Provisioning ⏸️
- [ ] Temporary AP script
- [ ] Web configuration form for Wi-Fi credentials
- [ ] Auto-kiosk mode launch on HDMI
- **Note**: Deferred until deployment on Raspberry Pi hardware

---

## Phase 2: Enhanced Functionality and Universal Adaptability

### P2.1 Universal Menu Builder ✅
- [x] Admin UI to show/hide columns
- [x] Sorting logic via API query
- [x] Field visibility settings stored in database
- [x] Column order configuration

### P2.2 Dynamic Display/Kiosk ✅
- [x] Non-scrolling, fixed-size table layout
- [x] Timed JavaScript pagination (auto page-flipping)
- [x] QR code generation for menu URL
- [x] Configurable display duration per page

### P2.3 Multi-View Support ⏳
- [ ] Database schema updated for multiple configurations
- [ ] Admin UI tabbed interface for creating new views
- [ ] Unique view URLs (`/1`, `/2`, `/3`) implemented
- [ ] Per-view settings (columns, sorting, filtering)

### P2.4 Unique Hostname ⏳
- [ ] Script to generate unique hostname from MAC address
- [ ] `digipi-xxxx.local` hostname implementation
- [ ] mDNS/Avahi configuration
- **Note**: Requires Raspberry Pi hardware for testing

---

## Phase 3: Customer Engagement, Hotspot, and Pro-Plan Foundation

### P3.1 Customer Hotspot ⏳
- [ ] DigiPi configured as Access Point (AP)
- [ ] Traffic routing established
- [ ] Firewall for network isolation
- [ ] `hostapd` and `dnsmasq` configuration

### P3.2 Captive Portal ⏳
- [ ] Captive portal service active on public network
- [ ] HTML splash page with store URL redirect
- [ ] DNS hijacking for captive portal detection

### P3.3 Head Office Sync (Pro Foundation) ⏳
- [ ] Basic authentication and security hardening
- [ ] API documentation for remote sync
- [ ] Multi-location management foundation

### P3.4 Feature Polishing ⏳
- [ ] Live preview in Admin Panel
- [ ] User-friendly styling improvements
- [ ] Error handling and validation
- [ ] Production deployment guide

---

## Legend
- ✅ Completed
- 🚧 In Progress
- ⏳ Not Started
- ⏸️ Deferred (requires hardware/deployment)

---

## Current Status Summary

**Completed**: 3/4 Phase 1 items (75%)  
**In Progress**: Phase 2.1 Universal Menu Builder  
**Next Up**: Phase 2.2 Dynamic Display/Kiosk

**Last Updated**: 2025-12-02
