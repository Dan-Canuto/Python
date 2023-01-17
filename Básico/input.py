nome = input('Qual o seu nome?')
print(f'O seu nome é {nome}')

numero1 = input('Digite um numero: ')
numero2 = input('Digite outro numero: ')

intNumero1 = int(numero1)
intNumero2 = int(numero2)


print(f'A soma dos numeros é: {numero1 + numero2}') #Está sendo considerado como String

print(f'A soma dos numero é: {intNumero1 + intNumero2}') #Está sendo considerado como numero