soma = 0
ct = 0
for c in range (3,501,3):
    if c % 2 !=0:
        soma += c
        ct += 1
print('Foram {} numeros somados e o resultrado foi {}'.format(ct,soma))