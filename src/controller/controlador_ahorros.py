import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2
from model.calculo_ahorro import CalculoAhorro
import secret_config

class CalculosController:

    def crear_tabla():
        cursor = CalculosController.obtener_cursor()
        with open("sql/crear-calculos.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    def borrar_tabla():
        cursor = CalculosController.obtener_cursor()
        with open("sql/borrar-calculos.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    def insertar(calculo: CalculoAhorro):
        """Inserta un cálculo realizado por un usuario"""
        cursor = CalculosController.obtener_cursor()
        consulta = f"""
        INSERT INTO calculos_ahorro 
        (id_usuario, meta, plazo_meses, interes_anual, abono_extra, resultado_mensual)
        VALUES 
        ({calculo.id_usuario}, {calculo.meta}, {calculo.plazo_meses}, 
        {calculo.interes_anual}, {calculo.abono_extra}, {calculo.resultado_mensual})
        """
        cursor.execute(consulta)
        cursor.connection.commit()

    def buscar_por_id(id_calculo) -> CalculoAhorro:
        """Busca un cálculo específico por su ID"""
        cursor = CalculosController.obtener_cursor()
        consulta = f"""
        SELECT id_calculo, id_usuario, meta, plazo_meses, interes_anual, 
               abono_extra, resultado_mensual, fecha_registro
        FROM calculos_ahorro WHERE id_calculo = {id_calculo}
        """
        cursor.execute(consulta)
        fila = cursor.fetchone()
        if not fila:
            return None
        return CalculoAhorro(
            id_calculo=fila[0], id_usuario=fila[1], meta=fila[2], plazo_meses=fila[3],
            interes_anual=fila[4], abono_extra=fila[5], resultado_mensual=fila[6],
            fecha_registro=fila[7]
        )

    def buscar_por_usuario(id_usuario) -> list[CalculoAhorro]:
        """Devuelve todos los cálculos de un usuario"""
        cursor = CalculosController.obtener_cursor()
        consulta = f"""
        SELECT id_calculo, id_usuario, meta, plazo_meses, interes_anual, 
               abono_extra, resultado_mensual, fecha_registro
        FROM calculos_ahorro WHERE id_usuario = {id_usuario}
        """
        cursor.execute(consulta)
        filas = cursor.fetchall()
        if not filas:
            return []

        lista = []
        for fila in filas:
            calculo = CalculoAhorro(
                id_calculo=fila[0], id_usuario=fila[1], meta=fila[2],
                plazo_meses=fila[3], interes_anual=fila[4], abono_extra=fila[5],
                resultado_mensual=fila[6], fecha_registro=fila[7]
            )
            lista.append(calculo)
        return lista

    def modificar_calculo(id_calculo, nueva_meta, nuevo_plazo, nuevo_interes, nuevo_abono, nuevo_resultado):
        """Modifica un cálculo existente"""
        cursor = CalculosController.obtener_cursor()
        consulta = f"""
        UPDATE calculos_ahorro
        SET meta = {nueva_meta}, plazo_meses = {nuevo_plazo}, 
            interes_anual = {nuevo_interes}, abono_extra = {nuevo_abono}, 
            resultado_mensual = {nuevo_resultado}
        WHERE id_calculo = {id_calculo}
        """
        cursor.execute(consulta)
        cursor.connection.commit()

    def eliminar(id_calculo):
        """Elimina un cálculo"""
        cursor = CalculosController.obtener_cursor()
        consulta = f"DELETE FROM calculos_ahorro WHERE id_calculo = {id_calculo}"
        cursor.execute(consulta)
        cursor.connection.commit()

    def obtener_cursor():
        """Crea la conexión a la base de datos y retorna un cursor"""
        connection = psycopg2.connect(
            database=secret_config.PGDATABASE,
            user=secret_config.PGUSER,
            password=secret_config.PGPASSWORD,
            host=secret_config.PGHOST,
            port=secret_config.PGPORT
        )
        return connection.cursor()