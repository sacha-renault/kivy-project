from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from src.models.template_model import TemplateModel

Builder.load_file('src/views/template_view.kv')

class TemplateController:
    def __init__(self):
        self.model = TemplateModel()
        self.view = TemplateView(controller=self)

    def get_view(self):
        return self.view

class TemplateView(BoxLayout):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
