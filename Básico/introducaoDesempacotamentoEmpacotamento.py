nome = ['Danilo', 'Canuto', 'Pereira']

nome1, nome2, nome3 = ['Danilo', 'Canuto', 'Pereira']
print(nome2)

nome1, *resto = ['Danilo', 'Canuto', 'Pereira']
print(resto)

*_, nome4 = ['Danilo', 'Canuto', 'Pereira']
print(nome4)