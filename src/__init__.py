from kivy.app import App
from kivy.properties import ObjectProperty
from .styles import load_styles, Theme
from .utils import AppScreenManager

# import controller here

class KivyApp(App):
    # make theme avalable
    theme = ObjectProperty()

    def __init__(self, **kwargs):
        # Make the theme available globally
        self.theme = Theme()

        # then load root 
        super().__init__(**kwargs)
    
    def build(self):
        # Load styles before building the root widget
        load_styles()

        # return the screen manager
        screen_manager = AppScreenManager()

        # Instantiate controllers and add their views to the screen manager
        # screen_manager.add_wrapped_layout()
        ...

        return screen_manager
            
        