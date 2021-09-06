ct = tot = 0
seg = 'S'
nm = 0
mai = 0
men = 0
while seg == 'S':
    nm = int(input('Informe o numero: '))
    ct += 1
    if ct == 1:
        mai = nm
        men = nm
    if nm > mai:
        mai = nm
    if nm < men:
        men = nm
    seg = str(input('Deseja continuar [S/N]: ')).strip().upper()
    tot += nm
    print('')
print('Foram digitados {} números, com um total de {} e uma média de {:.2f}'.format(ct,tot,tot/ct))
print('O maior número digitado foi {} e o menor foi {}'.format(mai,men,))