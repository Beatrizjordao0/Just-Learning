from kivy.lang import Builder
from kivymd.app import MDApp

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"  # "Purple", "Red"
        return Builder.load_file('kivymd-theming.kv')

Example().run()

