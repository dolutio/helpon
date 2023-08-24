from kivymd.uix.button import MDTextButton, MDRectangleFlatIconButton

class NavigationButton(MDRectangleFlatIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon_color = (1, 1, 1, 1)
        self.line_color = (0, 0, 0, 0)
        self.text_color = (1, 1, 1, 1)
        self.font_size += 7.5
        
        
class ScreenChangerButton(MDRectangleFlatIconButton):
    def __init__(self, screen_manager, text=None, **kwargs):
        super().__init__()
        self.icon_color = (1, 1, 1, 1)
        self.line_color = (0, 0, 0, 0)
        self.text_color = (1, 1, 1, 1)
        self.pos_hint = {'center_x': .5}
        self.size_hint_y = .25
        self.font_size += 15
        self.screen_manager = screen_manager
        
        if self.text is None:
            print('Screen with this name not found!')
            exit()
    def on_release(self):
        self.screen_manager.current = self.text
class ChemistryLabel(MDTextButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (1, 1, 1, 1)
        self.size_hint = (1, None)
        self.pos_hint = {'right': 0}

class ToHomeButton(MDRectangleFlatIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon = 'home'
        self.text = 'Home'
        self.icon_color = (1, 1, 1, 1)
        self.line_color = (0, 0, 0, 0)
        self.text_color = (1, 1, 1, 1)
        self.pos_hint = {'center_x': .5, 'bottom': 0}
        self.font_size += 15

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
    icon = 'flask'
    text = 'Chemistry'