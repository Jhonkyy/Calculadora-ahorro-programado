CREATE TABLE IF NOT EXISTS calculos (
    id_calculo SERIAL PRIMARY KEY,
    id_usuario INTEGER REFERENCES usuarios(id_usuario),
    meta NUMERIC NOT NULL,
    plazo_meses INTEGER NOT NULL,
    interes_anual NUMERIC NOT NULL,
    abono_extra NUMERIC NOT NULL,
    resultado_mensual NUMERIC NOT NULL
);