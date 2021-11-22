def menu():
    #Pedimos dos numeros
    error=1
    while(error==1):
        num1=input("Introduce un numero: ")
        num2=input("Introduce otro numero: ")
        #Damos la diferentes opciones
        print("=====================")
        print("======= MENU ========")
        print("=====================")
        print("1. SUMAR")
        print("2. RESTAR")
        print("3. MULTIPLICACION")
        print("4. DIVISION")
        #Mecanismo para que no meta otros numeros
        opcion=0
        while(opcion<=0 or opcion>4):
            opcion=input("ELIGE: ")
            if (num2==0 and opcion==4):
                error=1
                print("ELECCION ERRONEA. NO PUEDO DIVIDIR POR 0")
            else:
                error=0
                print("Has elegido la opcion: "+str(opcion))

    #OPCION SUMA
    if(opcion==1):
        print(num1+num2)
    else:
        #OPCION RESTA
        if(opcion==2):
            print(num1-num2)
        else:
            #OPCION MULTIPLICACION
            if(opcion==3):
                print(num1*num2)
            #OPCION DIVISION
            else:
                #FLOAT ES UNA CONVERSION FORZADA PARA CONVERTIRLO EN UN DECIMAL
                print(float(num1)/num2)




menu()
