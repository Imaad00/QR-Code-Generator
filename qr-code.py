# Import the necessary libraries
import qrcode  # Library for generating QR codes
from PIL import Image  # Library for image processing
import qrcode.constants  # Constants for QR code settings

# Create an instance of the QRCode class
# version: controls the size of the QR code (1 is the smallest)
# error_correction: determines how much error correction to include
# box_size: controls how many pixels each "box" of the QR code is
# border: controls how many boxes thick the border should be
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Add data to the QR code; this can be a URL, text, etc.
qr.add_data("https://github.com/Imaad00")

# Optimize the QR code configuration to fit the data
qr.make(fit=True)

# Create an image from the QR Code instance
# fill_color: the color of the QR code modules
# back_color: the background color of the QR code
img = qr.make_image(fill_color="green", back_color="black")

# Save the generated QR code image to a file
img.save("img.png")