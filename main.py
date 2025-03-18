import qrcode


data = "https://wa.me/5592986434478?text=olá, o meu nome é guilherme em que posso ajuda-lo"


qr=qrcode.QRCode(
    version= 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 5,
    border = 2
)

qr.add_data(data)


qr.make(fit= True)

imagem= qr.make_image(fill_color="black", back_color="white")
imagem.save("qrcode.Guilherme.png")