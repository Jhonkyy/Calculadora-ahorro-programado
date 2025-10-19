class CalculoAhorro:
    def __init__(self, id_calculo=None, id_usuario=None, meta=None, plazo_meses=None,
                 interes_anual=None, abono_extra=None, resultado_mensual=None, fecha_registro=None):
        
        self.id_calculo = id_calculo
        self.id_usuario = id_usuario
        self.meta = meta
        self.plazo_meses = plazo_meses
        self.interes_anual = interes_anual
        self.abono_extra = abono_extra
        self.resultado_mensual = resultado_mensual
        self.fecha_registro = fecha_registro