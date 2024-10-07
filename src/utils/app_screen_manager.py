from kivy.uix.screenmanager import ScreenManager, Screen

class AppScreenManager(ScreenManager):
    def add_wrapped_layout(self, layout, screen_name: str) -> Screen:
        # Create a new Screen
        wrapped_screen = Screen(name=screen_name)

        # Add the provided layout to the Screen
        wrapped_screen.add_widget(layout)
        
        # Add the Screen to the ScreenManager
        self.add_widget(wrapped_screen)

        return wrapped_screen