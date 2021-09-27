def gauss_pares():
    n=input("Hasta que numero quieres contar: ")
    acum=0
    resto=0
    for cont in range(1,n+1):
        resto=cont % 2
        if(resto==0):
            acum=acum+cont
        print(str(cont) +" acum= "+str(acum)) 

gauss_pares()

 
