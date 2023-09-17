from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window

from uix.buttons import TranslationUpdateBehavior
from translation import translate

class TextButton(ButtonBehavior, Label):
    ...

class ScrollViewTitle(ScrollView):
    size_hint=(1, None)
    size=(Window.width, Window.height-200)

class Title(TextButton, TranslationUpdateBehavior):
    def __init__(self, en=None, fr=None, ru=None, hy=None, children_labels_list=[], title_size_hint=1, **kwargs):
        super().__init__(**kwargs)
        self.children_labels_list = children_labels_list
        self.title_size_hint = title_size_hint
        self.color = (1, 1, 1, 1)
        self.font_size += 10
        self.pos_hint = {"center_x": .5}
        self.text_size = [500, None]
        self.halign = 'center'
        print(self.size)

        self.toggle = False
        self.en, self.fr, self.ru, self.hy = en, fr, ru, hy
        if en is not None:
                self.text = translate(self.en, self.fr, self.ru, self.hy, self)
        print(self.size)
    def on_release(self):
        self.toggle = not self.toggle
        
        if self.toggle:
            for i in self.children_labels_list:
                self.parent.add_widget(i)
                self.parent.size_hint_y = self.title_size_hint
        else:
            for i in self.children_labels_list:
                self.parent.remove_widget(i)
                self.parent.size_hint_y = 1
class Label(Label, TranslationUpdateBehavior):
    def __init__(self, en=None, fr=None, ru=None, hy=None, **kwargs):
        super().__init__(**kwargs)
        self.en, self.fr, self.ru, self.hy = en, fr, ru, hy

        if en is not None:
            self.text = translate(self.en, self.fr, self.ru, self.hy, self)

class ChemistryLabel(TextButton, TranslationUpdateBehavior):
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

        self.fr = self.another_language_analogue('Charge', 'Électronégativité', 'n\'a pas', 'Type' , 'Métal', 'métalloïde', 'non-métal')
        self.ru = self.another_language_analogue('Заряд', 'Электроотрицательность', 'не имеет', 'Тип', 'металл', 'металлоид', 'неметалл')
        self.hy = self.another_language_analogue('Լիցք', 'Էլեկտրաբացասականություն', 'չունի', 'Տեսակ', 'մետաղ', 'մետաղանման', 'ոչմետաղ')

        self.text = translate(self.en, self.fr, self.ru, self.hy, self)

    def another_language_analogue(self, element_charge, element_elneg, none, element_type, metal, metalloid, nonmetal):
        return self.en.replace('Charge', element_charge).replace('Electronegativity', element_elneg).replace('does\'nt have', none).replace('Type', element_type).replace('metalloid', metalloid).replace('nonmetal', nonmetal).replace('metal', metal)
    def animation_label(self):
        pass