from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import json

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Store dynamic fields as a JSON string (SQLite doesn't have native JSON type in older versions, 
    # but modern SQLite does. We'll use Text for maximum compatibility and parse it manually if needed, 
    # or rely on SQLAlchemy's JSON type if available).
    # Using db.JSON is generally safe with modern SQLAlchemy + SQLite.
    data = db.Column(db.JSON, nullable=False, default={})
    
    # We might want some standard fields if they are guaranteed, but the requirements say "generic".
    # However, an ID is usually good.
    
    def __repr__(self):
        return f'<Product {self.id}>'

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    value = db.Column(db.String(200))
    
    def __repr__(self):
        return f'<Settings {self.key}={self.value}>'
    
    @staticmethod
    def get_value(key, default=None):
        """Get a setting value by key."""
        setting = Settings.query.filter_by(key=key).first()
        return setting.value if setting else default
    
    @staticmethod
    def set_value(key, value):
        """Set a setting value by key."""
        setting = Settings.query.filter_by(key=key).first()
        if setting:
            setting.value = str(value)
        else:
            setting = Settings(key=key, value=str(value))
            db.session.add(setting)
        return setting

class ColumnConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    column_name = db.Column(db.String(100), unique=True, nullable=False)
    visible = db.Column(db.Boolean, default=True, nullable=False)
    sort_order = db.Column(db.Integer, nullable=True)  # 1 for primary, 2 for secondary, null for no sort
    sort_direction = db.Column(db.String(4), nullable=True)  # 'asc' or 'desc'
    display_order = db.Column(db.Integer, default=0)  # For column ordering in display
    
    def __repr__(self):
        return f'<ColumnConfig {self.column_name}>'
