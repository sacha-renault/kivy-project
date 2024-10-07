from src.models.template_model import TemplateModel
from src.views.template_view import TemplateView

class TemplateController:
    def __init__(self):
        self.model = TemplateModel()
        self.view = TemplateView(controller=self)

    def get_view(self):
        return self.view
