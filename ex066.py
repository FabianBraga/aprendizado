ct = tot = 0
while True:
    nm = int(input('Informe o numero (999 para encerrar): '))
    if nm == 999:
        break
    ct += 1
    tot += nm
print(f'Foram digitados {ct} numeros, com um total de {tot} e uma média de {tot/ct:.2f}')
