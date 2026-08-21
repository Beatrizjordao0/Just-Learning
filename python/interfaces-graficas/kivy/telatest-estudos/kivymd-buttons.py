from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder

from kivymd.uix.button import (MDIconButton, # Apenas ícones
                               MDFlatButton, # Apenas Texto
                               MDTextButton,
                               MDRectangleFlatButton,
                               MDRaisedButton,
                               MDFillRoundFlatButton,
                               MDFloatingActionButton,
                               MDRoundFlatButton,
                               MDRoundFlatIconButton,
                               MDRectangleFlatIconButton,
                               MDFillRoundFlatIconButton,
                               MDFloatingActionButtonSpeedDial)

class ButtonApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"  # "Purple", "Red"
        return Builder.load_file('kivymd-button.kv')


if __name__=='__main__':
    ButtonApp().run()