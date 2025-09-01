class ErrorMetaNegativa(Exception):
    "la meta de ahorro no puede ser negativa"
class ErrorPlazoCero(Exception):
    "el plazo de ahorro no puede ser 0"
class ErrorExtraMayorMeta(Exception):
    "la meta tiene que ser mayor que el extra"
def calcular_ahorro(meta:float, plazo:int, extra:int):
    if meta<0:
        raise ErrorMetaNegativa("la meta de ahorro no puede ser negativa")

    if plazo <=0:
        raise ErrorPlazoCero("el plazo de ahorro no puede ser 0")
    if extra > meta:
        raise ErrorExtraMayorMeta("la meta tiene que ser mayor que el extra")
    return (meta-extra)/plazo
    

def prueba_normal1():
    """"
    Entradas:
    valor a ahorrar
    plazo(meses)
    abono extra
    """
    
    meta = 1100000
    plazo = 6
    extra = 0
    
    salida = calcular_ahorro(meta,plazo,extra) 
    
    salida_esperada = 183333.33
    
    if round(salida,2) == round(salida_esperada,2):
        print("Prueba caso normal 1 Exitosa ")
    
    else:
        print("prueba caso normal 1 Fallida")



def prueba_normal2():
    """"
    Entradas:
    valor a ahorrar
    plazo(meses)
    abono extra
    """
    
    meta = 9000000
    plazo = 12
    extra = 0
    
    salida = calcular_ahorro(meta,plazo,extra) 
    
    salida_esperada = 750000.00
    
    if round(salida,2) == round(salida_esperada,2):
        print("Prueba caso normal 1 Exitosa ")
    
    else:
        print("prueba caso normal 1 Fallida")



def prueba_plazo_cero():
    
    meta = 400000
    plazo = 0
    extra = 400000
    
    salida = calcular_ahorro(meta,plazo,extra) 
    
    salida_esperada = 0
    
    if round(salida,2) == round(salida_esperada,2):
        print("Prueba caso plazo cero Exitosa ")
    
    else:
        print("prueba caso plazo cero Fallida")


