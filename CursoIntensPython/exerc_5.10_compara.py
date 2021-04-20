#Lista de usuários para comparação:
usuarios = ['admin', 'mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
new_users = ['priscilo', 'mushrooms', 'macarrão', 'green peppers', 'ferdinando', 'larisso']

#Garante que a lista não está vazia:
if new_users:
    #Para o usuário Admin:
    for users in usuarios:
        if users == 'admin':
            print("Olá Admin, deseja ver a lista de Status?")
    #Para outros usuários:
    for users in new_users:
        if users in usuarios:
            print(f"O nome de usuário {users} não está disponível.")
        else: print(f"O nome de usuário {users} está disponível.")

#Se a lista estiver vazia imprime:
else: print("Digite pelo menos um nome de usuário!")
