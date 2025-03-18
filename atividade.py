#atividade
import qrcode


número_de_telefone = input("digite o seu número de telefone aqui, apartir de +55 92 9---- ----:  ")
mensagem = input("digíte a sua mensagem: ")

data = f"https://wa.me/55929{número_de_telefone}?text={mensagem}"


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