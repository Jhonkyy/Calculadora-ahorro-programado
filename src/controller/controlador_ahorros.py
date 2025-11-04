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
        """Inserta un cálculo realizado por un usuario y devuelve su ID"""
        cursor = CalculosController.obtener_cursor()
        consulta = """
            INSERT INTO calculos 
            (id_usuario, meta, plazo_meses, interes_anual, abono_extra, resultado_mensual)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id_calculo;
        """
        cursor.execute(consulta, (
            calculo.id_usuario,
            calculo.meta,
            calculo.plazo_meses,
            calculo.interes_anual,
            calculo.abono_extra,
            calculo.resultado_mensual
        ))
        id_generado = cursor.fetchone()[0]
        cursor.connection.commit()
        return id_generado

    def buscar_por_id(id_calculo) -> CalculoAhorro | None:
        """Busca un cálculo específico por su ID"""
        cursor = CalculosController.obtener_cursor()
        consulta = """
            SELECT id_calculo, id_usuario, meta, plazo_meses, interes_anual, 
                   abono_extra, resultado_mensual
            FROM calculos 
            WHERE id_calculo = %s
        """
        cursor.execute(consulta, (id_calculo,))
        fila = cursor.fetchone()
        if not fila:
            return None
        return CalculoAhorro(
            id_calculo=fila[0],
            id_usuario=fila[1],
            meta=fila[2],
            plazo_meses=fila[3],
            interes_anual=fila[4],
            abono_extra=fila[5],
            resultado_mensual=fila[6]
        )

    def buscar_por_usuario(id_usuario) -> list[CalculoAhorro]:
        """Devuelve todos los cálculos asociados a un usuario"""
        cursor = CalculosController.obtener_cursor()
        consulta = """
            SELECT id_calculo, id_usuario, meta, plazo_meses, interes_anual, 
                   abono_extra, resultado_mensual
            FROM calculos 
            WHERE id_usuario = %s
        """
        cursor.execute(consulta, (id_usuario,))
        filas = cursor.fetchall()
        lista = []
        for fila in filas:
            calculo = CalculoAhorro(
                id_calculo=fila[0],
                id_usuario=fila[1],
                meta=fila[2],
                plazo_meses=fila[3],
                interes_anual=fila[4],
                abono_extra=fila[5],
                resultado_mensual=fila[6]
            )
            lista.append(calculo)
        return lista

    def modificar_calculo(id_calculo, nueva_meta, nuevo_plazo, nuevo_interes, nuevo_abono, nuevo_resultado):
        """Modifica un cálculo existente"""
        cursor = CalculosController.obtener_cursor()
        consulta = """
            UPDATE calculos
            SET meta = %s,
                plazo_meses = %s,
                interes_anual = %s,
                abono_extra = %s,
                resultado_mensual = %s
            WHERE id_calculo = %s
        """
        cursor.execute(consulta, (nueva_meta, nuevo_plazo, nuevo_interes, nuevo_abono, nuevo_resultado, id_calculo))
        cursor.connection.commit()

    def eliminar(id_calculo):
        """Elimina un cálculo"""
        cursor = CalculosController.obtener_cursor()
        consulta = "DELETE FROM calculos WHERE id_calculo = %s"
        cursor.execute(consulta, (id_calculo,))
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
