#Exercício 4.11.3 Adicionando sabor a lista do amigo

#Lista das minhas pizzas
minhas_pizzas = ['napolitana','baiana','peruana','marguerita']

#Adiciona um novo sabor a minha lista
minhas_pizzas.append('frango com catupiry')

#Lista pizzas do amigo
pizzas_amigo = minhas_pizzas[:]

#Adiciona um novo sabor a lista do meu amigo
pizzas_amigo.append('calabresa')

#Exibe minhas pizzas
for pizza in minhas_pizzas:
  #Exibe os sabores com a primeira letra maíuscula
  print(pizza.title())

#Linha em branco
print("\n")

#Exibe pizas do amigo
for pizza in pizzas_amigo:
  #Exibe os sabores com a primeira letra maíuscula
  print(pizza.title())
