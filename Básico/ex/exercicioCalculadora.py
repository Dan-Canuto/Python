while True:
    s = input("Deseja sair? [s/n] : ")
    
    if s == 's' or s == 'S':
        break


    try:
        n1 = input("Digite o primeiro número: ")
        n1Int = int(n1)
        n2 = input("Digite o segundo número: ")
        n2Int = int(n2)
    except:
        print("Números incorretos")
        continue

    op = input("Digite o operador[+,-,/,*]: ")
    if op == '+' or op == '-' or op == '/' or op =='*':
        if(op == '+'):
            resul = n1Int + n2Int
        elif(op == '-'):
            resul = n1Int - n2Int
        elif(op == '/'):
            resul = n1Int / n2Int
        else:
            resul = n1Int * n2Int
    else:
        "Operador não encontrado"
        continue
    print(f"{n1} {op} {n2} = {resul}")
print("Código encerrado")