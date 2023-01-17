nome = 'Danilo Canuto'

tamanhoNome = len(nome)
contador = 0
nomeCom = ""
while contador < tamanhoNome:
    nomeCom += f'{nome[contador]}*'
    contador += 1

print(nomeCom)