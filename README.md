[![qrcode](https://img.shields.io/pypi/v/qrcode?label=qrcode)](https://pypi.org/project/qrcode/)

# QRCodeGenerator

This project was developed to create QR codes using the **qrcode** library.

---

### Requirements
- Python 3.x
- `qrcode` library (pip install qrcode)

### Error Correction Level
QR codes use error correction to ensure that the data can still be read even if part of the code is damaged. Different error correction levels are available, and each offers a different balance between data capacity and the ability to recover from damage. The higher the error correction level, the more resilient the QR code is to damage, but this also increases the size of the QR code.

Here are the available **Error Correction Levels** and their details:

#### 1. **L - Low**

- **Error Correction:** Can correct up to 7% of data errors.
- **Description:** With the lowest error correction level, the QR code is compact and has the smallest size. This makes it faster to scan, but the QR code becomes unreadable if a significant portion of it is damaged. It is suitable for environments where the QR code is not exposed to much wear and tear.

#### 2. **M - Medium**

- **Error Correction:** Can correct up to 15% of data errors.
- **Description:** This is a good balance for most use cases. It provides better error recovery than the "L" level, without significantly increasing the size of the QR code. It is ideal for situations where moderate wear and tear are expected, but space constraints are still a concern.

#### 3. **Q - Quartile**

- **Error Correction:** Can correct up to 25% of data errors.
- **Description:** This level offers a higher degree of error correction. Even if a significant portion of the QR code is damaged, it will still be readable. The size of the QR code increases with the higher error correction, making it suitable for more demanding environments, such as situations where labels or codes might be exposed to physical damage.

#### 4. **H - High**

- **Error Correction:** Can correct up to 30% of data errors.
- **Description:** This level provides the highest resilience, allowing the QR code to be read even if a large portion of it is damaged. However, it also results in the largest QR code. This error correction level is ideal for harsh environments where QR codes might undergo significant wear and tear, or where reliability is crucial despite the space limitations.

---

### How to Use the QRCodeGenerator

To use this library, you can easily generate QR codes with customizable error correction levels, sizes, and more. Simply choose the error correction level that best suits your use case and generate the QR code.

Example:

```python
from lib.QRCodeGenerator import QRCodeGenerator

qrCodeGenerator = QRCodeGenerator(version=1, boxSize=64, borderWidth=1, errorCorrection='H')
qrCodeGenerator.generate("https://example.com")
qrCodeGenerator.saveAsPNG()
```

This example creates a QR code with the highest error correction level (H), which ensures maximum resilience.

---