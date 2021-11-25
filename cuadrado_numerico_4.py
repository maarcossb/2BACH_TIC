#dame un numero: 5
#11111
#10001
#10101
#10001
#11111

def cuadrado_numerico_4():
    
    fila=""
    num=input("Dame un numero: ")
    
    for fil in range(1,num+1):
        for col in range(1,num+1):
            if(col%2 == 1 and fil%2 == 1):
                fila=fila+"1"
            else:
                if(col == 1 or fil == 1 or col == num or fil == num):
                    fila=fila+"1"
                else:
                    fila=fila+"0" 
                
        print fila
        fila=""
                
    
cuadrado_numerico_4()
    
