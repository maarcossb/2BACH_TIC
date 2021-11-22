def fecha_mes():

    fecha=raw_input("Introduce una fecha (dd/mm/aa): ")
    nombre_meses="EneFebMarAbrMayJunJulAgoSepOctNovDic"
    mes=int(fecha[3])*10+int(fecha[4])
    mes_elegido=nombre_meses[(mes-1)*3:(mes-1)*3+3]
    print(mes_elegido)
    


          

fecha_mes()

    
    

    

    
    

