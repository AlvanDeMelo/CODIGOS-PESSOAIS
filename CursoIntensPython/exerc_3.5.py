#Exercíco 3.5 - Lista de Convidados.

#Nomes da lista
convidado = ['manoel','maria','soneca','juliana','morpheu','um']

#Convidado removido
removido = convidado.pop(2)

#Saudação
saudacao = "Olá " +convidado[2].title()+ "! Você foi convidado para o meu jantar."

#Imprime saudacao
print(saudacao)

#Imprime o removido
print("Infelizmente o convidado " +removido.title()+ " naõ poderá comparecer ao nosso jantar.")
