#Lista de usuários
usuarios = ['admin', 'mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
         print(f"Olá admin, deseja ver o relatório de status?")
        elif usuario != 'admin':
            print(f"olá {usuario}, bem-vindo ao nosso site!")

else: print("Preencha o campo 'usuários'.")
