import unittest
import ahorro

class pruebas_ahorro(unittest.TestCase):
    
    def preuba_normal1(self):
        #entradas
        meta = 1100000
        plazo = 6
        extra = 0
        #proceso
        calcular_cuota=ahorro.calcular_ahorro(meta,plazo,extra)
        #verificado
        cuota_esperada=183333.33
        
        self.assertAlmostEqual(calcular_cuota,cuota_esperada,2)
        
        
    def preuba_normal2(self):
        #entradas
        meta = 9000000
        plazo = 12
        extra = 0
        #proceso
        calcular_cuota=ahorro.calcular_ahorro(meta,plazo,extra)
        #verificado
        cuota_esperada=750000.00
        
        self.assertAlmostEqual(calcular_cuota,cuota_esperada,2)

    
