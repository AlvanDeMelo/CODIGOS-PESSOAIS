#Exercício 4.11 Pizzas minhas e do amigo

#Lista das minhas pizzas
minhas_pizzas = ['napolitana','baiana','peruana','marguerita']
#Lista pizzas do amigo
pizzas_amigo = minhas_pizzas[:]

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
