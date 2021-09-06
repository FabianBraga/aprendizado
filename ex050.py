sm = 0
for x in range(1,7):
    nm = int(input('informe o numero \033[;31m{}º\033[m numero: '.format(x)))
    if nm % 2 == 0:
        sm += nm
print('O resultado da soma dos números pares é ',sm)