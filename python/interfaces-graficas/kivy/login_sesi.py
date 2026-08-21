from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
from kivy.core.window import Window

class LoginPage(BoxLayout):
    """
    Class that defines the login page.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Main BoxLayout to vertically center everything
        self.vertical_layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        self.add_widget(self.vertical_layout)
        
        # Username input
        self.username_box = BoxLayout(orientation="horizontal", size_hint_y=None, height=30)
        self.vertical_layout.add_widget(self.username_box)
        self.username_box.add_widget(Label(text="Username:", size_hint_x=None, width=100, halign="right"))
        self.username_input = TextInput(multiline=False)
        self.username_box.add_widget(self.username_input)
        
        # Password input
        self.password_box = BoxLayout(orientation="horizontal", size_hint_y=None, height=30)
        self.vertical_layout.add_widget(self.password_box)
        self.password_box.add_widget(Label(text="Password:", size_hint_x=None, width=100, halign="right"))
        self.password_input = TextInput(multiline
                                        =False, password=True)
        self.password_box.add_widget(self.password_input)
        
        # Login button
        self.login_button = Button(text="Login", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        self.login_button.bind(on_press=self.login)
        self.vertical_layout.add_widget(self.login_button)
        
    def login(self, instance):
        """
        Method called when the login button is pressed.
        """
        check_username = self.username_input.text
        check_password = self.password_input.text
        # Here you can add your login logic, such as checking the credentials
        if check_username == self.username and check_password == self.password:
            print("Login successful")
            # Navigate to another screen or perform any other action
        else:
            print("Login failed")
            # Display a message to the user

class MyApp(App):
    def build(self):
        # Set window title and size
        self.title = "Login"
        Window.size = (400, 170)
        return LoginPage()

if __name__ == "__main__":
    MyApp().run()
