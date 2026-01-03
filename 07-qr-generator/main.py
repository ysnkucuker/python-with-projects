import pyqrcode

url = "https://www.yasinkucuker.com"

qr_code = pyqrcode.create(url)
qr_code.svg('yasinkucuker.svg', scale=6)