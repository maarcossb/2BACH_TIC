def diagrama():
    num=input("Dame un numero: ")
    suma=1
    for cont in range(num,-1,-1):
        print(cont,suma)
        suma=suma*cont

diagrama()
