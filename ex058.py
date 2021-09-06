from random import randint
nm = randint(1,10)
jg = ten = 0
print('-'*21,'Joguinho do papai','-'*21)
print('PENSEI EM UM NUMERO ENTRE 1 E 10 QUERO VER VOCÊ ADIVINHAR...')
print('-'*61)
while nm!= jg:
    jg = int(input('Dê seu palpite: '))
    ten+=1
if ten>5:
    print('Você precisou de {} tentativas. Pensei que você fosse melhor dados, mas ainda acertou apesar da demora...'.format(ten))
elif ten>2:
    print('Você precisou de {} tentativas. Acertou apesar da demora...'.format(ten))
elif ten>1:
    print('Você precisou de {} tentativas. Foi quase perfeito...'.format(ten))
else:
    print('Você acertou na {}ª tentativa. Você é bom nisso em...'.format(ten))
