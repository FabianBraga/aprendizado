import math
num = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(num,math.sin(math.radians(num))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(num,math.cos(math.radians(num))))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(num,math.tan(math.radians(num))))