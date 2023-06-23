from kivy.app import App
from kivy.uix.label import Label

class Finder(App):
    def build(self):
        return Label(text='Inicio del proyecto Kivy para localizador')

if __name__ == '__main__':
    Finder().run()

