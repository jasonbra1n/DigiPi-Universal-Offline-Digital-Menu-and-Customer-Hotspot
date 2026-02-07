# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Roadmap:** Added Phase 4 (Cloud SaaS & Centralized Management) to `docs/ROADMAP.md`.
- **Documentation:** Added high-level roadmap summary to `README.md`.

### Changed
- **Backend:** Updated `public/includes/functions.php` to accept `store_id` parameter for multi-tenant support.

## [v0.1.1] - 2025-12-24

### Added
- Initial project structure for PHP/MySQL architecture.
- `database/` directory for SQL schemas.
- `public/` directory for web server root.
- `.gemini/` folder for AI context and persona management.
- Documentation for cPanel and LAMP stack deployment in `README.md`.
- **Level 1 Mode:** Root `index.html` for standalone, client-side CSV menu display (no PHP required).
- **Admin Panel:** Basic dashboard structure at `public/admin/index.php`.
- **Sample Data:** Included `sample_products_crystal_shop.csv` for immediate testing.
- **Database Schema:** Updated `database.sql` to v1.1.0 with `stores` and `users` tables, and added `store_id` to all core tables to support future multi-tenant SaaS architecture.

### Changed
- Pivoted backend from Python/Flask to PHP/MySQL to support standard web hosting.
- Updated `CONTRIBUTING.md` with new development setup instructions.