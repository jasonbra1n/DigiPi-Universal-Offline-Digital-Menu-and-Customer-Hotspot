import qrcode
import os
from io import BytesIO

def generate_qr_code(url, save_path=None):
    """
    Generate a QR code for the given URL.
    
    Args:
        url: The URL to encode in the QR code
        save_path: Optional path to save the QR code image
        
    Returns:
        BytesIO object containing the QR code image
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    if save_path:
        img.save(save_path)
    
    # Also return as BytesIO for potential in-memory use
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    
    return buffer

def get_qr_code_path(static_folder):
    """Get the path where QR code should be saved."""
    return os.path.join(static_folder, 'uploads', 'menu_qr.png')
