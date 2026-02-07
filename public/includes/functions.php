<?php
require_once __DIR__ . '/../config.php';

/**
 * Fetch a specific setting value from the database.
 */
function get_setting($key, $store_id = 1) {
    global $pdo;
    try {
        $stmt = $pdo->prepare("SELECT setting_value FROM settings WHERE setting_key = ? AND store_id = ?");
        $stmt->execute([$key, $store_id]);
        return $stmt->fetchColumn();
    } catch (PDOException $e) {
        return null;
    }
}

/**
 * Get the total count of products in the database.
 */
function get_product_count($store_id = 1) {
    global $pdo;
    try {
        $stmt = $pdo->prepare("SELECT COUNT(*) FROM products WHERE store_id = ?");
        $stmt->execute([$store_id]);
        return $stmt->fetchColumn();
    } catch (PDOException $e) {
        return 0;
    }
}

/**
 * Sanitize output for HTML display.
 */
function h($string) {
    return htmlspecialchars($string, ENT_QUOTES, 'UTF-8');
}

/**
 * Format price strings (removes currency symbols for sorting/math if needed).
 */
function format_price($price) {
    // Basic implementation - can be expanded for currency conversion
    return $price;
}

// Future: API Integration functions will go here
// function sync_with_pos_api() { ... }
?>