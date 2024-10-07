from kivy.app import App

# import controller here

class MyApp(App):
    def build(self):
        self.controller = Controller()
        return self.controller.get_view()