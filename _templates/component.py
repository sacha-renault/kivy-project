from kivy.uix.widget import Widget
from kivy.lang import Builder

class TemplateComponent(Widget):
    def __init__(self, **kwargs):
        super(TemplateComponent, self).__init__(**kwargs)

Builder.load_file("src/components/template_component.kv")