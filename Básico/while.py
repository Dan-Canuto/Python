"""
Repetições
while(enquanto)
executa uma ação enqaunto um condição for verdadeira
Loop infinito -> quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome:: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break
print('Acabou')

#Parte 2

contador = 0

while contador < 10:
    print(contador)
    contador += 1

print('Acabou')

#Parte 3 - Continue

contador = 0

while contador <= 100:
    contador += 1

    if contador >= 10 and contador <= 27:
        print('Não mostra o ' , contador)
        continue

    print(contador)

#Parte 4 - While + while

qtdColunas = 5
qtdLinhas = 5

linha = 1
while linha <= qtdLinhas:
    coluna = 1
    while coluna <= qtdColunas:
        print(f'{linha=}{coluna=}')
        coluna += 1
    linha += 1

print('Acabou')