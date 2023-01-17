# try -> tentar executar o codigo
# except -> ocorreu algum erro ao tentar executar

numero = input('V ou dobrar o numero que vc digitar:')

try:
    numeroFloat = float(numero)
    print('FLOAT:', numeroFloat)
    print(f'O dobro do {numero} é {numeroFloat * 2:.2f}')    
except:
    print(f'Isso não é um numero')
# if numero.isdigit():
#     numeroFloat = float(numero)
#     print(f'O dobro do {número} é {numeroFloat * 2:.2f}')
# else:
#     print(f'Não é um numero valido')
