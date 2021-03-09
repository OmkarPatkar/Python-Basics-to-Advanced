#import libraries.
import pyqrcode
from pyqrcode import QRCode

#link to make qrcode
link = 'https://github.com/OmkarPatkar'

#generate the qrcode
qr = pyqrcode.create(link)

#create and save the qrcode
qr.svg('github_link.svg', scale = 8)