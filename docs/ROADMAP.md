# 🗺️ DigiPi Digital Menu and Customer Hotspot System: Roadmap

This roadmap is organized into three phases, starting with the core functionality required for a Minimum Viable Product (MVP) and building toward advanced features and scalability.

## Phase 1: Minimum Viable Product (MVP) - Core Functionality

| Goal | Description | Deliverables |
| :--- | :--- | :--- |
| **P1.1 Initial Server Setup** | Establish the base web server environment and persistence. | PHP environment configured; MySQL database schema imported; `config.php` created. |
| **P1.2 Basic Data Handling** | Implement core data ingestion and display logic. | PHP CSV parser; PDO Database connection; simple, non-paginated table view on the frontend. |
| **P1.3 Admin Panel MVP** | Create a basic admin UI for data upload and initial content management. | Admin PHP pages created; File upload handling; display for product list; single button to save settings. |
| **P1.4 Network Provisioning** | Implement the first-boot setup flow. | Temporary AP script; web configuration form for Wi-Fi credentials; auto-kiosk mode launch on HDMI. |

## Phase 2: Enhanced Functionality and Universal Adaptability

| Goal | Description | Deliverables |
| :--- | :--- | :--- |
| **P2.1 Universal Menu Builder** | Implement dynamic data column management. | Admin UI allows hiding/showing any column found in the CSV; sorting logic implemented via API query. |
| **P2.2 Dynamic Display/Kiosk** | Refine the customer view to meet specific design requirements. | Non-scrolling, fixed-size table layout; timed JavaScript pagination (page-flipping); QR code generation; configurable display duration; dynamic page titles based on primary sort. |
| **P2.3 Multi-View Support** | Enable the DigiPi to serve multiple menu configurations. | Database schema updated to support multiple configurations; Admin UI tabbed interface for creating new views (e.g., View 2); unique view URLs (`/2`, `/3`) implemented. |
| **P2.4 Unique Hostname** | Ensure device identification on the local network. | Script to generate unique hostname (`digipi-xxxx.local`) from MAC address fragments. |
| **P2.5 Visual Theming** | Provide aesthetic variety for different business types. | 5 pre-made CSS themes (e.g., Dark/Light, Chalkboard, Minimalist, Vibrant); Admin selector for active theme. |

## Phase 3: Customer Engagement, Hotspot, and Pro-Plan Foundation

| Goal | Description | Deliverables |
| :--- | :--- | :--- |
| **P3.1 Customer Hotspot** | Implement the dual-network functionality. | DigiPi configured to run as an Access Point (AP); traffic routing and firewall established for network isolation. |
| **P3.2 Captive Portal** | Implement the online store marketing feature. | Captive portal service active on the public network; HTML splash page with mandatory redirect/link to the configured online store URL. |
| **P3.3 Head Office Sync (Pro Foundation)** | Lay the groundwork for centralized management. | Basic authentication and security hardening; API documentation for future remote data synchronization (Pro Plan). |
| **P3.4 Feature Polishing** | Finalize UI/UX for commercial readiness. | Live preview functionality in the Admin Panel; user-friendly styling and error handling. |
| **P3.5 Advanced Customization** | Enable deep visual control for brand alignment. | Font selection; font size controls; theme import/export functionality for custom CSS. |

## Phase 4: Cloud SaaS & Centralized Management (Long Term)

| Goal | Description | Deliverables |
| :--- | :--- | :--- |
| **P4.1 Cloud Platform Core** | Establish a centralized, multi-tenant web platform. | SaaS infrastructure; User accounts/Auth; Subscription billing integration (e.g., Stripe). |
| **P4.2 Cloud Menu Builder** | Web-based version of the Admin Panel. | Users can upload CSVs and configure menus via a public website instead of a local IP. |
| **P4.3 Screen-as-a-Service** | Direct-to-Cloud display mode. | Unique public URLs (e.g., `app.digipi.io/s/store-name`) to run menus on Smart TVs without local hardware. |
| **P4.4 Hybrid Sync** | Bridge local offline units with the cloud. | Mechanism for local DigiPi units to pull configs from the cloud account or push analytics up. |

## Phase 4: Cloud SaaS & Centralized Management (Long Term)

| Goal | Description | Deliverables |
| :--- | :--- | :--- |
| **P4.1 Cloud Platform Core** | Establish a centralized, multi-tenant web platform. | SaaS infrastructure; User accounts/Auth; Subscription billing integration (e.g., Stripe). |
| **P4.2 Cloud Menu Builder** | Web-based version of the Admin Panel. | Users can upload CSVs and configure menus via a public website instead of a local IP. |
| **P4.3 Screen-as-a-Service** | Direct-to-Cloud display mode. | Unique public URLs (e.g., `app.digipi.io/s/store-name`) to run menus on Smart TVs without local hardware. |
| **P4.4 Hybrid Sync** | Bridge local offline units with the cloud. | Mechanism for local DigiPi units to pull configs from the cloud account or push analytics up. |
