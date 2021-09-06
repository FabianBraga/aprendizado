lista = ('pão',1,'Farinha',4.5,'Arroz',3.2,'café',4.8,'Açucar',2.1,'Ervilhas',6)
for x in range(0,len(lista),2):
    print(f'{lista[x]:.<20}R${lista[x+1]:>7.2f}')