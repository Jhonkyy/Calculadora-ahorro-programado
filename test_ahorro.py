#importelo ahi
from ahorro import calcular_ahorro
import unittest


class testAhorro(unittest.TestCase):
    #Cada prueba es un metodo y DEBE iniciar coon la palabra "test"
    
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



if __name__ == "__main__":
    unittest.main()