import qrcode

data='Dont forget to subscribe!'

img=qrcode.make(data)
img.save('C:/Users/Iyanu.O/Documents/Python Work/Python-projects/myqrcode.png')