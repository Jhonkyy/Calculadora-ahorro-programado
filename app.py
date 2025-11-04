from flask import Flask, render_template, request


import sys
sys.path.append("src")

from src.model.ahorro import calcular_ahorro 

app = Flask(__name__)
@app.route("/")
def menu():
    return render_template("menu.html")

@app.route("/ahorro")
def ahorro():
    return render_template("ahorro.html")

@app.route("/calcular_ahorros")
def calcular_ahorros():
    meta = float(request.args["meta"])
    plazo = float(request.args["plazo"])
    interes = float(request.args["interes"])
    abono = float(request.args["abono"])
    
    
    cuota = calcular_ahorro(meta,plazo,interes,abono)
    return f"el valor a ahorrar es: {cuota}"

app.run(debug=True)