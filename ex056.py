md = 0
hm = 0
hmv = ''
ml = 0
for x in range(1,5):
    print('-'*10,'{}ª pessoa'.format(x),'-'*10)
    nm = str(input('Informe o seu Nome: ')).strip()
    ida = int(input('Informe a sua ano: '))
    sx = str(input('Informe o sexo [M/F: ')).strip().upper()
    md += ida
    if sx =='M' and hm<ida:
        hm = ida
        hmv = nm
    if sx =='F' and ida<20:
        ml +=1
print('A média das idades do grupo é de {:.2f} anos'.format(md/4))
print('O homem mais velho se chama {} e tem {} anos'.format(hmv, hm))
print('Ao todo são {} nulheres com menso de 20 anos'.format(ml))