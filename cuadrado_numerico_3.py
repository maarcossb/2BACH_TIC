#dame un numero: 5
#10101
#01010
#10101
#01010
#10101

def cuadrado_numerico_3():
    
    fila=""
    num=input("Dame un numero: ")
    
    for fil in range(1,num+1):
        for col in range(1,num+1):
            if (col%2 == 0 and fil%2 == 1):
                fila=fila+"0"
            else:
                if(col%2 == 1 and fil%2 == 0):
                    fila=fila+"0"
                else:
                    fila=fila+"1"  
                
        print fila
        fila=""
                
    
cuadrado_numerico_3()
    
