def cuenta_letras():

    palabra=raw_input("Escribe una palabra: ")
    vocal=0
    consonante=0
    cont=0
        
    while(cont<len(palabra)):
        if(palabra[cont]=='a'):
            vocal=vocal+1
        else:
            if(palabra[cont]=='e'):
                vocal=vocal+1
            else:
                if(palabra[cont]=='i'):
                    vocal=vocal+1
                else:
                    if(palabra[cont]=='o'):
                        vocal=vocal+1
                    else:
                        if(palabra[cont]=='u'):
                            vocal=vocal+1
                        else:
                            consonante=consonante+1
                                                     
        cont=cont+1

    print("Vocales: "+str(vocal))
    print("Consonantes: "+str(consonante))
    print("Numero total: "+str(vocal+consonante))
 

    
cuenta_letras()
