from pyzbar.pyzbar import decode
from PIL import Image

img=Image.open('C:/Users/Iyanu.O/Documents/Python Work/Python-projects/myqrcode2.png')

result=decode(img)

print(result)