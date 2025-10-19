import sys
sys.path.append(".")
sys.path.append("src")

from controller.controlador_ahorros import CalculosController
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout


class BuscarLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = 16

        # --- Campo para buscar por ID cálculo ---
        self.add_widget(Label(text="Buscar cálculo por ID:"))
        self.id_calculo_input = TextInput(hint_text="Ej: 1", input_filter="int", multiline=False)
        self.add_widget(self.id_calculo_input)

        self.buscar_btn = Button(text="Buscar Cálculo")
        self.buscar_btn.bind(on_release=self.on_buscar_calculo)
        self.add_widget(self.buscar_btn)

        # --- Campo para buscar por usuario ---
        self.add_widget(Label(text="Buscar cálculos de un usuario (ID Usuario):"))
        self.id_usuario_input = TextInput(hint_text="Ej: 1", input_filter="int", multiline=False)
        self.add_widget(self.id_usuario_input)

        self.buscar_usuario_btn = Button(text="Buscar por Usuario")
        self.buscar_usuario_btn.bind(on_release=self.on_buscar_usuario)
        self.add_widget(self.buscar_usuario_btn)

        # --- Área de resultados ---
        self.resultado_area = ScrollView(size_hint=(1, 1))
        self.resultado_layout = GridLayout(cols=1, size_hint_y=None, spacing=5)
        self.resultado_layout.bind(minimum_height=self.resultado_layout.setter("height"))
        self.resultado_area.add_widget(self.resultado_layout)
        self.add_widget(self.resultado_area)

    def limpiar_resultados(self):
        """Limpia los resultados previos del ScrollView."""
        self.resultado_layout.clear_widgets()

    def mostrar_resultado(self, texto):
        """Muestra un texto dentro del ScrollView."""
        self.resultado_layout.add_widget(Label(text=texto, size_hint_y=None, height=30))

    def on_buscar_calculo(self, _instance):
        """Buscar un cálculo por su ID"""
        self.limpiar_resultados()
        try:
            if not self.id_calculo_input.text:
                self.mostrar_resultado("Ingrese un ID de cálculo")
                return

            id_calculo = int(self.id_calculo_input.text)
            calculo = CalculosController.buscar_por_id(id_calculo)
            if calculo:
                texto = (
                    f"ID Cálculo: {calculo.id_calculo}\n"
                    f"Usuario: {calculo.id_usuario}\n"
                    f"Meta: {calculo.meta}\n"
                    f"Plazo: {calculo.plazo_meses} meses\n"
                    f"Interés anual: {calculo.interes_anual}%\n"
                    f"Abono extra: {calculo.abono_extra}\n"
                    f"Resultado mensual: {calculo.resultado_mensual:.2f}\n"
                    f"Fecha: {calculo.fecha_registro}"
                )
                self.mostrar_resultado(texto)
            else:
                self.mostrar_resultado("No se encontró ningún cálculo con ese ID.")
        except Exception as e:
            self.mostrar_resultado(f"Error al buscar: {e}")

    def on_buscar_usuario(self, _instance):
        """Buscar todos los cálculos de un usuario"""
        self.limpiar_resultados()
        try:
            if not self.id_usuario_input.text:
                self.mostrar_resultado("Ingrese un ID de usuario")
                return

            id_usuario = int(self.id_usuario_input.text)
            lista = CalculosController.buscar_por_usuario(id_usuario)

            if not lista:
                self.mostrar_resultado("Este usuario no tiene cálculos registrados.")
                return

            for calculo in lista:
                texto = (
                    f"[Cálculo #{calculo.id_calculo}] "
                    f"Meta: {calculo.meta} | Plazo: {calculo.plazo_meses} | "
                    f"Interés: {calculo.interes_anual}% | Resultado: {calculo.resultado_mensual:.2f}"
                )
                self.mostrar_resultado(texto)
        except Exception as e:
            self.mostrar_resultado(f"Error al buscar: {e}")


class BuscarApp(App):
    def build(self):
        self.title = "Buscar cálculos en BD"
        return BuscarLayout()


if __name__ == "__main__":
    BuscarApp().run()
