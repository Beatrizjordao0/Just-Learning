from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image

musica = ['Quando estou só',
          'e o choro parece querer chegar',
          'e o sentimento de temor',
          'como será',
          'o amanhã que eu não vejo',
          'e quer me assustar',
          'oh meu Deus ajuda me a confiar',
          'quando os sonhos se frustram',
          'ou parecem não se realizar',
          'quando as forças se acabam',
          'tudo o que eu sei é te adorar.']

numero = 0
def botao_pressionado(instance):
    global numero
    if numero < len(musica):
        print(musica[numero])
        numero += 1
    else:
        numero = 0
        print('RECOMEÇANDO...')

class MinhaApp(App):
    def build(self):

        layout = BoxLayout(orientation='vertical') 

        # Adicionando a frase
        frase_layout = BoxLayout(orientation='horizontal', 
                                  size_hint=(1, None), 
                                  height='50sp',
                                  spacing=10)
        
        frase_label = Label(text='Jesus é bom?', 
                            color=[1, 1, 0, 1], 
                            font_size=20)
        
        frase_layout.add_widget(frase_label)
        layout.add_widget(frase_layout)

        # Adicionando a checkbox no centro abaixo da frase
        checkbox_layout = BoxLayout(orientation='horizontal', 
                                    size_hint=(1, None), 
                                    height='50sp',
                                    spacing=10,
                                    padding=(0, 50, 0, 0))
        checkbox_layout.add_widget(Label())  # Espaço em branco para centralizar a checkbox
        checkbox_layout.add_widget(CheckBox(size_hint=(None, None), 
                                             size=('30sp', '30sp')))
        checkbox_layout.add_widget(Label())  # Espaço em branco para centralizar a checkbox
        layout.add_widget(checkbox_layout)

        # Adicionando o botão no centro da tela
        btn = Button(text='Click me',
                    font_size=50, 
                    background_color=get_color_from_hex('#FF0000'), 
                    size_hint=(None, None), size=(300, 100),
                    pos_hint={'center_x': 0.5})
        btn.bind(on_press=botao_pressionado)
        layout.add_widget(btn)

        img = Image(source='C:\\Users\\beatr\\Dropbox\\PC\\Downloads\\mama.jpg')
        layout.add_widget(img)
        return layout
    
if __name__ == '__main__':
    MinhaApp().run()
