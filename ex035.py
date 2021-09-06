n1 = int(input('Informe o 1º reta: '))
n2 = int(input('Informe o 2º reta: '))
n3 = int(input('Informe o 3º reta: '))
if (n2-n3)<n1<(n2+n3):
    print('é possível formar um triângulo pois os numeros atendem as regras ')
else:
    if (n1-n3)<n2<(n1+n3):
        print('é possível formar um triângulo pois os numeros atendem as regras ')
    else:
        if (n1-n2)<n3<(n1+n2):
            print('é possível formar um triângulo pois os numeros atendem as regras ')

