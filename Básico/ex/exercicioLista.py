compras = []
while True :
    opcao = input('Selecione uma opção \n [i]nserir [a]pagar [l]istar [s]air:')
    if opcao == 'i':
        insere = input('\nInsira o Item')
        if insere in compras:
            print('Item já se encontra na lista\n')
        else:
            compras.insert(len(compras),insere)
            print('Item inserido com sucesso \n')
    elif opcao == 'a':
        apaga = input('Qual valor deseja apagar?')
        for indice ,item in enumerate(compras):
            cont = False
            if item == apaga:
                compras.pop(indice)
                print("Item apagado com sucesso")
                cont = True
            
            if cont == False:
                print("Nenhum item foi apagado")                 
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
