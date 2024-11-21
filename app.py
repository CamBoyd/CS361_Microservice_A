# Configuration
from  flask import *
import os
import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H
import io

DEFAULT_BOX_SIZE = 10
DEFAULT_BORDER = 4
DEFAULT_VERSION = 1
DEFAULT_ERRORCORRECTION = 'M'

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

    # check item is defined in request or defined as none, if so use default value
    url = data.get('url')
    box_size = data.get('box_size') or DEFAULT_BOX_SIZE
    border = data.get('border') or DEFAULT_BORDER
    version = data.get('version', 1) or DEFAULT_VERSION
    error_correction = data.get('error_correction') or DEFAULT_ERRORCORRECTION


    qr = qrcode.QRCode(
        version=version,
        box_size=box_size,
        border=border,
        error_correction=ERROR_CORRECTION[error_correction],
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create a QR code image
    qr_image = qr.make_image(fill="black", back_color="white")

    # Save the QR code image to a buffer
    image_buffer = io.BytesIO()
    qr_image.save(image_buffer, format="PNG")
    image_buffer.seek(0)

    # Create the response object
    filename = "QRCode.png"
    response = make_response(image_buffer.getvalue())
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    response.mimetype = "image/png"
    return response


# Listener

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 55000)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port)