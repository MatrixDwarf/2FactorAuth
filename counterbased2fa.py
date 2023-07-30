import pyotp

key = "ChaveTesteMatrix"

# Á partir daqui, irei demonstrar um verificador com limites de input
#Lembrando: não é mais basado em tempo, mas sim em quantidades limitadas de códigos / tentativas

contador = 0

#Counter-Based One Time Password
hotp = pyotp.HOTP(key)

print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(2))
print(hotp.at(3))
print(hotp.at(4))

for _ in range(5):
    print(hotp.verify(input("Código de Verificaçao: "), contador))
    contador += 1
