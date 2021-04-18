#Exercicio 4.11.4 Os 3 últimos itens com método for

#Lista
comidas = ['arroz','feijão','batata','hamburguer','milkshake']

#Exibe o 3 ultimos sabores
print('Os 3 últimos intens da lista são: ')

for comida in comidas[-3:]:
  print(comida.title())
