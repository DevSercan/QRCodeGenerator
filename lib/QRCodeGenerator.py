import qrcode
from qrcode.image.svg import SvgImage
import time

class QRCodeGenerator:
    def __init__(self, version: int = 1, boxSize: int = 64, borderWidth: int = 1, errorCorrection: str = 'L'):
        """
        QR code generation class.
        :param version: Size of the QR code (1-40)
        :param boxSize: Pixel size of each box
        :param borderWidth: Border thickness (space around the QR code)
        :param errorCorrection: Sets the error correction level ('L', 'M', 'Q', 'H')
        """
        self.version = version
        self.boxSize = boxSize
        self.borderWidth = borderWidth
        self.qr = None

        errorCorrectionLevels = {
            'L': qrcode.constants.ERROR_CORRECT_L,
            'M': qrcode.constants.ERROR_CORRECT_M,
            'Q': qrcode.constants.ERROR_CORRECT_Q,
            'H': qrcode.constants.ERROR_CORRECT_H
        }
        self.errorCorrection = errorCorrectionLevels.get(errorCorrection.upper(), qrcode.constants.ERROR_CORRECT_L)
    
    def generate(self, data: str) -> bool:
        """
        Generates the QR code object.
        :param data: The data to be encoded in the QR code.
        """
        try:
            self.qr = qrcode.QRCode(
                version = self.version,
                box_size = self.boxSize,
                border = self.borderWidth,
                error_correction = self.errorCorrection
            )

            self.qr.add_data(data)
            self.qr.make(fit = True)
        except Exception as e:
            print(f"[ERROR] Error generating QR code: {e}")
            return False
    
    def _createFilename(self) -> str:
        """ Creates a filename for the QR code file. """
        return f"{int(time.time())}_QR"
        
    def saveAsPNG(self, filename: str = None) -> bool:
        """
        Saves the QR code in PNG format.
        :param filename: The name of the file to save
        """
        try:
            if self.qr is None:
                self.generate()
            
            qrImage = self.qr.make_image(fill = "black", back_color = "white")

            if filename is None:
                filename = self._createFilename()
            filename = filename + ".png"

            qrImage.save(filename)
            return True
        except Exception as e:
            print(f"[ERROR] Error saving QR code as PNG: {e}")
            return False
    
    def saveAsSVG(self, filename: str = None) -> bool:
        """
        Saves the QR code in SVG format.
        :param filename: The name of the file to save
        """
        try:
            if self.qr is None:
                self.generate()
            
            qrImage = self.qr.make_image(image_factory = SvgImage)

            if filename is None:
                filename = self._createFilename()
            filename = filename + ".svg"

            qrImage.save(filename)
            return True
        except Exception as e:
            print(f"[ERROR] Error saving QR code as SVG: {e}")
            return False