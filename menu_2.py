def pinta_menu():
    print("=====================")
    print("=====-:|MENU|:-======")
    print("=====================")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICACION")
    print("4. DIVISION")

def manda_error():
    print("ELECCION ERRONEA. NO PUEDO DIVIDIR POR 0")

def suma(num1,num2):
    respuesta=num1+num2
    return(respuesta)

def resta(num1,num2):
    respuesta=num1-num2
    return(respuesta)

def multiplicacion(num1,num2):
    respuesta=num1*num2
    return(respuesta)

def division(num1,num2):
    respuesta=num1/num2
    return(respuesta)
    
def menu_2():
    #Pedimos dos numeros
    error=1
    while(error==1):
        num1=input("Introduce un numero: ")
        num2=input("Introduce otro numero: ")
        pinta_menu()
        opcion=0
        while(opcion<=0 or opcion>4):
            opcion=input("ELIGE: ")
            if (num2==0 and opcion==4):
                error=1
                manda_error()
            else:
                error=0
                print("Has elegido la opcion: "+str(opcion))  
    
    #OPCION SUMA
    if(opcion==1):
        print(suma(num1,num2))
    else:
        #OPCION RESTA
        if(opcion==2):
            print(resta(num1,num2))
        else:
            #OPCION MULTIPLICACION
            if(opcion==3):
                print(multiplicacion(num1,num2))
            #OPCION DIVISION
            else:
                #FLOAT ES UNA CONVERSION FORZADA PARA CONVERTIRLO EN UN DECIMAL
                print (division(float (num1),num2))




menu_2()
