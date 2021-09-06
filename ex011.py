largura = float(input('Informe a largura da sua parede em metros: '))
altura = float(input('Informe a altura da sua parede em metros: '))

print('com base nas medidas informadas a sua area de pintura é de {:.2f}m² \nVão ser nescessários {:.2f}L de tinta para o serviço'.format(largura * altura, largura * altura / 2))