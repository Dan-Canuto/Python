compras = []
while True :
    opcao = input('Selecione uma opção \n [i]nserir [a]pagar [l]istar [s]air:')
    if opcao == 'i':
        insere = input('\nInsira o Item: ')
        if insere in compras:
            print('Item já se encontra na lista\n')
        else:
            compras.append(insere)
            print('Item inserido com sucesso \n')
    elif opcao == 'a':
        apaga = input('Qual indice deseja apagar?: ')
        teste = compras.pop(int(apaga))
        if teste:
            print("Apagado com sucesso")
        else:
            print("Item não encontrado")                 
    elif opcao == 'l':
        if compras:
            for item in enumerate(compras):
                print(item)
        else:
            print("Lista vazia")
    elif opcao == 's':
        break
    else :
        print("Comando não reconhecido")
