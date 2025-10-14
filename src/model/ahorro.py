class ErrorMetaNegativa(Exception):
    "la meta de ahorro no puede ser negativa"
class ErrorPlazoCero(Exception):
    "el plazo de ahorro no puede ser 0"
class ErrorExtraMayorMeta(Exception):
    "la meta tiene que ser mayor que el extra"


def calcular_ahorro(meta:float, plazo:int, interes:float, extra:float):
    if meta<0:
        raise ErrorMetaNegativa("la meta de ahorro no puede ser negativa")

    if plazo <=0:
        raise ErrorPlazoCero("el plazo de ahorro no puede ser 0")
    
    if extra > meta:
        raise ErrorExtraMayorMeta("la meta tiene que ser mayor que el extra")
    
    interes = (interes/100) / 12
    
    monto_faltante = meta - extra
    
    if interes > 0:
        ahorro_mensual = monto_faltante * interes / ((1 + interes)**plazo - 1)
    else:
        ahorro_mensual = monto_faltante / plazo
    
    
    return ahorro_mensual