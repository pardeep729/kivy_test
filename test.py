# Environment Varilabes (https://kivy.org/doc/stable/guide/environment.html)
import os
# e.g:  os.environ['KIVY_TEXT'] = 'pil'


import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2 # Number of columns in grid
        # self.rows = 2 # Number of rows in grid

        # Arrange child widgets on screen
        self.add_widget(Label(text="User name:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="Password:"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class MyApp(App):
    def build(self):
        # return Label(text="Wagwarn brederin")
        # return Button(text='yo')
        return LoginScreen()

if __name__ == '__main__':
    my_app = MyApp()
    my_app.run()