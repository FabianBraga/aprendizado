n= int(input('Quantos termos de fibo você quer: '))
print('-'*124)
print(0,end='')
for x in range (1,n):
    rs = int((((1+(5**(1/2)))/2)**x - ((1-(5**(1/2)))/2)**x)/5**(1/2))
    print(' - ',rs,end='')
print('')
print('-'*124)
