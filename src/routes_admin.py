from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
import os
from database import db, Product, ColumnConfig, Settings
from qr_generator import generate_qr_code, get_qr_code_path

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@admin_bp.route('/')
def index():
    product_count = Product.query.count()
    column_count = ColumnConfig.query.count()
    return render_template('admin/index.html', product_count=product_count, column_count=column_count)

@admin_bp.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('admin.index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('admin.index'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        # Get upload folder from app config
        upload_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        
        try:
            # Parse CSV using pandas
            df = pd.read_csv(filepath)
            
            # Clear existing products
            Product.query.delete()
            
            # Auto-create ColumnConfig entries for new columns
            existing_columns = {col.column_name for col in ColumnConfig.query.all()}
            new_columns = set(df.columns) - existing_columns
            
            for idx, col_name in enumerate(df.columns):
                if col_name in new_columns:
                    col_config = ColumnConfig(
                        column_name=col_name,
                        visible=True,
                        display_order=idx
                    )
                    db.session.add(col_config)
            
            # Insert new products
            for _, row in df.iterrows():
                product = Product(data=row.to_dict())
                db.session.add(product)
            
            db.session.commit()
            
            flash(f'Successfully uploaded {len(df)} products with {len(df.columns)} columns!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error processing CSV: {str(e)}', 'error')
        
        return redirect(url_for('admin.index'))
    else:
        flash('Invalid file type. Please upload a CSV file.', 'error')
        return redirect(url_for('admin.index'))

@admin_bp.route('/columns')
def columns():
    columns = ColumnConfig.query.order_by(ColumnConfig.display_order).all()
    return render_template('admin/columns.html', columns=columns)

@admin_bp.route('/columns/update', methods=['POST'])
def update_columns():
    try:
        data = request.get_json()
        
        for col_data in data:
            col_config = ColumnConfig.query.filter_by(column_name=col_data['column_name']).first()
            if col_config:
                col_config.visible = col_data.get('visible', True)
                col_config.sort_order = col_data.get('sort_order')
                col_config.sort_direction = col_data.get('sort_direction')
                col_config.display_order = col_data.get('display_order', 0)
        
        db.session.commit()
        return jsonify({'success': True, 'message': 'Column settings updated!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 400

@admin_bp.route('/display')
def display():
    kiosk_enabled = Settings.get_value('kiosk_enabled', 'false') == 'true'
    items_per_page = int(Settings.get_value('items_per_page', '10'))
    page_duration = int(Settings.get_value('page_duration', '10'))
    
    # Check if QR code exists
    static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    qr_path = get_qr_code_path(static_folder)
    qr_exists = os.path.exists(qr_path)
    
    return render_template('admin/display.html', 
                         kiosk_enabled=kiosk_enabled,
                         items_per_page=items_per_page,
                         page_duration=page_duration,
                         qr_exists=qr_exists)

@admin_bp.route('/display/update', methods=['POST'])
def update_display():
    try:
        data = request.get_json()
        
        Settings.set_value('kiosk_enabled', 'true' if data.get('kiosk_enabled') else 'false')
        Settings.set_value('items_per_page', str(data.get('items_per_page', 10)))
        Settings.set_value('page_duration', str(data.get('page_duration', 10)))
        
        db.session.commit()
        return jsonify({'success': True, 'message': 'Display settings updated!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 400

@admin_bp.route('/display/generate-qr', methods=['POST'])
def generate_qr():
    try:
        # Get the menu URL from request or use default
        menu_url = request.json.get('url', 'http://digipi.local/')
        
        static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
        qr_path = get_qr_code_path(static_folder)
        
        # Generate QR code
        generate_qr_code(menu_url, qr_path)
        
        return jsonify({'success': True, 'message': 'QR code generated!', 'path': '/static/uploads/menu_qr.png'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400
