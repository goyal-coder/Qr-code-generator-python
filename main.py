import qrcode

data = input("Enter the text or url: ").strip()
filename = input("Enter the filename: ")

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=5,
)

# Add data to the QRCode object
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QRCode object
image = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
image.save(filename)
print(f"QR code saved as {filename}")