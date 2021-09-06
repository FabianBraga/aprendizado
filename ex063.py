nm = int(input('Informe um numero para a sequencia de Fibonacci: '))
nf = int(input('Informe um numero de elementos dessa sequencia: '))
x = fba = 0
fb = nm
while x <= nf-1:
    print(fb)
    x += 1
    fb = fb+fba
    fba = nm
    nm = fb
