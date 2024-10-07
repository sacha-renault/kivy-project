from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from src.models.template_model import TemplateModel

Builder.load_file('src/views/template_view.kv')

class TemplateView(BoxLayout):
    controller = ObjectProperty()
    def __init__(self, controller, **kwargs):
        self.controller = controller
        super().__init__(**kwargs)


class TemplateController:
    def __init__(self):
        self.model = TemplateModel()
        self.view = TemplateView(controller=self)

    def get_view(self):
        return self.view
