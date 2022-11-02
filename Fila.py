# -*- coding: utf-8 -*-


#Cria a fila inicial, uma lista com 5 elementos
fila = list(range(1, 5))
#Cria uma lista vazia que guardará os ítens retirados da fila
atendidos = []

while True:

    print('\nDigite A para acrescentar mais alguém na fila')
    print('Digite R para retirar alguém da fila')
    print('Digite S para sair')
    
    escolha = input('\nDigite a sua escolha: ')

    if escolha == 'A' or escolha =='a':
        ultimo = input('Digite o próximo elemento da fila: ')
        fila.append(ultimo)
        print('\n', fila)
    elif escolha == 'r' or escolha =='R':
        if len(fila) > 0:
            vez_de_atendimento = fila.pop(0)
            atendidos.append(vez_de_atendimento)
            print(f'O elemento {vez_de_atendimento} foi atendido!')
            print(f'A fila agora possui os elementos: {fila}')
            print(f'Já foram atendidos {len(atendidos)} clientes')
            print(f'Os clientes atendidos foram: {atendidos}')
        else:
            print('Fila vazia, adicione elementos à fila primeiro.')
    elif escolha == 'S' or escolha== 's':
        break
    else:
        print('Escolha uma opção válida (A, R ou S')
    