# main.py
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp


class Tela1(Screen):
    pass


class Tela2(Screen):
    pass


class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"

        # Carregar os arquivos .kv
        Builder.load_file('tela1.kv')
        Builder.load_file('tela2.kv')

        sm = ScreenManager()
        sm.add_widget(Tela1(name='tela1'))
        sm.add_widget(Tela2(name='tela2'))

        return sm

    def trocar_tela(self, nome_tela):
        self.root.current = nome_tela


if __name__ == '__main__':
    MyApp().run()
