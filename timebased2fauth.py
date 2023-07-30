import time
import pyotp
import qrcode

key = "ChaveTesteMatrix"

# #Time-Based One Time Password - Aqui iremos verificar á cada 30 segundo o código
totp = pyotp.TOTP(key)
print(totp.now())

input_code = input("Insira seu Código de Verificação: ")
#aqui farei uma verificação se é de fato o mesmo código que há 30 segundos atrás
print(totp.verify(input_code))

