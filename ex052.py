nm = int(input('Informe um numero: '))
res = 0
if nm> 1:
    for x in range (1,nm+1):
        if nm % x == 0:
            res += 1
            if x  == 1 or x == nm:
                print('\033[33m{}\033[m'.format(x), end=' - ')
            else:
                print('\033[38m{} \033[m'.format(x), end=' - ')
if res>2 or res == 0:
    print('esse numero não é primo')
else:
    print('esse numero é primo')

