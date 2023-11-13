import qrcode

qr= qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=7, border=2)

qr.add_data('www.linkedin.com/in/abel-serra-zambrano-59050a260')
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')
img.save('linkedinQR.png')