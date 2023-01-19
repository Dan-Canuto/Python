lista = ['Danilo', 'Canuto', 'Pereira']

lista.append('João')

listaEnumerada = enumerate(lista)

for item in listaEnumerada:
    print(item)

print('O que tem na lista enumerada' , listaEnumerada)

for item in enumerate(lista):
    print(item)

#Recomendado utilizar
for indice, nome in enumerate(lista):
    print(indice, nome)