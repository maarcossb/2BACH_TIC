def devuelve_el_mayor(x,y,z):
    if(x>y and x>z):
        mayor=x
    else:
        if(y>z):
            mayor=y
        else:
            mayor=z

    return(mayor)


def mayor():
    x=input("Dame un numero: ")
    y=input("Dame otro numero: ")
    z=input("Dame otro numero: ")

    print("El mayor es: "+ str(devuelve_el_mayor(x,y,z)))

mayor()
