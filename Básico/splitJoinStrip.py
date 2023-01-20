frase = '      Olha só que    , coisa interessante    '

listaPalavras = frase.split()
print(listaPalavras)

listaPalavras2 = frase.split(', ')
print(listaPalavras2)

listaPalavras2 = frase.split(',')
print(listaPalavras2)

for i, frase in enumerate(listaPalavras2):
    print(listaPalavras2[i].strip())

for i, frase in enumerate(listaPalavras2):
    print(listaPalavras2[i].rstrip())

for i, frase in enumerate(listaPalavras2):
    print(listaPalavras2[i].lstrip())


#Boa pratica
frase = '      Olha só que    , coisa interessante    '
listaFrases = frase.split(',')
listaFrasesCorrigida = []

for i, frase in enumerate(listaPalavras2):
    listaFrasesCorrigida.append(listaFrases[i].strip())

print("\n\n",listaFrasesCorrigida)

frasesUnidas = ', '.join(listaFrasesCorrigida)
print(frasesUnidas)
