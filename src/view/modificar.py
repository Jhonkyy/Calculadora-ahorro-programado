import sys
sys.path.append(".")
sys.path.append("src")

from controller.controlador_ahorros import CalculosController
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ModificarLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = 16

        # --- ID del cálculo ---
        self.add_widget(Label(text="ID del cálculo a modificar"))
        self.id_input = TextInput(hint_text="Ej: 1", input_filter="int", multiline=False)
        self.add_widget(self.id_input)

        # --- Campos nuevos ---
        self.add_widget(Label(text="Nueva meta"))
        self.meta_input = TextInput(hint_text="Ej: 1000000", input_filter="float", multiline=False)
        self.add_widget(self.meta_input)

        self.add_widget(Label(text="Nuevo plazo (meses)"))
        self.plazo_input = TextInput(hint_text="Ej: 12", input_filter="int", multiline=False)
        self.add_widget(self.plazo_input)

        self.add_widget(Label(text="Nuevo interés anual (%)"))
        self.interes_input = TextInput(hint_text="Ej: 6", input_filter="float", multiline=False)
        self.add_widget(self.interes_input)

        self.add_widget(Label(text="Nuevo abono extra"))
        self.extra_input = TextInput(hint_text="Ej: 50000", input_filter="float", multiline=False)
        self.add_widget(self.extra_input)

        self.add_widget(Label(text="Nuevo resultado mensual"))
        self.resultado_input = TextInput(hint_text="Ej: 180000", input_filter="float", multiline=False)
        self.add_widget(self.resultado_input)

        # --- Botón modificar ---
        self.modificar_btn = Button(text="Modificar Cálculo", size_hint_y=None, height=48)
        self.modificar_btn.bind(on_release=self.on_modificar)
        self.add_widget(self.modificar_btn)

        # --- Mensaje ---
        self.mensaje_lbl = Label(text="", color=(1, 1, 1, 1))
        self.add_widget(self.mensaje_lbl)

    def on_modificar(self, _instance):
        """Acción al presionar el botón 'Modificar'"""
        try:
            if not self.id_input.text:
                self.mensaje_lbl.text = "Debe ingresar el ID del cálculo."
                return

            id_calculo = int(self.id_input.text)
            nueva_meta = float(self.meta_input.text or 0)
            nuevo_plazo = int(self.plazo_input.text or 0)
            nuevo_interes = float(self.interes_input.text or 0)
            nuevo_abono = float(self.extra_input.text or 0)
            nuevo_resultado = float(self.resultado_input.text or 0)

            # Llamada al controlador
            CalculosController.modificar_calculo(
                id_calculo,
                nueva_meta,
                nuevo_plazo,
                nuevo_interes,
                nuevo_abono,
                nuevo_resultado
            )

            self.mensaje_lbl.text = f"Cálculo #{id_calculo} modificado correctamente ✅"
        except Exception as e:
            self.mensaje_lbl.text = f"Error: {e}"


class ModificarApp(App):
    def build(self):
        self.title = "Modificar Cálculos"
        return ModificarLayout()


if __name__ == "__main__":
    ModificarApp().run()
