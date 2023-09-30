from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDTextButton
from kivymd.app import MDApp
from kivy.uix.dropdown import DropDown

class Test(MDApp):
    def build(self):
        self.layout = DropDown()
        self.button = MDTextButton(text='Press me', pos_hint={"center_x": .5, "center_y": .5})
        self.button.bind(on_release=self.menu_open)
        self.layout.add_widget(self.button)

        return self.layout

    def menu_open(self, instance):
        self.layout.add_widget(MDTextButton(text='Hi'))

    def menu_callback(self, text_item):
        print(text_item)

if __name__ == '__main__':
    Test().run()