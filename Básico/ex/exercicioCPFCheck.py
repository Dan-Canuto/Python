#cpf = input("Digite o numero do cpf a ser testado")
cpf = '746.824.890-70'
numeros = cpf.split('-')
semPontos = numeros[0].split('.')

numIni = ''.join(semPontos)
numDig = numeros[1]
cont = 10
soma = 0

for num in numIni:
    mult = int(num) * cont
    soma += mult
    cont -= 1

conta = (soma * 10) % 11

resultado1 = 0 if conta >  9 else conta

check = list(numIni)

check.append(str(resultado1))

cont = 11
soma = 0

for num in check:
    mult = int(num) * cont
    soma += mult
    cont -= 1

conta = (soma * 10) % 11

resultado = 0 if conta >  9 else conta

check.append(str(resultado))

print(resultado)
print(conta)
print(numDig)
print(numIni)

print(check)