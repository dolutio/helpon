from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ScreenChangerButton(Button):
    def __init__(self, screen_manager, text=None, **kwargs):
        super().__init__()
        
        if self.text is None:
            print('Screen with this name not found!')
            exit()
    def on_press(self):
        self.screen_manager.current = self.text

class Home(BoxLayout):
    def __init__(self, screen_manager):
            super().__init__()
            self.orientation = 'vertical'
            self.screen_manager = screen_manager

            self.btna = Button(text='Algebra', on_press=self.to_algebra_screen)
            self.btng = Button(text='Geometry', on_press=self.to_geometry_screen)
            self.btnph = Button(text='Physics', on_press=self.to_physics_screen)
            self.btnch = Button(text='Chemistry', on_press=self.to_chemistry_screen)
            self.add_widget(self.btna)
            self.add_widget(self.btng)
            self.add_widget(self.btnph)
            self.add_widget(self.btnch)
    def change_screen(required_screen):
        self.screen_manger.current = reuired_screen
    def to_algebra_screen(self, *args):
        self.screen_manager.current = 'Algebra'
    def to_geometry_screen(self, *args):
        self.screen_manager.current = 'Geometry'
    def to_physics_screen(self, *args):
        self.screen_manager.current = 'Physics'
    def to_chemistry_screen(self, *args):
        self.screen_manager.current = 'Chemistry'

class NavigationDrawerContent(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        
        self.feedback_btn = NavigationButton(
                    icon="github")
        
        self.add_widget(self.feedback_btn)