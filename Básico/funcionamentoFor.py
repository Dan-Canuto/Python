"""
iteravel -> str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entrege o proximo valor
iter -> me entregue o seu iterador
"""

texto = iter('Danilo')
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

texto1 = 'Danilo' # iterável4
iterador = iter(texto1) # iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break