from kivymd.uix.button import MDTextButton, MDRectangleFlatIconButton as NavigationButton, MDRoundFlatIconButton

class ToHomeButton(MDTextButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Home'

class ScreenChangerButton(MDRoundFlatIconButton):
    def __init__(self, screen_manager, text=None, **kwargs):
        super().__init__()
        self.screen_manager = screen_manager
        
        if self.text is None:
            print('Screen with this name not found!')
            exit()
    def on_press(self):
        self.screen_manager.current = self.text

class ToAlgebraButton(ScreenChangerButton):
    icon = 'math-integral'
    text = 'Algebra'

class ToGeometryaButton(ScreenChangerButton):
    icon = 'alpha'
    text = 'Geometry'

class ToPhysicsButton(ScreenChangerButton):
    icon = 'atom'
    text = 'Physics'

class ToChemistryButton(ScreenChangerButton):
    icon = 'microscope'
    text = 'Chemistry'