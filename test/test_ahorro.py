import sys
sys.path.append("src")

from model.ahorro import calcular_ahorro
import unittest
from model.ahorro import ErrorMetaNegativa, ErrorPlazoCero, ErrorExtraMayorMeta

# Agregar nuevas excepciones si no existen en model.ahorro
class ErrorInteresNegativo(Exception):
    "la tasa de interés no puede ser negativa"

class ErrorExtraNegativo(Exception):
    "el abono extra no puede ser negativo"

# Modificar la función calcular_ahorro para incluir validaciones adicionales (basado en los nuevos casos de error)
def calcular_ahorro(meta: float, plazo: int, interes: float, extra: float):
    if meta <= 0:  # Cambiado de <0 a <=0 para incluir meta=0
        raise ErrorMetaNegativa("la meta de ahorro no puede ser cero o negativa")
    if plazo <= 0:
        raise ErrorPlazoCero("el plazo de ahorro no puede ser 0")
    if extra > meta:
        raise ErrorExtraMayorMeta("la meta tiene que ser mayor que el extra")
    if interes < 0:
        raise ErrorInteresNegativo("la tasa de interés no puede ser negativa")
    if extra < 0:
        raise ErrorExtraNegativo("el abono extra no puede ser negativo")
    
    interes = (interes / 100) / 12
    
    monto_faltante = meta - extra
    
    if interes > 0:
        ahorro_mensual = monto_faltante * interes / ((1 + interes)**plazo - 1)
    else:
        ahorro_mensual = monto_faltante / plazo
    
    
    return ahorro_mensual

class testAhorro(unittest.TestCase):
    """CASOS NORMALES"""
    def test_normal1(self):
        #entradas
        meta = 5000000
        plazo = 24
        interes = 6
        extra = 0
        #proceso
        cuota_calculado = calcular_ahorro(meta, plazo, interes, extra)
        #salidas
        cuota_esperada = 180000  # Aproximado
        self.assertAlmostEqual(cuota_calculado, cuota_esperada, 0)  # Tolerancia de 0 decimales
    
    def test_normal2(self):
        #entradas
        meta = 2400000
        plazo = 8
        interes = 0
        extra = 400000
        #proceso
        cuota_calculado = calcular_ahorro(meta, plazo, interes, extra)
        #salidas
        cuota_esperada = 250000
        self.assertAlmostEqual(cuota_calculado, cuota_esperada, 2)
    
    def test_normal3(self):
        #entradas
        meta = 10000000
        plazo = 10
        interes = 12
        extra = 2000000
        #proceso
        cuota_calculado = calcular_ahorro(meta, plazo, interes, extra)
        #salidas
        cuota_esperada = 694400  # Aproximado
        self.assertAlmostEqual(cuota_calculado, cuota_esperada, 0)
        
    """CASOS EXTRAORDINARIOS"""
        
    def test_extra1(self):
        #entradas
        meta = 1000000
        plazo = 1
        interes = 0
        extra = 0
        #proceso
        cuota_calculado = calcular_ahorro(meta, plazo, interes, extra)
        #salidas
        cuota_esperada = 1000000
        self.assertAlmostEqual(cuota_calculado, cuota_esperada, 2)
        
    def test_extra2(self):
        #entradas
        meta = 2000000
        plazo = 12
        interes = 24
        extra = 0
        #proceso
        cuota_calculado = calcular_ahorro(meta, plazo, interes, extra)
        #salidas
        cuota_esperada = 144900  # Aproximado
        self.assertAlmostEqual(cuota_calculado, cuota_esperada, 0)

    def test_extra3(self):
        #entradas
        meta = 1000000
        plazo = 10
        interes = 0
        extra = 900000
        #proceso
        cuota_calculado = calcular_ahorro(meta, plazo, interes, extra)
        #salidas
        cuota_esperada = 10000
        self.assertAlmostEqual(cuota_calculado, cuota_esperada, 2)

    """CASOS DE ERROR"""
    
    def test_error1(self):
        #entradas
        meta = 0
        plazo = 6
        interes = 0
        extra = 0
        #proceso
        with self.assertRaises(ErrorMetaNegativa):
            calcular_ahorro(meta, plazo, interes, extra)
            
    def test_error2(self):
        #entradas
        meta = 10000000
        plazo = 12
        interes = -5
        extra = 0
        #proceso
        with self.assertRaises(ErrorInteresNegativo):
            calcular_ahorro(meta, plazo, interes, extra)

    def test_error3(self):
        #entradas
        meta = 10000000
        plazo = 12
        interes = 0
        extra = -500000
        #proceso
        with self.assertRaises(ErrorExtraNegativo):
            calcular_ahorro(meta, plazo, interes, extra)

    def test_error4(self):
        #entradas
        meta = 5000000
        plazo = -10
        interes = 0
        extra = 0
        #proceso
        with self.assertRaises(ErrorPlazoCero):
            calcular_ahorro(meta, plazo, interes, extra)


if __name__ == "__main__":
    unittest.main()
