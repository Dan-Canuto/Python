import decimal

numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2
numero4 = decimal.Decimal(str(numero1)) + decimal.Decimal(str(numero2))

print(numero3)
print(numero4)
print(f'{numero3:.2f}')
print(round(numero3, 2))