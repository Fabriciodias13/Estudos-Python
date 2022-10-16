sair='n'

while sair!='s':
    
    print('Escolha a operacao desejada abaixo:')
    print('+', '-', 'x', '/' 'ou digite s para sair')
    operacao=input('Digite sua escolha: ')

    n1=float(input('Digite o primeiro numero: '))
    n2=float(input('Digite o segundo numero: '))

    if operacao=='+':
        print('A soma de {} e {} e {}'.format(n1,n2,n1+n2))
    elif operacao=='-':
        print('A subtracao entre {} e {} e {}'.format(n1,n2,n1-n2))
    elif operacao=='x':
        print('A multiplicacao entre {} e {} e {}'.format(n1,n2,n1*n2))
    elif operacao=='/':
        print('A divisão entre {} e {} e {}'.format(n1,n2,n1/n2))
    elif operacao=='s':
        sair='s'
    else:
        print('ERRO! Opcao invalida!')