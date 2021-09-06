fr = str(input('Informe seu nome completo: ')).strip()

print(fr.upper())
print(fr.lower())
print('Total geral de digitos: ',len(fr))
print('Seu nome tem ao todo {} letras'.format(len(fr.replace(' ',''))))
print('O primeiro nome tem: ',fr.find(' '))
