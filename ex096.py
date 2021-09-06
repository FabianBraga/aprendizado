def area(lar, alt):
    print(f'A área do terreno de {lar}x{alt} é de {lar*alt:.2f}m²')

#programa principal

a = float(input('LARGURA (m): '))
b  = float(input('COMPRIMENTO (m): '))
area(a, b)