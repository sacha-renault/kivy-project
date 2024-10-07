from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Builder.load_file('src/views/template_view.kv')

class TemplateView(BoxLayout):
    controller = ObjectProperty()
    def __init__(self, controller, **kwargs):
        self.controller = controller
        super().__init__(**kwargs)