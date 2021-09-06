lista=[]
for x in range(0,5):
    nm= int(input('Digite um valor: '))
    if x==0 or nm > lista[-1]:
        lista.append(nm)
        print('Adicionado ao final da cadastro...')
    else:
        posic= 0
        while posic < len(lista):
            if nm<= lista[posic]:
                lista.insert(posic,nm)
                print(f'Adicionado na posição {posic}...')
                break
            posic += 1
print('-='*30)
print(f'A nossa cadastro ficou assim: {lista}')
