from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.core.window import Window

from home import Home
from algebra import Algebra
from geometry import Geometry
from physics import Physics
from chemistry import Chemistry
from navigationtools import NavigationLayout, NavigationDrawer, NavigationDrawerContent
from buttons import ToHomeButton

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


  





class HelpOnApp(MDApp):
    icon = 'HelpOn.png'
    def __init__(self):
        super().__init__()
        self.theme_cls.colors |= colors

        self.main_screen = NavigationLayout()

        self.navigation_drawer = NavigationDrawer()
        self.navigation_drawer.add_widget(NavigationDrawerContent())

        self.screen_manager = ScreenManager(transition=NoTransition())
        self.home_screen = Screen(name="Home")
        self.algebra_screen = Screen(name='Algebra')
        self.geometry_screen = Screen(name='Geometry')
        self.physics_screen = Screen(name='Physics')
        self.chemistry_screen = Screen(name='Chemistry')
        
        Window.bind(on_keyboard=self.on_key_down)
        self.build_screens()
    def on_key_down(self, window, keycode, *args):
        if keycode in [27, 1001]:
            self.to_home_screen()
            return True
        
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

        algebra_page.add_widget(ToHomeButton(on_release=self.to_home_screen))
        self.algebra_screen.add_widget(algebra_page)
        
        geometry_page = Geometry()

        geometry_page.add_widget(ToHomeButton(on_release=self.to_home_screen))
        self.geometry_screen.add_widget(geometry_page)
        
        physics_page = Physics()
        
        physics_page.add_widget(ToHomeButton(on_release=self.to_home_screen))
        self.physics_screen.add_widget(physics_page)
        
        chemistry_page = Chemistry()
       
        chemistry_page.add_widget(ToHomeButton(on_release=self.to_home_screen))
        self.chemistry_screen.add_widget(chemistry_page)
        
    def to_home_screen(self, *args):
        self.screen_manager.current = 'Home'

if __name__ == '__main__':
    HelpOnApp().run()