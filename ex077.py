lista = ('pessoa','Acertivo','alevado','inconstitucional','estudos','trabalho')
for x in lista:
    print(f'Na palavra {x.upper()} temos: ',end='')
    for y in x:
        if y.lower() in 'aeiou':
            print(f'\033[:34m{y} \033[m',end='')
    print('')


