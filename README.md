# QR Code Generator

This project is a simple QR code generator written in Python. It uses the `qrcode` library to generate QR codes from user input and save them as image files.

## Requirements

- Python 3.x
- `qrcode` library

You can install the `qrcode` library using pip:

```bash
pip install qrcode[pil]

Usage
Clone the repository or download the main.py file.
Run the script:
Enter the text or URL you want to encode in the QR code when prompted.
Enter the filename to save the QR code image.

Code Explanation
The script performs the following steps:
Imports the qrcode library.
Prompts the user to enter the text or URL to encode in the QR code.
Prompts the user to enter the filename to save the QR code image.
Creates a QRCode object with specific parameters.
Adds the user input data to the QRCode object.
Generates the QR code.
Creates an image from the QR code.
Saves the image to the specified filename.
Prints a confirmation message.
