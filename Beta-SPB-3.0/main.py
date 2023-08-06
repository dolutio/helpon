from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ColorProperty
from kivy.core.window import Window




Window.clearcolor = (0/255, 150/255, 150/255, 1)
colors = {
    'Cyan': {
        "200": '#009898',
        "500": '#009898',
        "700": '#009898'},
    "Light": {
        "StatusBar": "#009898",
        "AppBar": "#009898",
        "Background": "#009898",
        "CardsDialogs": "#009898",
        "FlatButtonDown": "555555",
    }}


  
class ToHomeButton(Button):
    def __init__(self, **kwargs):
        self.text = 'Home'
        




class HelpOnApp(MDApp):
    def __init__(self):
        super().__init__()
        self.icon = 'HelpOn.png'
        self.theme_cls.colors |= colors

        self.main_screen = MDNavigationLayout()

        self.navigation_drawer = MDNavigationDrawer()
        self.navigation_drawer.add_widget(NavigationButton(icon_color='white', icon='account', 
        text_color='white', text='Feedback'))

        self.screen_manager = ScreenManager(transition=NoTransition())
        self.home_screen = Screen(name="Home")
        self.algebra_screen = Screen(name='Algebra')
        self.geometry_screen = Screen(name='Geometry')
        self.physics_screen = Screen(name='Physics')
        self.chemistry_screen = Screen(name='Chemistry')
        
        
        self.clear_info = 0
        self.text = ''
        self.y = 100

        self.btn_home = Button(text='Home', on_press=self.to_home_screen)
        
        
        self.build_screens()

    def on_key_down(self, keycode, modifiers):
        if keycode[1] == 'escape':
            self.to_home_screen()
        
    def build(self, *arg):
        
        self.screen_manager.add_widget(self.home_screen)
        self.screen_manager.add_widget(self.algebra_screen)
        self.screen_manager.add_widget(self.geometry_screen)
        self.screen_manager.add_widget(self.physics_screen)
        self.screen_manager.add_widget(self.chemistry_screen)
        self.main_screen.add_widget(self.screen_manager)
        self.main_screen.add_widget(self.navigation_drawer)

        return self.main_screen

    def build_screens(self, *args):
        home_page = Home(self.screen_manager)

        self.home_screen.add_widget(home_page)
        
        algebra_page = Algebra()

        algebra_page.add_widget(
        ToScreenButton(on_press=self.to_home_screen))
        self.algebra_screen.add_widget(algebra_page)
        
        geometry_page = Geometry()

        geometry_page.add_widget( Button(text='Home', on_press=self.to_home_screen))
        self.geometry_screen.add_widget(geometry_page)
        
        physics_page = Physics()
        
        physics_page.add_widget( Button(text='Home', on_press=self.to_home_screen))
        self.physics_screen.add_widget(physics_page)
        
        chemistry_page = Chemistry()
       
        chemistry_page.add_widget(Button(text='Home', on_press=self.to_home_screen))
        self.chemistry_screen.add_widget(chemistry_page)
        
    def to_home_screen(self, *args):
         self.screen_manager.current = 'Home'

if __name__ == '__main__':
    HelpOnApp().run()