import time
import pyotp
import qrcode

key = "ChaveTesteMatrix"

# #neste Snippet, vou gerar um código QR para autenticar no próprio GoogleAuthenticator
uri = pyotp.totp.TOTP(key).provisioning_uri(name='CaioGalvao123', issuer_name="App Qualquer")

print(uri)
qrcode.make(uri).save("2fa.png") #Aqui será gerado o seu QR Code









# BETA: Tentando fazer isso através do código gerado pelo Google
# totp = pyotp.TOTP(key)
# print(totp.now())
# while True:
#     print(totp.verify(input("Insira o Código: ")))