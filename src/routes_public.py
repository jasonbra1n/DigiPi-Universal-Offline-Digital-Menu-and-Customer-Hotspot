from flask import Blueprint, render_template, jsonify
from database import Product, ColumnConfig, Settings

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def index():
    return render_template('public/menu.html')

@public_bp.route('/hotspot')
def hotspot():
    return render_template('public/splash.html')

@public_bp.route('/api/settings')
def api_settings():
    """Return kiosk/display settings."""
    return jsonify({
        'kiosk_enabled': Settings.get_value('kiosk_enabled', 'false') == 'true',
        'items_per_page': int(Settings.get_value('items_per_page', '10')),
        'page_duration': int(Settings.get_value('page_duration', '10'))
    })

@public_bp.route('/api/products')
def api_products():
    # Get all products
    products = Product.query.all()
    
    # Get column configurations ordered by display_order
    column_configs = ColumnConfig.query.order_by(ColumnConfig.display_order).all()
    config_map = {col.column_name: col for col in column_configs}
    
    # Get visible columns only, in display order
    visible_columns = [col.column_name for col in column_configs if col.visible]
    
    # Filter product data to only include visible columns, maintaining order
    filtered_products = []
    for product in products:
        # Create list of values in the correct order
        row_data = []
        for col_name in visible_columns:
            row_data.append(product.data.get(col_name, ''))
        filtered_products.append(row_data)
    
    # Apply sorting if configured
    sort_configs = sorted(
        [col for col in column_configs if col.sort_order is not None],
        key=lambda x: x.sort_order
    )
    
    if sort_configs:
        def sort_key(row_data):
            keys = []
            for sort_col in sort_configs:
                # Find the index of the sort column
                try:
                    col_index = visible_columns.index(sort_col.column_name)
                    value = row_data[col_index]
                except (ValueError, IndexError):
                    value = ''
                
                # Try to convert to number for proper numeric sorting
                try:
                    value = float(value.replace('$', '').replace(',', '')) if isinstance(value, str) and value else value
                except (ValueError, AttributeError):
                    pass
                
                # Reverse for descending
                if sort_col.sort_direction == 'desc':
                    value = (False, value) if isinstance(value, bool) else -value if isinstance(value, (int, float)) else value
                keys.append(value)
            return tuple(keys)
        
        try:
            filtered_products.sort(key=sort_key, reverse=any(col.sort_direction == 'desc' for col in sort_configs))
        except Exception:
            # If sorting fails, just return unsorted
            pass
    
    # Return both headers and data
    return jsonify({
        'headers': visible_columns,
        'data': filtered_products
    })
