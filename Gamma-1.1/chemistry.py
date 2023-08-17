from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.core.window import Window

class Chemistry(BoxLayout):
    orientation = 'vertical'
    def __init__(self):
         super().__init__()
         self.reading_elements_info()
    def reading_elements_info(self, *args):
        self.element_enter = TextInput(hint_text='Enter element name')
        self.read_el_info = Button(text='Read', size_hint =(.2, 1), on_press=self.el)
        self.element_box = BoxLayout()
        self.element_box.add_widget(self.element_enter)
        self.element_box.add_widget(self.read_el_info)
        self.reply = Label(text='')
        self.add_widget(self.element_box)
        layout = GridLayout(cols=1, spacing=10, size_hint_y=.5)
        layout.bind(minimum_height=layout.setter('height'))
        layout.add_widget(self.reply)
        screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-200))
        screen.add_widget(layout)
        self.add_widget(screen)
        

    def el(self, *arg):
        self.get_element = self.element_enter.text
        element_base = {'H': [1, 2.20, 1, 'nonmetal'],
                        'He': [2, 'none', 4, 'nonmetal'],
                        'Li': [3, 0.98, 7, 'metal'],
                        'Be': [4, 1.57, 9, 'metal'],
                        'B': [5, 2.04, 10, 'metalloid'],
                        'C': [6, 2.55, 12, 'nonmetal'],
                        'N': [7, 3.04,14, 'nonmetal'],
                        'O': [8, 3.44, 16, 'nonmetal'],
                        'F': [9, 3.98, 19, 'nonmetal'],
                        'Ne': [10, 'none', 20, 'nonmetal'],
                        'Na': [11, 0.93, 23, 'metal'],
                        'Mg': [12, 1.31, 24, 'metal'],
                        'Al': [13, 1.61, 27, 'metal'],
                        'Si': [14, 1.90, 28, 'metalloid'],
                        'P': [15, 2.19, 28, 'nonmetal'],
                        'S': [16, 2.58, 32, 'nonmetal'],
                        'Cl': [17, 3.16, 35.5, 'nonmetal'],
                        'Ar': [18, 'none', 40, 'nonmetal'],
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
                        'As': [33, 2.18, 75, 'meta-like'],
                        'Se': [34, 2.55, 79, 'nonmetal'],
                        'Br': [35, 2.96, 80, 'nonmetal'],
                        'Kr': [36, 'none', 84, 'nonmetal'],
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
        if self.get_element ==  'H':
            self.reply.text += '\n                 H\nprotons: 1\nelectrons: 1\nelectronegativity: 2.20\nmass: 1\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'He':
            self.reply.text += '\n                He\nprotons: 2\nelectrons: 2\nelectronegativity: none\nmass: 4\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Li':
            self.reply.text += '\n                Li\nprotons: 3\nelectrons: 3\nelectronegativity: 0.98\nmass: 7\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Be':
            self.reply.text += '\n                Be\nprotons: 4\nelectrons: 4\nelectronegativity: 1.57\nmass: 9\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'B':
            self.reply.text += '\n                 B\nprotons: 5\nelectrons: 5\nelectronegativity: 2.04\nmass: 10\ntype: metalloid\n'
            self.element_enter.text = ''
        elif self.get_element == 'C':
            self.reply.text += '\n                 C\nprotons: 6\nelectrons: 6\nelectronegativity: 2.55\nmass: 12\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'N':
            self.reply.text += '\n                 N\nprotons: 7\nelectrons: 7\nelectronegativity: 3.04\nmass: 14\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'O':
            self.reply.text += '\n                 O\nprotons: 8\nelectrons: 8\nelectronegativity: 3.44\nmass: 16\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'F':
            self.reply.text += '\n                 F\nprotons: 9\nelectrons: 9\nelectronegativity: 3.98\nmass: 19\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Ne':
            self.reply.text += '\n                Ne\nprotons: 10\nelectrons: 10\nelectronegativity: none\nmass: 20\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Na':
            self.reply.text += '\n                Na\nprotons: 11\nelectrons: 11\nelectronegativity: 0.93\nmass: 23\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Mg':
            self.reply.text += '\n                Mg\nprotons: 12\nelectrons: 12\nelectronegativity: 1.31\nmass: 24\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Al':
            self.reply.text += '\n                Al\nprotons: 13\nelectrons: 13\nelectronegativity: 1.61\nmass: 27\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Si':
            self.reply.text += '\n                Si\nprotons: 14\nelectrons: 14\nelectronegativity: 1.90\nmass: 28\ntype: metalloid\n'
            self.element_enter.text = ''
        elif self.get_element == 'P':
            self.reply.text += '\n                 P\nprotons: 15\nelectrons: 15\nelectronegativity: 2.19\nmass: 31\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'S':
            self.reply.text += '\n                 S\nprotons: 16\nelectrons: 16\nelectronegativity: 2.58\nmass: 32\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Cl':
            self.reply.text += '\n                Cl\nprotons: 17\nelectrons: 17\nelectronegativity: 3.16\nmass: 35.5\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Ar':
            self.reply.text += '\n                Ar\nprotons: 18\nelectrons: 18\nelectronegativity: none\nmass: 40\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'K':
            self.reply.text += '\n                 K\nprotons: 19\nelectrons: 19\nelectronegativity: 0.82\nmass: 39\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Ca':
            self.reply.text += '\n                Ca\nprotons: 20\nelectrons: 20\nelectronegativity: 1.00\nmass: 40\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Sc':
            self.reply.text += '\n                Sc\nprotons: 21\nelectrons: 21\nelectronegativity: 1.36\nmass: 45\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Ti':
            self.reply.text += '\n                Ti\nprotons: 22\nelectrons: 22\nelectronegativity: 1.54\nmass: 48\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'V':
            self.reply.text += '\n                 V\nprotons: 23\nelectrons: 23\nelectronegativity: 1.63\nmass: 51\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Cr':
            self.reply.text += '\n                Cr\nprotons: 24\nelectrons: 24\nelectronegativity: 1.66\nmass: 52\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Mn':
            self.reply.text += '\n                Mn\protons: 25\nelectrons: 25\nelectronegativity: 1.55\nmass: 55\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Fe':
            self.reply.text += '\n                Fe\nprotons: 26\nelectrons: 26\nelectronegativity: 1.83\nmass: 56\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Co':
            self.reply.text += '\n                Co\nprotons: 27\nelectrons: 27\nelectronegativity: 1.88\nmass: 59\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Ni':
            self.reply.text += '\n                Ni\nprotons: 28\nelectrons: 28\nelectronegativity: 1.91\nmass: 59\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Cu':
            self.reply.text += '\n                Cu\nprotons: 29\nelectrons: 29\nelectronegativity: 1.90\nmass: 64\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Zn':
            self.reply.text += '\n                Zn\nprotons: 30\nelectrons: 30\nelectronegativity: 1.65\nmass: 65\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Ga':
            self.reply.text += '\n                Ga\nprotons: 31\nelectrons: 31\nelectronegativity: 1.81\nmass: 70\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Ge':
            self.reply.text += '\n                Ge\nprotons: 32\nelectrons: 32\nelectronegativity: 2.01\nmass: 73\ntype: metalloid\n'
            self.element_enter.text = ''
        elif self.get_element == 'As':
            self.reply.text += '\n                As\nprotons: 33\nelectrons: 33\nelectronegativity: 2.18\nmass: 75\ntype: metalloid\n'
            self.element_enter.text = ''
        elif self.get_element == 'Se':
            self.reply.text += '\n                Se\nprotons: 34\nelectrons: 34\nelectronegativity: 2.55\nmass: 79\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Br':
            self.reply.text += '\n                Br\nprotons: 35\nelectrons: 35\nelectronegativity: 2.96\nmass: 80\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Kr':
            self.reply.text += '\n                Kr\nprotons: 36\nelectrons: 36\nelectronegativity: none\nmass: 84\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Rb':#                                        START
            self.reply.text += '\n                Rb\nprotons: 37\nelectrons: 37\n electronegativity: 0.82\nmass: 85\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Sr':
            self.reply.text += '\n                Sr\nprotons: 38\nelectrons: 38\n electronegativity: 0.95\nmass: 88\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Y':
            self.reply.text += '\n                 Y\nprotons: 39\nelectrons: 39\n electronegativity: 1.22\nmass: 89\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Zr':
            self.reply.text += '\n                Zr\nprotons: 40\nelectrons: 40\n electronegativity: 1.33\nmass: 91\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Nb':
            self.reply.text += '\n                Nb\nprotons: 41\nelectrons: 41\n electronegativity: 1.60\nmass: 93\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Mo':
            self.reply.text += '\n                Mo\nprotons: 42\nelectrons: 42\n electronegativity: 2.16\nmass: 96\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Tc':
            self.reply.text += '\n                Zr\nprotons: 43\nelectrons: 43\n electronegativity: 2.10\nmass: 98\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Ru':
            self.reply.text += '\n                Ru\nprotons: 44\nelectrons: 44\n electronegativity: 2.20\nmass: 101\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Rh':
            self.reply.text += '\n                Rh\nprotons: 45\nelectrons: 45\n electronegativity: 2.28\nmass: 103\ntype: metal\n'
            self.element_enter.text = ''
        elif self.get_element == 'Pd':
            self.reply.text += '\n                Pd\nprotons: 46\nelectrons: 46\nelectronegativity: 2.20\nmass: 106\ntype: metal\n'
            self.element_enter.text = ''
        else:
            if  not self.get_element:
                self.element_enter.text = 'Enter element name!'
            else:
                self.element_enter.text = 'This element not found'