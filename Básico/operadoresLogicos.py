#and (e) or (ou) not (não)

#AND
entrada = input('[E]ntrar [S]air: ')
senhaDigitada = input('Senha: ')

senhaPermitida = '123456'



if entrada == 'E' and senhaDigitada == senhaPermitida:
    print('Entrar And')
else:
    print('Sair')

#OR
entrada = input('[E]ntrar [S]air: ')
senhaDigitada = input('Senha: ')

senhaPermitida = '123456'



if (entrada == 'E' or entrada == 'e') and senhaDigitada == senhaPermitida:
    print('Entrar OR')
else:
    print('Sair')

#NOT

senha = input('Senha: ')

if not senha:
    print('Você não digitou nenhuma senha')


