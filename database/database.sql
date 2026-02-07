-- DigiPi Database Schema
-- Version: 1.1.0 (SaaS-Ready)

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Table structure for table `stores`
-- Single row for local DIY, multiple rows for Cloud SaaS.
--
CREATE TABLE IF NOT EXISTS `stores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `name` varchar(255) NOT NULL DEFAULT 'My DigiPi Store',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Default Store (Local)
--
INSERT INTO `stores` (`id`, `uuid`, `name`) VALUES
(1, UUID(), 'Local DigiPi Store');

--
-- Table structure for table `users`
--
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `store_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `store_id` (`store_id`),
  CONSTRAINT `fk_users_store` FOREIGN KEY (`store_id`) REFERENCES `stores` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Default Admin User (admin / admin) - Change on first login!
--
INSERT INTO `users` (`store_id`, `username`, `password_hash`) VALUES
(1, 'admin', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi');

--
-- Table structure for table `products`
-- Stores imported CSV data. 'data' column holds dynamic fields (Price, THC, etc.) as JSON.
--
CREATE TABLE IF NOT EXISTS `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `store_id` int(11) NOT NULL DEFAULT 1,
  `uuid` varchar(36) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `data` json DEFAULT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `store_id` (`store_id`),
  CONSTRAINT `fk_products_store` FOREIGN KEY (`store_id`) REFERENCES `stores` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `settings`
-- Global system configuration (Store Name, Wi-Fi SSID, etc.)
--
CREATE TABLE IF NOT EXISTS `settings` (
  `store_id` int(11) NOT NULL DEFAULT 1,
  `setting_key` varchar(50) NOT NULL,
  `setting_value` text DEFAULT NULL,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`store_id`, `setting_key`),
  CONSTRAINT `fk_settings_store` FOREIGN KEY (`store_id`) REFERENCES `stores` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Default Settings
--
INSERT INTO `settings` (`store_id`, `setting_key`, `setting_value`) VALUES
(1, 'store_name', 'My DigiPi Store'),
(1, 'wifi_ssid', 'DigiPi_Hotspot'),
(1, 'kiosk_mode', '1'),
(1, 'refresh_interval', '30');

--
-- Table structure for table `displays`
-- Manages multiple screens (e.g., ?display=1, ?display=2)
--
CREATE TABLE IF NOT EXISTS `displays` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `store_id` int(11) NOT NULL DEFAULT 1,
  `display_identifier` varchar(50) NOT NULL COMMENT 'URL slug (e.g. 1, 2) or MAC',
  `name` varchar(100) NOT NULL DEFAULT 'New Display',
  `config` json DEFAULT NULL COMMENT 'Per-display settings (hidden cols, sort)',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_display` (`store_id`, `display_identifier`),
  KEY `store_id` (`store_id`),
  CONSTRAINT `fk_displays_store` FOREIGN KEY (`store_id`) REFERENCES `stores` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

COMMIT;