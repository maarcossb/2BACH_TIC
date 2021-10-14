def tabla_multiplicar():

    n=input("Que tabla deseas: ")
    print("=  TABLA DEL "+str(n)+("  ="))
    print("")
    cont=0
    while(cont<=10):
            print (str(n)+(" x ")+str(cont)+(" = ")+str(cont*n))
            cont=cont+1
    
tabla_multiplicar()
