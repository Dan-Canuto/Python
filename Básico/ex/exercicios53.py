#Ex1
numero = input("Digite um número inteiro")

try:
    numeroInt = int(numero)
    if (numeroInt % 2 == 0):
        print('O numero é Par')
    else:
        print('O numero é impar')
except:
    print('Não foi colocado um inteiro')

#Ex2

hora = input("Que Horas são?")
horaInt = int(hora)

if horaInt > 0 and horaInt <= 11:
    print("Bom dia!!")
elif horaInt > 11 and horaInt <= 17:
    print("Boa tarde!!")
else:
    print("Boa noite!!")

#Ex3
nome = input("Digite seu nome")

if(len(nome) <= 4):
    print("Seu nome é curto")
elif len(nome) < 7:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")