import os
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.screen import MDScreen
import pyrebase

# Configuração do Firebase
firebaseConfig = {
    "apiKey": os.getenv("FIREBASE_API_KEY", ""),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN", ""),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL", ""),
    "projectId": os.getenv("FIREBASE_PROJECT_ID", ""),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET", ""),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID", ""),
    "appId": os.getenv("FIREBASE_APP_ID", ""),
}

firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

KV = '''
<TelaconfigPerfil>:
    name: 'config_Perfil'
    background_color:  '#FFFFFF'
    Image:
        source: 'BackgroundPerfil.png'
        allow_stretch: True
        keep_ratio: False
    FloatLayout:
        spacing: 14
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        size_hint: None, None
        size: dp(360), dp(160)                    
        MDCard:
            id: card_image
            size_hint_x: None
            size: dp(160), dp(160)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            elevation: 1
            orientation: 'vertical'
            md_bg_color: 0, 0, 0, 1  
            mode: "round"
            FitImage:
                id: profile_image_large
                source: root.large_image_path
                allow_stretch: True
                keep_ratio: False
        MDIconButton:
            icon: 'arrow-left'
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1
            pos_hint: {'center_x': 0.1, 'center_y': 0.7}
            size_hint: None, None
            size: dp(48), dp(48)
            on_release: 
                app.root.transition.direction = "right"
                app.root.current = 'Menu'               
        MDIconButton:
            icon: 'camera'
            theme_text_color: "Custom"
            pos_hint: {'center_x': 0.9,'center_y': 0.7}
            size_hint: None, None
            size: dp(48), dp(48)
            text_color: 0, 0, 0, 1  
            on_release: root.open_file_chooser_large()
    FloatLayout:
        size_hint: None, None
        size: dp(100), dp(100) 
        pos_hint: {'center_x': 0.2, 'center_y': 0.78}
        Image:
            id: profile_image_small
            source: root.small_image_path
            allow_stretch: True
            keep_ratio: False
            size_hint: None, None
            size: dp(100), dp(100)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            radius:[100, 100, 100, 100]
        MDIconButton:
            icon: 'camera'
            theme_text_color: "Custom"
            pos_hint: {'center_x': 0.82,'center_y': 0.14}
            size_hint: None, None
            size: dp(48), dp(48)
            text_color: 0, 0, 0, 1  
            on_release: root.open_file_chooser_small()
'''


class TelaconfigPerfil(MDScreen):
    large_image_path = StringProperty('default_large_profile.png')
    small_image_path = StringProperty('default_small_profile.png')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            select_path=self.select_path_large,
            exit_manager=self.exit_manager,
            preview=True
        )

        self.file_manager_small = MDFileManager(
            select_path=self.select_path_small,
            exit_manager=self.exit_manager_small,
            preview=True
        )

        # Adicione a configuração do usuário aqui
        self.user = {
            "localId": "user_local_id",
            "idToken": "user_id_token"
        }

    def open_file_chooser_large(self):
        self.file_manager.show('/')

    def open_file_chooser_small(self):
        self.file_manager_small.show('/')

    def select_path_large(self, path):
        self.large_image_path = path
        self.upload_image(path, "large")

    def select_path_small(self, path):
        self.small_image_path = path
        self.upload_image(path, "small")

    def upload_image(self, path, size_type):
        try:
            if path:
                large_file = f"user_banner/{self.user['localId']}_large.jpg"
                small_file = f"user_banner/{self.user['localId']}_small.jpg"
                file_name = large_file if size_type == "large" else small_file
                storage.child(file_name).put(path, self.user['idToken'])
                url = storage.child(file_name).get_url(self.user['idToken'])
                database.child("users").child(self.user['localId']).update({f"profile_pic_{size_type}": url})
        except Exception as e:
            print(e)

    def exit_manager(self, *args):
        self.file_manager.close()

    def exit_manager_small(self, *args):
        self.file_manager_small.close()


class MainApp(MDApp):
    def build(self):
        Builder.load_string(KV)
        return TelaconfigPerfil()


MainApp().run()
