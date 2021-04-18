while True:
    #Lê o valor de entrada:
    spam = int(input("Digite um valor: "))
    #Se o valor for 1 imprime "Hello":
    if spam == 1:
        print("Hello!")
    #Se o valor for 2 imprime "Howdy":   
    elif spam == 2:
        print("Howdy!")
    #Se o valor for queler outro imprime "Greentings": 
    elif spam != 1 or 2:
        print("Greetings!")
