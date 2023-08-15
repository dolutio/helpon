from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer as NavigationDrawer, MDNavigationLayout as NavigationLayout

class NavigationDrawerContent(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        
        # self.feedback_btn = NavigationButton(
        #             icon="github")
        
        # self.add_widget(self.feedback_btn)