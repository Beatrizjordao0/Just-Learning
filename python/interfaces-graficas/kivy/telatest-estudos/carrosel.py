from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar, MDBottomAppBar

KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'MDCarousel Example'
            elevation: 10
        MDCarousel:
            id: carousel
            direction: 'right'
            loop: True
            on_slide_progress: app.on_slide_progress

            BoxLayout:
                orientation: 'vertical'
                MDLabel:
                    text: 'Slide 1'
                    halign: 'center'
                MDIconButton:
                    icon: 'slide-1'
                    pos_hint: {"center_x": .5}

            BoxLayout:
                orientation: 'vertical'
                MDLabel:
                    text: 'Slide 2'
                    halign: 'center'
                MDIconButton:
                    icon: 'slide-2'
                    pos_hint: {"center_x": .5}

            BoxLayout:
                orientation: 'vertical'
                MDLabel:
                    text: 'Slide 3'
                    halign: 'center'
                MDIconButton:
                    icon: 'slide-3'
                    pos_hint: {"center_x": .5}
            BoxLayout:
                orientation: 'vertical'
                MDLabel:
                    text: 'This is slide 4'
                    halign: 'center'
                MDIconButton:
                    icon: 'slide-4'
                    pos_hint: {"center_x": .5}
'''


class MainScreen(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def on_slide_progress(self, instance_carousel, progress):
        # Aqui você pode adicionar código para responder ao progresso da transição
        pass


if __name__ == '__main__':
    MyApp().run()
