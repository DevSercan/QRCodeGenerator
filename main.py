from lib.QRCodeGenerator import QRCodeGenerator

def main():
    qrCodeGenerator = QRCodeGenerator()
    data = "https://github.com/DevSercan"
    qrCodeGenerator.generate(data)
    qrCodeGenerator.saveAsPNG()
    qrCodeGenerator.saveAsSVG()

if __name__ == "__main__":
    main()