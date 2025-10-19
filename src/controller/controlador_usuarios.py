import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2
from model.usuario import Usuario
import secret_config

class UsuariosController:

    def crear_tabla():
        cursor = UsuariosController.obtener_cursor()
        with open("sql/crear-usuarios.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    def borrar_tabla():
        cursor = UsuariosController.obtener_cursor()
        with open("sql/borrar-usuarios.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    def insertar(usuario: Usuario):
        cursor = UsuariosController.obtener_cursor()
        consulta = f"""
        INSERT INTO usuarios (nombre)
        VALUES ('{usuario.nombre}')
        """
        cursor.execute(consulta)
        cursor.connection.commit()

    def buscar_por_id(id_usuario) -> Usuario:
        cursor = UsuariosController.obtener_cursor()
        consulta = f"""
        SELECT id_usuario, nombre
        FROM usuarios WHERE id_usuario = {id_usuario}
        """
        cursor.execute(consulta)
        fila = cursor.fetchone()
        if not fila:
            return None
        return Usuario(id_usuario=fila[0], nombre=fila[1])

    def modificar_nombre(id_usuario, nuevo_nombre):
        cursor = UsuariosController.obtener_cursor()
        consulta = f"""
        UPDATE usuarios
        SET nombre = '{nuevo_nombre}'
        WHERE id_usuario = {id_usuario}
        """
        cursor.execute(consulta)
        cursor.connection.commit()

    def eliminar(id_usuario):
        cursor = UsuariosController.obtener_cursor()
        consulta = f"""
        DELETE FROM usuarios WHERE id_usuario = {id_usuario}
        """
        cursor.execute(consulta)
        cursor.connection.commit()

    def obtener_cursor():
        connection = psycopg2.connect(
            database=secret_config.PGDATABASE, 
            user=secret_config.PGUSER, 
            password=secret_config.PGPASSWORD, 
            host=secret_config.PGHOST, 
            port=secret_config.PGPORT
        )
        return connection.cursor()