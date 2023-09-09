from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.uix.button import MDTextButton

from kivy.core.window import Window

from uix.labels import ChemistryLabel

class Chemistry(BoxLayout):
    orientation = 'vertical'
    def __init__(self):
        super().__init__()
        self.index = 0
        self.reading_elements_info()

    def reading_elements_info(self, *args):
        self.element_enter = TextInput(hint_text='Enter element name', size_hint_y=.25, pos_hint={'top': 1})
        self.read_el_info = Button(text='Read', size_hint=(.2, .25), pos_hint={'top': 1}, on_press=self.get_element_info)
        self.element_box = BoxLayout()
        self.element_box.add_widget(self.element_enter)
        self.element_box.add_widget(self.read_el_info)
        self.add_widget(self.element_box)

        self.reply_layout_parent = None
        self.reply_layout = DropDown(size_hint=(1, 1))

        screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-200))
        screen.add_widget(self.reply_layout)
        self.add_widget(screen)

    def get_element_info(self, *arg):
        self.get_element = self.element_enter.text

        element_base = {'H': [1, 2.20, 1, 'nonmetal'],
                        'He': [2, 'does\'nt have', 4, 'nonmetal'],
                        'Li': [3, 0.98, 7, 'metal'],
                        'Be': [4, 1.57, 9, 'metal'],
                        'B': [5, 2.04, 10, 'metalloid'],
                        'C': [6, 2.55, 12, 'nonmetal'],
                        'N': [7, 3.04,14, 'nonmetal'],
                        'O': [8, 3.44, 16, 'nonmetal'],
                        'F': [9, 3.98, 19, 'nonmetal'],
                        'Ne': [10, 'does\'nt have', 20, 'nonmetal'],
                        'Na': [11, 0.93, 23, 'metal'],
                        'Mg': [12, 1.31, 24, 'metal'],
                        'Al': [13, 1.61, 27, 'metal'],
                        'Si': [14, 1.90, 28, 'metalloid'],
                        'P': [15, 2.19, 28, 'nonmetal'],
                        'S': [16, 2.58, 32, 'nonmetal'],
                        'Cl': [17, 3.16, 35.5, 'nonmetal'],
                        'Ar': [18, 'does\'nt have', 40, 'nonmetal'],
                        'K': [19, 0.82, 39, 'metal'],
                        'Ca': [20, 1, 40, 'metal'],
                        'Sc': [21, 1.36, 45, 'metal'],
                        'Ti': [22, 1.54, 48, 'metal'],
                        'V': [23, 1.63, 51, 'metal'],
                        'Cr': [24, 1.66, 52, 'metal'],
                        'Mn': [25, 1.55, 55, 'metal'],
                        'Fe': [26, 1.83, 56, 'metal'],
                        'Co': [27, 1.88, 59, 'metal'],
                        'Ni': [28, 1.91, 59, 'metal'],
                        'Cu': [29, 1.90, 64, 'metal'],
                        'Zn': [30, 1.65, 65, 'metal'],
                        'Ga': [31, 1.81, 70, 'metal'],
                        'Ge': [32, 2.01, 73, 'metalloid'],
                        'As': [33, 2.18, 75, 'metalloid'],
                        'Se': [34, 2.55, 79, 'nonmetal'],
                        'Br': [35, 2.96, 80, 'nonmetal'],
                        'Kr': [36, 'does\'nt have', 84, 'nonmetal'],
                        'Rb': [37, 0.82, 85, 'nonmetal'],
                        'Sr': [38, 0.95, 88, 'metal'],
                        'Y': [39, 1.22, 89, 'metal'],
                        'Tc': [40, 1.9, 91, 'metal'],
                        'Nb': [41, 1.60, 93, 'metal'],
                        'Mo': [42, 2.16, 96, 'metal'],
                        'Zr': [43, 2.10, 98, 'metal'],
                        'Ru': [43, 2.20, 101, 'metal'],
                        'Rh': [45, 2.28, 103, 'metal'],
                        'Pd': [46, 2.20, 106, 'metal']}

        element_charge = element_base[self.get_element][0]
        element_electronegativity = element_base[self.get_element][1]
        element_Ar = element_base[self.get_element][2]
        element_type = element_base[self.get_element][3]
 
        self.reply_layout.add_widget(ChemistryLabel(self.get_element, element_charge, element_electronegativity, element_Ar, element_type), index=10)
        self.index += 1