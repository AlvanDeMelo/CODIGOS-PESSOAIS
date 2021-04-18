#Biblioteca sys:
import sys

while True:
    resposta = input("Digite 'sair' para sair: ")
    if resposta == 'sair':
        sys.exit()
    print(f'Você digitou: {resposta}')
