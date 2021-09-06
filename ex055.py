mp = 0
ml = 0
cdmp = 0
cdml = 0
for x in range(1, 6):
    pe = float(input('Candidato nº{:.2f} informe o seu peso: '.format(x)))
    if x == 1:
        mp = pe
        ml = pe
    else:
        if pe > mp:
           mp = pe
           cdmp = x
        if pe < ml:
           ml = pe
           cdml = x
print('A pessoa mais pesda é a {}ª com o peso de {:.2f} Kg'.format(cdmp,mp))
print('A pessoa mais leve é a {}ª com o peso de {:.2f} Kg'.format(cdml,ml))