import sys
sys.path.append(".")
sys.path.append("src")

from controller.controlador_ahorros import CalculosController
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class InsertarLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = 16

        # --- Campos de entrada ---
        self.add_widget(Label(text="Meta (monto a alcanzar)"))
        self.meta_input = TextInput(hint_text="Ej: 5000000", input_filter="float", multiline=False)
        self.add_widget(self.meta_input)

        self.add_widget(Label(text="Plazo (meses)"))
        self.plazo_input = TextInput(hint_text="Ej: 24", input_filter="int", multiline=False)
        self.add_widget(self.plazo_input)

        self.add_widget(Label(text="Interés anual (%)"))
        self.interes_input = TextInput(hint_text="Ej: 6", input_filter="float", multiline=False)
        self.add_widget(self.interes_input)

        self.add_widget(Label(text="Abono extra"))
        self.extra_input = TextInput(hint_text="Ej: 100000", input_filter="float", multiline=False)
        self.add_widget(self.extra_input)

        self.add_widget(Label(text="Resultado mensual"))
        self.resultado_input = TextInput(hint_text="Ej: 180000", input_filter="float", multiline=False)
        self.add_widget(self.resultado_input)

        # --- Botón insertar ---
        self.insertar_btn = Button(text="Insertar Cálculo", size_hint_y=None, height=48)
        self.insertar_btn.bind(on_release=self.on_insertar)
        self.add_widget(self.insertar_btn)

        # --- Mensaje de confirmación ---
        self.mensaje_lbl = Label(text="", color=(1, 1, 1, 1))
        self.add_widget(self.mensaje_lbl)

    def on_insertar(self, _instance):
        """Acción al presionar 'Insertar'"""
        try:
            meta = float(self.meta_input.text or 0)
            plazo = int(self.plazo_input.text or 0)
            interes = float(self.interes_input.text or 0)
            extra = float(self.extra_input.text or 0)
            resultado = float(self.resultado_input.text or 0)

            if meta <= 0 or plazo <= 0:
                self.mensaje_lbl.text = "Debe ingresar valores válidos."
                return

            # Llamada al controlador
            CalculosController.insertar_calculo(meta, plazo, interes, extra, resultado)

            self.mensaje_lbl.text = "✅ Cálculo insertado correctamente."

            # Limpiar campos
            self.meta_input.text = ""
            self.plazo_input.text = ""
            self.interes_input.text = ""
            self.extra_input.text = ""
            self.resultado_input.text = ""

        except Exception as e:
            self.mensaje_lbl.text = f"Error: {e}"


class InsertarApp(App):
    def build(self):
        self.title = "Insertar Cálculo"
        return InsertarLayout()


if __name__ == "__main__":
    InsertarApp().run()
