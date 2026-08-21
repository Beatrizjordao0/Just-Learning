from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


Window.size = (500, 500)


class LoginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.label_color = get_color_from_hex('#00ced9')

        return Builder.load_file('login-tlauncher.kv')

LoginApp().run()