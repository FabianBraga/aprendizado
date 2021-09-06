from datetime import date
aa = date.today().year
ma = 0
me = 0
for x in range(1, 8):
    pe = int(input('Candidato nº{} informe o ano do seu nascimento: '.format(x)))
    if aa-pe >= 21:
        ma += 1
    else:
        me += 1
print('Na relação de catastros esxitem {} que são naoires de ano e {} que são menores'.format(ma,me))