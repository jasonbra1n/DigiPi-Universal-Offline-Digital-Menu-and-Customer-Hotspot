# 💻 DigiPi Digital Menu and Customer Hotspot System: Project Plan

## 1. Project Overview

The DigiPi system is a self-contained, offline-first digital signage server designed for retail environments (e.g., cannabis dispensaries, crystal shops, QSRs). It uses a low-cost single-board computer (like a Raspberry Pi) to host a local web server, providing a dynamic product menu and an isolated customer Wi-Fi hotspot.

## 2. Core Architecture and Network Design

The system employs a **Dual Network Architecture** to ensure security and functionality.

### 2.1 Hardware
* **Server:** 1x DigiPi (Raspberry Pi or similar SBC).
* **Display Nodes (Clients):** Any web-enabled device (secondary DigiPi, Fire Stick, Chromecast, Smart TV) running a full-screen web browser in kiosk mode.

### 2.2 Network & Identification
| Network Segment | Purpose | Access/Host | Addressing |
| :--- | :--- | :--- | :--- |
| **Private Store Network** | Internal connectivity for Admin Panel and Display Node data updates. | Store's Router/Wi-Fi | **Unique Hostname:** `http://digipi-xxxx.local/` (where `xxxx` is derived from the MAC address). |
| **Public Customer Hotspot** | Provides isolated, free Wi-Fi access for customers to browse the online store. | DigiPi acts as an Access Point (AP). | **Captive Portal:** Redirects all initial connections to the pre-set online store URL. |

### 2.3 Technology Stack
* **Operating System:** Linux (e.g., Raspberry Pi OS, customized for kiosk mode).
* **Web Framework:** Python (Flask or Django) for the application server and API.
* **Database:** SQLite (file-based) for local, persistent storage of product data and settings.
* **Frontend:** HTML5, CSS3, JavaScript (for dynamic updates and pagination).

## 3. Key Feature Specifications

### 3.1 Initial Provisioning (First Boot Setup)
1.  **Temporary AP Mode:** On first boot, the DigiPi broadcasts its own configuration Wi-Fi.
2.  **QR Code Display:** The HDMI output displays a QR code for quick connection to the temporary AP.
3.  **Web Configuration:** A captive portal forces the user to a setup page to input:
    * Store's Private Wi-Fi credentials.
    * Customer Hotspot SSID/Password.
    * Store's Official Online URL (for captive portal redirect).
4.  **Auto-Kiosk Launch:** Upon successful connection to the store network, the DigiPi automatically launches a web browser in full-screen kiosk mode, opening its own menu URL (`http://digipi-xxxx.local/`).

### 3.2 Dynamic Digital Menu Server
* **Offline Data Access:** Menu data is pulled directly from the local SQLite database.
* **Static Display:** The customer-facing view contains no buttons, scrollbars, or interactive elements.
* **Timed Pagination:** JavaScript handles periodic API calls for data updates and cycles the display through multiple "pages" of content if the product list exceeds the screen limit.

### 3.3 Universal Admin Control Panel (`/admin`)
* **Data Ingestion:** File upload feature to accept CSV data. The system dynamically reads the CSV headers to identify all available product variables (e.g., `THC_Level`, `Price_per_Gram`).
* **Universal Menu Builder:** For each unique variable/column found in the data, the admin can set options:
    * **Visible/Hidden:** Toggle for the customer display.
    * **Sort Key:** Define primary and secondary sort order.
* **Multi-Display Management:** A tabbed interface to create and manage independent menu configurations.
    * Each tab corresponds to a unique display URL (e.g., `/1`, `/2`, `/3`).
    * Each display can have different product sorting, hidden columns, or even filtered product sets.
* **Display QR Codes:** Generate QR codes on the admin page for quick connection of new display nodes.

### 3.4 Customer Hotspot (Captive Portal)
* **Network Isolation:** The customer network is firewalled from the store's private network.
* **Internet Gateway:** Traffic is routed through the DigiPi's existing internet connection.
* **Mandatory Redirect:** Customers connecting to the public Wi-Fi are forced to a splash page with a prominent link to the store's official online URL, serving as a marketing and sales tool.
