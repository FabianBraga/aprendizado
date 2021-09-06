ct = tot = 0

nm = 0
while nm != 999:
    nm = int(input('Informe o numero: '))
    if nm != 999:
        ct += 1
        tot += nm
print('Foram digitados {} numeros, com um total de {} e uma média de {:.2f}'.format(ct,tot,tot/ct))
