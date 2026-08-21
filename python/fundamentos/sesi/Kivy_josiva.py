# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput


# class LoginScreen(GridLayout):

#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text='User Name'))
#         self.username = TextInput(multiline=True)
#         self.add_widget(self.username)
#         self.add_widget(Label(text='password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)


# class MyApp(App):

#     def build(self):
#         return LoginScreen()


# if __name__ == '__main__':
#     MyApp().run()
# class MyApp(App):

#     def build(self):
#         return Label(text='Hello world')

# class MyApp(App):
#     def build(self):
#         layout = BoxLayout(padding=250)
#         button = Button(text='Hi! I\'m Beatriz', size=(50, 40))
#         layout.add_widget(button)
    
#         return layout
    

# if __name__ == '__main__':
#     MyApp().run()


