import sys
sys.path.append("src")

from model.ahorro import calcular_ahorro
from model.ahorro import ErrorMetaNegativa, ErrorPlazoCero, ErrorExtraMayorMeta

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard


class AhorroLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = 16

        # Meta
        self.add_widget(Label(text="Meta de ahorro"))
        self.meta_input = TextInput(hint_text="Ej: 1000000", input_filter="float", multiline=False)
        self.add_widget(self.meta_input)

        # Plazo
        self.add_widget(Label(text="Plazo (meses)"))
        self.plazo_input = TextInput(hint_text="Ej: 12", input_filter="int", multiline=False)
        self.add_widget(self.plazo_input)

        # Abono extra
        self.add_widget(Label(text="Abono extra"))
        self.extra_input = TextInput(hint_text="Ej: 100000", input_filter="float", multiline=False)
        self.add_widget(self.extra_input)

        # Botones
        botones = BoxLayout(orientation="horizontal", spacing=8, size_hint_y=None, height=48)
        self.calcular_btn = Button(text="Calcular")
        self.calcular_btn.bind(on_release=self.on_calcular)
        self.limpiar_btn = Button(text="Limpiar")
        self.limpiar_btn.bind(on_release=self.on_limpiar)
        self.ejemplo_btn = Button(text="Llenar ejemplo")
        self.ejemplo_btn.bind(on_release=self.on_ejemplo)
        self.copiar_btn = Button(text="Copiar resultado")
        self.copiar_btn.bind(on_release=self.on_copiar)
        botones.add_widget(self.calcular_btn)
        botones.add_widget(self.limpiar_btn)
        botones.add_widget(self.ejemplo_btn)
        botones.add_widget(self.copiar_btn)
        self.add_widget(botones)

        # Resultado
        self.resultado_lbl = Label(text="Resultado mensual: -", size_hint_y=None, height=32)
        self.add_widget(self.resultado_lbl)

    def on_calcular(self, _instance):
        try:
            # Validación previa de campos vacíos
            if not self.meta_input.text or not self.plazo_input.text:
                self.resultado_lbl.text = "Complete meta y plazo"
                return

            meta_valor = float(self.meta_input.text)
            plazo_valor = int(self.plazo_input.text)
            extra_valor = float(self.extra_input.text or 0)

            resultado = calcular_ahorro(meta_valor, plazo_valor, extra_valor)
            self.resultado_lbl.text = f"Resultado mensual: {resultado:.2f}"

        except ValueError:
            self.resultado_lbl.text = "Entradas inválidas: use números válidos"
        except ErrorMetaNegativa:
            self.resultado_lbl.text = "Error: la meta no puede ser negativa"
        except ErrorPlazoCero:
            self.resultado_lbl.text = "Error: el plazo debe ser mayor que 0"
        except ErrorExtraMayorMeta:
            self.resultado_lbl.text = "Error: el extra no puede superar la meta"
        except Exception:
            self.resultado_lbl.text = "Ocurrió un error inesperado"

    def on_limpiar(self, _instance):
        self.meta_input.text = ""
        self.plazo_input.text = ""
        self.extra_input.text = ""
        self.resultado_lbl.text = "Resultado mensual: -"

    def on_ejemplo(self, _instance):
        self.meta_input.text = "1100000"
        self.plazo_input.text = "6"
        self.extra_input.text = "0"

    def on_copiar(self, _instance):
        # Copia solo el número si está disponible
        texto = self.resultado_lbl.text.replace("Resultado mensual:", "").strip()
        if texto and texto != "-" and "Error" not in texto:
            Clipboard.copy(texto)


class AhorroApp(App):
    def build(self):
        self.title = "Calculadora de Ahorro"
        return AhorroLayout()


if __name__ == "__main__":
    AhorroApp().run()