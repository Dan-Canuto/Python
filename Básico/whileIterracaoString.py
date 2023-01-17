frase = 'Danilo é uma palavra Danilo'

i = 0
qtd = 0
letraMaisRepetida = ''
while i < len(frase):
    letraAtual = frase[i]
    quantasVezesApareceu = frase.count(letraAtual)
    
    if qtd < quantasVezesApareceu:
        qtd = quantasVezesApareceu
        letraMaisRepetida = letraAtual

    print(letraAtual)
    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letraMaisRepetida}" '
    f'{qtd} vezes.'
    )