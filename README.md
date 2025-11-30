# QR Code Generator using Python

This is a simple QR Code generator application created using Python. It allows you to generate QR codes for text or URLs and save them as image files. The interface is built using Tkinter for easy usability.

## Prerequisites
Before running this application, make sure you have the following installed:

- Python (version 3.7 or later)
- `qrcode` library
- `tkinter` library (usually included with Python)

To install the required library, run:


## How to Run
1. Download or clone the project files.
2. Open a terminal/command prompt and navigate to the folder containing the script.
3. Run the program using:


4. The application window will open.

## Application Features

### 🔹 Enter Text or URL
- Type any text or URL in the “Enter the text/URL” field.
- This text will be encoded inside the QR code.

### 🔹 Choose Save Location
- Enter the folder path where you want to save the generated QR code.

### 🔹 Choose QR Code File Name
- Enter the desired name for the QR code image file.

### 🔹 Automatic QR Code Size
- The application **no longer includes a size field**.
- QR code size adjusts automatically using the internal `fit=True` algorithm.

### 🔹 Generate QR Code
- Click the **Generate Code** button.
- The QR code image is generated and saved as a `.png` file.
- A pop-up message confirms successful saving.

## Notes
- Ensure the save directory exists; otherwise, saving will fail.
- The QR code is generated using PIL and saved as a PNG image.
- You can customize the appearance, colors, and style in the code.

Happy coding!
