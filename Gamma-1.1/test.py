from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

class Test(MDApp):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.button = Button(text='Press me', pos_hint={"center_x": .5, "center_y": .5})
        self.button.bind(on_release=self.menu_open)
        self.layout.add_widget(self.button)

        return self.layout

    def menu_open(self, instance):
        menu_items = [
            {
                "text": f"Item {i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        menu = MDDropdownMenu(caller=instance, items=menu_items)
        menu.open()

    def menu_callback(self, text_item):
        print(text_item)

if __name__ == '__main__':
    Test().run()
