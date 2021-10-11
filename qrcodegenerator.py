
import pyqrcode
import png
from pyqrcode import QRCode

s = 'https://www.youtube.com/watch?v=IUjWumGIqe8&ab_channel=BoilerRoom'


url = pyqrcode.create(s)

print(f'Creating png. \n')
url.png('QR_codes/testQR.png', scale = 8)

print(f'Creating svg. \n')
url.svg('QR_codes/testQR.svg', scale = 8)

