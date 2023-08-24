from kivymd.app import MDApp
from kivymd.uix.button import MDTextButton
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown

class MyAnchorLayoutApp(MDApp):
    def build(self):
        self.layout = DropDown()
        self.add_button = MDTextButton(text='Add Widget', on_press=self.add_widget)
        self.layout.add_widget(self.add_button)
        return self.layout
    
    def add_widget(self, instance):
        new_button = Label(text='New Widget\n10000000000000\n000000000000', size_hint=(None, None), size=(100, 50))
        self.layout.add_widget(new_button)

if __name__ == '__main__':
    MyAnchorLayoutApp().run()






