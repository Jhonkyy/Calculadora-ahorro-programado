from flask import Flask, render_template, request
import sys
sys.path.append("src")

from src.model.ahorro import calcular_ahorro
from src.controller.controlador_usuarios import UsuariosController
from src.controller.controlador_ahorros import CalculosController
from src.model.usuario import Usuario
from src.model.calculo_ahorro import CalculoAhorro

UsuariosController.crear_tabla()
CalculosController.crear_tabla()


app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("menu.html")

@app.route("/insertar")
def insertar():
    nombre = request.args.get("nombre")
    if nombre:
        usuario = Usuario(nombre=nombre)
        UsuariosController.insertar(usuario)
        return render_template("insertar.html")
    return render_template("insertar.html")

@app.route("/buscar")
def buscar():
    nombre = request.args.get("nombre")
    if nombre:
        usuario = UsuariosController.buscar_por_nombre(nombre)
        if usuario:
            calculos = CalculosController.buscar_por_usuario(usuario.id_usuario)
            return render_template("resultados.html", usuario=usuario, calculos=calculos)
        else:
            return render_template("buscar.html")
    return render_template("buscar.html")

@app.route("/ahorro")
def ahorro():
    id_usuario = request.args.get("id_usuario")
    meta = request.args.get("meta")
    plazo = request.args.get("plazo")
    interes = request.args.get("interes")
    abono = request.args.get("abono")

    if id_usuario and meta and plazo and interes and abono:
        id_usuario = int(id_usuario)
        meta = float(meta)
        plazo = float(plazo)
        interes = float(interes)
        abono = float(abono)

        resultado = calcular_ahorro(meta, plazo, interes, abono)

        calculo = CalculoAhorro(
            id_usuario=id_usuario,
            meta=meta,
            plazo_meses=plazo,
            interes_anual=interes,
            abono_extra=abono,
            resultado_mensual=resultado
        )
        CalculosController.insertar(calculo)

        return f"debes ahorrar {resultado}$ mensual"

    return render_template("ahorro.html")

if __name__ == "__main__":
    app.run(debug=True)
