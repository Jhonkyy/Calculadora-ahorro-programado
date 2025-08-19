from ahorro import calcular_ahorro
#Leer entradas

meta = float(input("Ingrese meta de ahorro: "))
plazo = int(input("Ingrese el plazo de ahorro: "))
abono_extra = float(input("Ingrese su abono extra: "))

#Realizar proceso

cuota_ahorro = calcular_ahorro(meta, plazo, abono_extra)

#Mostrar salidas

print(cuota_ahorro)