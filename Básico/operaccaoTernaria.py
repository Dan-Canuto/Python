condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro Valor'
print(variavel)

digito = 4
novoDigito = digito if digito <=9 else 0
print(novoDigito);

novoDigito2 = 0 if digito > 9 else digito
print(novoDigito2)