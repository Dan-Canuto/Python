palavra = input('Digite a palavra secreta: ')
print("\n\n")
palavra = palavra.upper()
letrasUtilizadas = ' '
resposta = "*" * len(palavra)
tentativas = 0
while True:
    print(f"Palavra resposta '{resposta}'")
    tentativas += 1
    print(f"Você já testou essas letras: {letrasUtilizadas}")
    letra = input('Digite uma letra: ')
    letra =letra.upper()
    if not(letra in letrasUtilizadas):
        if letra in palavra:
            letrasUtilizadas += f"{letra} "
            for num in range(0,len(palavra)):
                if letra == palavra[num]:
                    print('Você acertou uma letra \n')
                    resposta = resposta[:num] + letra + resposta[num+1:]
        else:
            print('Essa letra não está na palavra\n')
            letrasUtilizadas += f"{letra} "
    else:
        print("Você já buscou essa palavra\n")                 
    if not('*' in resposta):
        print(f"Parabéns você concluiu o jogo!!!\n {tentativas=}")
        break