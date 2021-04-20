#Lista de usuários
usuarios = ['admin', 'mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

for usuario in usuarios:
    if usuario == 'admin':
        print(f"Olá admin, deseja ver o relatório de status?")
    else:
        print(f"olá {usuario}, bem-vindo ao nosso site!")
