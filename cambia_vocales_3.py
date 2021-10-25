def cambia_vocales_3():

    palabra=raw_input("Escribe una palabra: ")
    vocal=raw_input("Que vocal deseas cambiar: ")
    nueva_palabra=""
    cont=0 
    
    while(cont<len(palabra)):
        if(palabra[cont]=='a'):
            print(str(vocal))
            nueva_palabra=nueva_palabra+vocal
        else:
            if(palabra[cont]=='e'):
                print(str(vocal))
                nueva_palabra=nueva_palabra+vocal
            else:
                if(palabra[cont]=='i'):
                    print(str(vocal))
                    nueva_palabra=nueva_palabra+vocal
                else:
                    if(palabra[cont]=='o'):
                        print(str(vocal))
                        nueva_palabra=nueva_palabra+vocal
                    else:
                        if(palabra[cont]=='u'):
                            print(str(vocal))
                            nueva_palabra=nueva_palabra+vocal
                        else:
                            print(palabra[cont])
                            nueva_palabra=nueva_palabra+(palabra[cont])

        cont=cont+1

    print("Palabra transformada: "+nueva_palabra)

cambia_vocales_3()
