import sys
sys.path.append(".")
sys.path.append("src")

import unittest
from controller.controlador_usuarios import UsuariosController
from controller.controlador_ahorros import CalculosController
from model.usuario import Usuario
from model.calculo_ahorro import CalculoAhorro
from datetime import datetime

class TestBaseDatos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Se ejecuta una sola vez al iniciar las pruebas"""
        # Crear tablas antes de comenzar
        try:
            UsuariosController.crear_tabla()
        except Exception as e:
            print("Tabla usuarios ya existe o error al crear:", e)

        try:
            CalculosController.crear_tabla()
        except Exception as e:
            print("Tabla calculos ya existe o error al crear:", e)

        # Insertar usuario de prueba
        cls.usuario = Usuario(nombre="Usuario Prueba")
        UsuariosController.insertar(cls.usuario)

    def test_insertar_calculo1(self):
        calc = CalculoAhorro(id_usuario=1, meta=5000000, plazo_meses=24, interes_anual=6,
                            abono_extra=0, resultado_mensual=180000)
        id_insertado = CalculosController.insertar(calc)
        resultado = CalculosController.buscar_por_id(id_insertado)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.meta, 5000000)

    def test_insertar_calculo2(self):
        calc = CalculoAhorro(id_usuario=1, meta=2400000, plazo_meses=8, interes_anual=0,
                            abono_extra=400000, resultado_mensual=250000)
        id_insertado = CalculosController.insertar(calc)
        resultado = CalculosController.buscar_por_id(id_insertado)
        self.assertEqual(resultado.interes_anual, 0)
        self.assertAlmostEqual(resultado.resultado_mensual, 250000, 0)

    def test_insertar_calculo3(self):
        """Inserta un cálculo con abono extra"""
        calc = CalculoAhorro(id_usuario=1, meta=10000000, plazo_meses=10, interes_anual=12,
                             abono_extra=2000000, resultado_mensual=694400)
        CalculosController.insertar(calc)
        resultado = CalculosController.buscar_por_id(3)
        self.assertEqual(resultado.abono_extra, 2000000)

    """------------------ CASOS PARA MODIFICAR ------------------"""
    def test_modificar_calculo1(self):
        """Modifica la meta de un cálculo existente"""
        CalculosController.modificar_calculo(1, 6000000, 24, 6, 0, 216000)
        modificado = CalculosController.buscar_por_id(1)
        self.assertEqual(modificado.meta, 6000000)

    def test_modificar_calculo2(self):
        """Modifica el plazo de un cálculo"""
        CalculosController.modificar_calculo(2, 2400000, 12, 0, 400000, 166000)
        modificado = CalculosController.buscar_por_id(2)
        self.assertEqual(modificado.plazo_meses, 12)

    def test_modificar_calculo3(self):
        """Modifica el interés y resultado"""
        CalculosController.modificar_calculo(3, 10000000, 10, 10, 2000000, 650000)
        modificado = CalculosController.buscar_por_id(3)
        self.assertEqual(modificado.interes_anual, 10)

    """------------------ CASOS PARA BUSCAR ------------------"""
    def test_buscar_por_id(self):
        """Busca un cálculo específico"""
        resultado = CalculosController.buscar_por_id(1)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.id_calculo, 1)

    def test_buscar_por_usuario(self):
        """Busca todos los cálculos de un usuario"""
        resultados = CalculosController.buscar_por_usuario(1)
        self.assertGreaterEqual(len(resultados), 3)

    def test_buscar_inexistente(self):
        """Busca un cálculo que no existe"""
        resultado = CalculosController.buscar_por_id(9999)
        self.assertIsNone(resultado)

    @classmethod
    def tearDownClass(cls):
        """Limpieza final de las tablas"""
        try:
            CalculosController.borrar_tabla()
        except Exception as e:
            print("⚠️ Error al borrar tabla calculos:", e)
        try:
            UsuariosController.borrar_tabla()
        except Exception as e:
            print("⚠️ Error al borrar tabla usuarios:", e)


if __name__ == "__main__":
    unittest.main()
