#dame un numero: 5
#11111
#11111
#11111
#11111
#11111

def cuadrado_numerico_1():
    
    fila=""
    num=input("Dame un numero: ")
    
    for fil in range(1,num+1):
        for col in range(1,num+1):
            fila=fila+"1"
         
        print fila
        fila=""
                
    
cuadrado_numerico_1()
    
