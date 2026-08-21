from kivy.lang import Builder
from kivy.uix.label import Label
from kivymd.app import MDApp


KV = '''
MDScreen:

    MDRaisedButton:
        text: "primary_light"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        md_bg_color: app.theme_cls.primary_light # 200

    MDRaisedButton:
        text: "primary_color" # 500
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

    MDRaisedButton:
        text: "primary_dark"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        md_bg_color: app.theme_cls.primary_dark # 700
    Label:
        text: '200'
        pos_hint: {"center_x": 0.7, "center_y": 0.7}
    Label:
        text: '500'
        pos_hint: {"center_x": 0.7, "center_y": 0.5}
    Label:
        text: '700'
        pos_hint: {"center_x": 0.7, "center_y": 0.3}

'''


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


MainApp().run()