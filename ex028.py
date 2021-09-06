import random
res = int(input('Digite seu palpite entre 0 e 5: '))
maq = random.randint(0, 5)
if res == maq:
    print('Você acertou parabens!')
else:
    print('Você perdeu a resposta seria ',maq)
