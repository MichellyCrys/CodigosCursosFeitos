
from kivy.app import App
#from kivy.uix.label import Label
from kivy.uix.image import AsyncImage

class MainApp(App):
    def build(self):
        img = AsyncImage(source='https://supermariorun.com/assets/img/stage/mario03.png',
                         size_hint=(.5, .5),
                         pos_hint={'x': .5, 'y': .5})
        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()