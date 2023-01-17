listaA = ['Danilo','Maria']
listaB = listaA
listaC = listaA.copy()

listaA[0] = 'Qualquer coisa'
print(listaB)
print(listaC)