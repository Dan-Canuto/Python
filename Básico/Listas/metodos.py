# metodos úteis -> append, insert, pop, del, clear, extend, +
lista = [10,20,30,40]
lista2 = [1,2,3]

lista3 = lista + lista2
print(lista3)

lista[2] = 300
print(lista)

del lista[2]
print(lista)

lista.append(50)
lista.append(60)
lista.append(70)
print(lista)

ultimoRemovido = lista.pop()
print(lista, 'Removido', ultimoRemovido)

ultimoValor = lista.pop(2)
print(lista, 'Removido', ultimoValor)

lista.insert(0,'inserido por insert')
print(lista)

lista.extend(lista2)
print(lista)

lista.clear()
print(lista)