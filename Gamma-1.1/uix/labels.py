from kivymd.uix.button import MDTextButton
from kivy.uix.label import Label
from uix.buttons import TranslationUpdateBehavior
from translation import translate

class Label(Label, TranslationUpdateBehavior):
    def __init__(self, en=None, fr=None, ru=None, hy=None, **kwargs):
        super().__init__(**kwargs)
        self.en, self.fr, self.ru, self.hy = en, fr, ru, hy
        if en is not None:
            self.text = translate(self.en, self.fr, self.ru, self.hy, self)

class ChemistryLabel(MDTextButton, TranslationUpdateBehavior):
    def __init__(self, element_name, element_charge, element_electronegativity, element_Ar, element_type, **kwargs):
        super().__init__(**kwargs)
        self.color = (1, 1, 1, 1)
        self.pos_hint = {'right': 0}

        self.en = f'''
                                {element_name}
                Charge: {element_charge}
                Electronegativity: {element_electronegativity}
                Ar: {element_Ar}
                Type: {element_type}
                        '''
        self.fr = self.en

        self.ru = self.another_language_analogue('Заряд', 'Электроотрицательность', 'Тип')
        self.hy = self.another_language_analogue('Լիցք', 'Էլեկտրաբացասականություն', 'Տեսակ')

        self.text = translate(self.en, self.fr, self.ru, self.hy, self)

    def another_language_analogue(self, element_charge, element_elneg, element_type):
        return self.en.replace('Charge', element_charge).replace('Electronegativity', element_elneg).replace('Type', element_type)
    def animation_label(self):
        pass