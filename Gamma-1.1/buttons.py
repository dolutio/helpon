from kivymd.uix.button import MDTextButton, MDRectangleFlatIconButton

from translation import translate

class TranslationUpdateBehavior:
    def text_update(self):
        self.text = translate(self.en, self.fr, self.ru, self.hy, self)

class NavigationButton(MDRectangleFlatIconButton, TranslationUpdateBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon_color = (1, 1, 1, 1)
        self.line_color = (0, 0, 0, 0)
        self.text_color = (1, 1, 1, 1)
        self.font_size += 7.5
        
        
class ScreenChangerButton(MDRectangleFlatIconButton, TranslationUpdateBehavior):
    def __init__(self, screen_manager, screen_name=None, **kwargs):
        super().__init__()
        self.icon_color = (1, 1, 1, 1)
        self.line_color = (0, 0, 0, 0)
        self.text_color = (1, 1, 1, 1)
        self.pos_hint = {'center_x': .5}
        self.size_hint_y = .25
        self.font_size += 15
        self.screen_manager = screen_manager
        self.screen_name = screen_name
        
        if self.text is None:
            print('Screen with this name not found!')
            exit()
    def on_release(self):
        self.screen_manager.current = self.screen_name
class ChemistryLabel(MDTextButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (1, 1, 1, 1)
        self.pos_hint = {'right': 0}
    def animation_label(self):
        pass

class ToHomeButton(MDRectangleFlatIconButton, TranslationUpdateBehavior):
    icon = 'home'
    icon_color = (1, 1, 1, 1)
    line_color = (0, 0, 0, 0)
    text_color = (1, 1, 1, 1)
    pos_hint = {'center_x': .5, 'bottom': 0}
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.en, self.fr, self.ru, self.hy = 'Home', 'Maison', 'Главная', 'Գլխավոր'
        self.text = translate(self.en, self.fr, self.ru, self.hy, self)
        self.font_size += 15


class ToAlgebraButton(ScreenChangerButton, TranslationUpdateBehavior):
    icon = 'math-integral'
    
    def __init__(self, screen_manager, screen_name=None, **kwargs):
        super().__init__(screen_manager, screen_name, **kwargs)
        self.en, self.fr, self.ru, self.hy = 'Algebra', 'Algèbre', 'Алгебра', 'Հանրահաշիվ'
        self.text = translate(self.en, self.fr, self.ru, self.hy, self)
        self.screen_name = 'Algebra'

class ToGeometryaButton(ScreenChangerButton, TranslationUpdateBehavior):
    icon = 'alpha'

    def __init__(self, screen_manager, screen_name=None, **kwargs):
        super().__init__(screen_manager, screen_name, **kwargs)
        self.en, self.fr, self.ru, self.hy = 'Geometry', 'Géométrie', 'Геометрия', 'Երկրաչափություն'
        self.text = translate(self.en, self.fr, self.ru, self.hy, self)
        self.screen_name = 'Geometry'

class ToPhysicsButton(ScreenChangerButton, TranslationUpdateBehavior):
    icon = 'atom'

    def __init__(self, screen_manager, screen_name=None, **kwargs):
        super().__init__(screen_manager, screen_name, **kwargs)
        self.en, self.fr, self.ru, self.hy = 'Physics', 'Physique', 'Физика', 'Ֆիզիկա'
        self.text = translate(self.en, self.fr, self.ru, self.hy, self)
        self.screen_name = 'Physics'

class ToChemistryButton(ScreenChangerButton, TranslationUpdateBehavior):
    icon = 'flask'

    def __init__(self, screen_manager, screen_name=None, **kwargs):
        super().__init__(screen_manager, screen_name, **kwargs)
        self.en, self.fr, self.ru, self.hy = 'Chemistry', 'Chimie', 'Химия', 'Քիմիա'
        self.text = translate(self.en, self.fr, self.ru, self.hy, self)
        self.screen_name = 'Chemistry'

class FeedBackButton(NavigationButton, TranslationUpdateBehavior):
    icon = "account"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.en, self.fr, self.ru, self.hy = 'FeedBack', 'Rétroaction', 'Обратная связь', 'Հետադարձ կապ'
        self.text = translate(self.en, self.fr, self.ru, self.hy, self)

class LanguageButton(NavigationButton, TranslationUpdateBehavior):
    icon = 'earth'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.en, self.fr, self.ru, self.hy = 'Language', 'Langue', 'Язык', 'Լեզու'
        self.text = translate(self.en, self.fr, self.ru, self.hy, self)