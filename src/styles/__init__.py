import os
from kivy.lang import Builder
from .theme import Theme

def load_styles():
    DIR = os.path.dirname(os.path.abspath(__file__))
    theme_files = [os.path.join(DIR, path) for path in os.listdir(DIR) if path.endswith(".kv")]
    for file in theme_files:
        Builder.load_file(file)