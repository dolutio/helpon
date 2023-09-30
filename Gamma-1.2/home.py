from kivy.uix.boxlayout import BoxLayout

from uix.buttons import ToAlgebraButton, ToGeometryaButton, ToPhysicsButton, ToChemistryButton

class Home(BoxLayout):
    orientation = 'vertical'
    
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        
        self.screen_manager = screen_manager

        self.add_widget(ToAlgebraButton(screen_manager=screen_manager))
        self.add_widget(ToGeometryaButton(screen_manager=screen_manager))
        self.add_widget(ToPhysicsButton(screen_manager=screen_manager))
        self.add_widget(ToChemistryButton(screen_manager=screen_manager))