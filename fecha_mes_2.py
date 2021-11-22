def fecha_mes_2():

    fecha=raw_input("Introduce una fecha (dd/mm/aa): ")
    nombre_meses="Enero,Febrero,Marzo,Abril,Mayo,Junio,Julio,Agosto,Septiembre,Octubre,Noviembre,Diciembre,"
    numero_mes=int(fecha[3])*10+int(fecha[4])

    print(numero_mes)
    
    numero_comas=0
    cont=0
    mes=" "

    while(numero_comas<=numero_mes-1):

        if(nombre_meses[cont]==','):
            numero_comas=numero_comas+1
            
        if(numero_comas==numero_mes-1):
            if(nombre_meses[cont]!=','):
                mes=mes+nombre_meses[cont]
      
        cont=cont+1
        
    #print("cont: "+str(cont))
    #print("comas: "+str(numero_comas))
    print("Estoy en el mes de"+mes)
 


        
fecha_mes_2()

    
    

    

    
    

