while True:
    #Pede o nome de usuário 'Koty':
    name = input('Entre com o seu nome: ')
    if name != 'Koty':
        continue
    #Se Koty for digitado, pde a senha:    
    senha = input('Olá Koty, qual é a senha?')
    if senha == '673439':
        break
    #Senão:    
    else:
        print('Senha incorreta. Tente novamente.')
print('Acesso concedido!')
