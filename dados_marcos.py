import random

def suerte():

    print("Introduce el nombre de los jugadores: ")
    jugador1=raw_input("JUGADOR 1: ")
    jugador2=raw_input("JUGADOR 2: ")

    print""
    
    print(jugador1)
    
    print("Lanzo dadito: ")
    num1a=random.randint(1,6)
    print(num1a)
    
    
    print("Lanzo dadito: ")
    num1b=random.randint(1,6)
    print(num1b)
    
    print("Lanzo dadito: ")
    num1c=random.randint(1,6)
    print(num1c)
    
    print""

    print(jugador2)
    
    print("Lanzo dadito: ")
    num2a=random.randint(1,6)
    print(num2a)
    
    print("Lanzo dadito: ")
    num2b=random.randint(1,6)
    print(num2b)
    
    print("Lanzo dadito: ")
    num2c=random.randint(1,6)
    print(num2c)

    print""

    num1=num1a+num1b+num1c
    num2=num2a+num2b+num2c
    
    if(num1>num2):
        print("The winner is: "+str(jugador1)+" ("+str(num1)+")")
    else:
        print("The winner is: "+str(jugador2)+" ("+str(num2)+")")

        #if(num1==num2):
            #print("The winner is: JUGADOR 1"+"("+str(num1)+")"+" & "+"JUGADOR 2 "+"("+str(num2)+")")


    
suerte()
#un programa de dados. 3 tiradas. Gana el que sume mas
