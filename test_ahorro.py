#importelo ahi
from ahorro import calcular_ahorro
import unittest
from ahorro import ErrorMetaNegativa,Errorplazocero,Errorextramayormeta 

class testAhorro(unittest.TestCase):
    #Cada prueba es un metodo y DEBE iniciar coon la palabra "test"
    """CASOS NORMALES"""
    def test_normal1(self):
        #entradas
        meta = 1100000
        plazo = 6
        extra = 0
        #proceso
        
        cuota_calculado = calcular_ahorro(meta,plazo,extra)
        #salidas
        cuota_esperada = 183333.33
        self.assertAlmostEqual(cuota_calculado,cuota_esperada,2)
    
    def test_normal2(self):
        #entradas
        meta = 9000000
        plazo = 12
        extra = 0
        #proceso
        
        cuota_calculado = calcular_ahorro(meta,plazo,extra)
        #salidas
        cuota_esperada = 750000.00
        self.assertAlmostEqual(cuota_calculado,cuota_esperada,2)
    
    def test_normal3(self):
        #entradas
        meta = 170000000
        plazo = 36
        extra = 50000000
        #proceso
        
        cuota_calculado = calcular_ahorro(meta,plazo,extra)
        #salidas
        cuota_esperada = 3333333.33
        self.assertAlmostEqual(cuota_calculado,cuota_esperada,2)
        
        """CASO EXTRAORDINARIOS"""
        
    def test_Extra1(self):
        #entradas
        meta = 0
        plazo = 1
        extra = 0
        #proceso
        
        cuota_calculado = calcular_ahorro(meta,plazo,extra)
        #salidas
        cuota_esperada = 0
        self.assertAlmostEqual(cuota_calculado,cuota_esperada,2)
        
    def test_Extra2(self):
        #entradas
        meta = 90000
        plazo = 1
        extra = 0
        #proceso
        
        cuota_calculado = calcular_ahorro(meta,plazo,extra)
        #salidas
        cuota_esperada = 90000
        self.assertAlmostEqual(cuota_calculado,cuota_esperada,2)

        
    def test_Extra3(self):
        #entradas
        meta = 400000
        plazo = 2
        extra = 400000
        #proceso
        
        cuota_calculado = calcular_ahorro(meta,plazo,extra)
        #salidas
        cuota_esperada = 0
        self.assertAlmostEqual(cuota_calculado,cuota_esperada,2)

    """CASOS DE ERROR"""
    
    def test_Error1(self):
        #entradas
        meta = -1300000
        plazo = 15
        extra = 0
        #proceso
        
        with self.assertRaises(ErrorMetaNegativa):
            calcular_ahorro(meta,plazo,extra)
            
    def test_Error2(self):
        #entradas
        meta = 50000
        plazo = 0
        extra = 2000
        #proceso
        
        with self.assertRaises(Errorplazocero):
            calcular_ahorro(meta,plazo,extra)

    def test_Error3(self):
        #entradas
        meta = 400000
        plazo = 2
        extra = 800000
        #proceso
        
        with self.assertRaises(Errorextramayormeta):
            calcular_ahorro(meta,plazo,extra)



if __name__ == "__main__":
    unittest.main()