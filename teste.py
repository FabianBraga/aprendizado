a = int(input('diga o 1º termo da PA: '))
r = int(input('diga a razão de progressão da PA: '))

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

for c in range(1,11):
      print('{0:>2}º termo = {2}{1:>2}{3}'.format(c, a, cor['amarelo'], cor['limp']))
      a = a + r