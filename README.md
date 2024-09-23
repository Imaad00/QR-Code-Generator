# QR-Code-Generator

Here’s a version of the HTML presentation for your `README.md` in plain Markdown syntax. GitHub renders Markdown, so the formatting will be simpler and more readable directly on your repository page.

```markdown
# QR Code Generator

This is a Python-based QR code generator that allows you to create customizable QR codes using the `qrcode` library.

## Features

- Generate QR codes from input data (text or URLs).
- Customize the version (size), error correction level, box size, and border width of the QR code.
- Save the generated QR code as an image file (PNG).
- Open and display the generated QR code image.

## Installation

To install the required dependencies, use the following command:

```bash
pip install qrcode[pil]
```

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/qr-code-generator.git
    cd qr-code-generator
    ```

2. Run the script to generate a QR code:

    ```bash
    python qr-code.py
    ```

3. The generated QR code will be saved as an image (`.png`) and displayed using the default image viewer.

## Example Code

Here is an example of how you can configure the QR code settings in the script:

```python
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
```

- **Version**: Controls the size of the QR code (1 is the smallest).
- **Error Correction**: Determines how much error correction to include (L, M, Q, H).
- **Box Size**: Controls how many pixels each "box" of the QR code is.
- **Border**: Controls how many boxes thick the border should be.

## License

This project is licensed under the MIT License.
