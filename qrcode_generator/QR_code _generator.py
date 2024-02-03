
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)
qr.add_data('https://www.linkedin.com/in/harsh-jatav-b53997225/')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("linkedin.png")