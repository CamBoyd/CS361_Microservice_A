# Configuration
from  flask import *
import os
import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H
import io

app = Flask(__name__)

ERROR_CORRECTION = {
    "L": ERROR_CORRECT_L,
    "M": ERROR_CORRECT_M,
    "Q": ERROR_CORRECT_Q,
    "H": ERROR_CORRECT_H
}

# Routes 

@app.route('/', methods=["POST"])
def generate_qr_code():
    data = request.json

    url = data.get('url')
    box_size = data.get('box_size', 10)
    border = data.get('border', 4)
    version = data.get('version', 1)
    error_correction = data.get('error_correction', 'M')

    # Set defaults
    if version == None:
        version = 1
    if box_size == None:
        box_size = 10
    if border == None:
        border = 4
    if error_correction == None:
        error_correction = "M"

    qr = qrcode.QRCode(
        version=version,
        box_size=box_size,
        border=border,
        error_correction=ERROR_CORRECTION[error_correction],
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create a QR code image
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the QR code image to a buffer
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    
    # Create the response object
    response = make_response(buffer.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=QRCode.png'
    response.mimetype = 'image/png'
    return response

# Listener

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 55000)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port)