from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (0/255, 150/255, 150/255, 1)

class HelpOnApp(App):
    def __init__(self):
        super().__init__()
        self.icon = 'HelpOn.png'
        self.clear_info = 0
        self.text = ''
        self.y = 100

        self.btna = Button(text='Algebra', on_press=self.algebra)
        self.btng = Button(text='Geometry', on_press=self.geometry)
        self.btnph = Button(text='Physics', on_press=self.ph)
        self.btnch = Button(text='Chemistry', on_press=self.ch)
        self.btn_home = Button(text='Home', on_press=self.home)
        self.b = BoxLayout(orientation='vertical')

    def build(self, *arg):
        if self.clear_info:
            self.b.clear_widgets()
        self.b.add_widget(self.btna)
        self.b.add_widget(self.btng)
        self.b.add_widget(self.btnph)
        self.b.add_widget(self.btnch)

        return self.b

    def algebra(self, *arg):
        self.b.remove_widget(self.btna)
        self.b.remove_widget(self.btng)
        self.b.remove_widget(self.btnph)
        self.b.remove_widget(self.btnch)

        alg_grand_title = Label(text='Algebra')
        alg_grand_title.font_size += 15
        
        layout = GridLayout(cols=1, spacing=10, size_hint_y=4)
        layout.bind(minimum_height=layout.setter('height'))

        layout.add_widget(alg_grand_title)

        abb_multi_formula = Label(text='Abbreviated multiplication formula')
        abb_multi_formula.font_size += 10
        layout.add_widget(abb_multi_formula)

        apb2 = Label(text=' (a+b)² = a² + 2ab + b²', halign='left', valign='middle')
        layout.add_widget(apb2)

        amb2 = Label(text=' (a-b)² = a² - 2ab + b²', halign='left', valign='middle')
        layout.add_widget(amb2)

        a2mb2 = Label(text=' (a-b)(a+b) = a² - b²', halign='left', valign='middle')
        layout.add_widget(a2mb2)

        

        a3pb3 = Label(text=' (a+b)(a²-ab+b²) = a³ + b³')
        layout.add_widget(a3pb3)

        a3mb3= Label(text=' (a-b)(a²+ab+b²) = a³ - b³')
        layout.add_widget(a3mb3)

        apb3 = Label(text='(a+b)³ = a³ + 3a²b + 3ab² + b³')
        layout.add_widget(apb3)

        amb3 = Label(text='(a - b)³ = a³ - 3a²b + 3ab² - b³')
        layout.add_widget(amb3)

        discriminant = Label(text='Discriminant')
        discriminant.font_size += 10
        layout.add_widget(discriminant)

        discformul = Label(text='D = b² - 4ac')
        layout.add_widget(discformul)
        quadrequation = Label(text='Quadratic equation')
        quadrequation.font_size += 10
        layout.add_widget(quadrequation)

        x1form = Label(text='x1 = (-b - √D) / 2a')
        x2form = Label(text='x2 = (-b + √D) / 2a')
        layout.add_widget(x1form)
        layout.add_widget(x2form)
        discinfo = Label(text='(D is discriminant)')
        layout.add_widget(discinfo)



        vtheorem = Label(text='Viette\'s Theorem')
        vtheorem.font_size += 5
        layout.add_widget(vtheorem)

        x1px2 = Label(text='x1 + x2 = -b')
        layout.add_widget(x1px2)
        x1x2 = Label(text='x1 * x2 = c')
        layout.add_widget(x1x2)

        
        q_e_w_a_e_s_c = Label(text='Quadratic equation with an even second coefficient')
        q_e_w_a_e_s_c.font_size += 5
        layout.add_widget(q_e_w_a_e_s_c)
        
        quad_example_1 = Label(text='D = k² - ac')
        layout.add_widget(quad_example_1)

        quad_example_2 = Label(text='x1 = (-k - √D) / a')
        layout.add_widget(quad_example_2)

        quad_example_3 = Label(text='x2 = (-k + √D) / a')
        layout.add_widget(quad_example_3)
        
        
        probability_title = Label(text='Formula for finding probability')
        probability_title.font_size += 10
        layout.add_widget(probability_title)

        probability_example = Label(text='P = m / n')
        layout.add_widget(probability_example)

        probability_m = Label(text='m is the desired result in theory')
        layout.add_widget(probability_m)

        probability_n = Label(text='n is the total result')
        layout.add_widget(probability_n)

        frequency_title = Label(text='Formula for finding frequency')
        frequency_title.font_size += 10
        layout.add_widget(frequency_title)

        frequency_example = Label(text='W = m / n')
        layout.add_widget(frequency_example)

        frequency_m = Label(text='m is desired result')
        layout.add_widget(frequency_m)

        frequency_n = Label(text='n is the number of times we repeated the experiment')
        layout.add_widget(frequency_n)

        two_unknowns_equation_title = Label(text='Equation with two unknowns')
        two_unknowns_equation_title.font_size += 10
        layout.add_widget(two_unknowns_equation_title)

        layout.add_widget(Widget())

        two_unknowns_equation_1 = BoxLayout(orientation='vertical')

        two_un_example = Label(text='x + y = 10\n5x + 3y = 42')
        two_unknowns_equation_1.add_widget(two_un_example)
        layout.add_widget(two_unknowns_equation_1)

        layout.add_widget(Widget())
        layout.add_widget(Widget())


        two_unknowns_equation_2 = BoxLayout(orientation='vertical')

        two_unknowns_equation_2.add_widget(Label(text='5x + 5y = 50\n[size=40]-[/size]\n5x + 3y = 42', markup=1))
        layout.add_widget(two_unknowns_equation_2)

        layout.add_widget(Widget())

        two_unknowns_equation_3 = Label(text='0 * x + 2y = 8')
        layout.add_widget(two_unknowns_equation_3)

        two_unknowns_equation_4 = Label(text='2y = 8')
        layout.add_widget(two_unknowns_equation_4)

        two_unknowns_equation_5 = Label(text='y = 4')
        layout.add_widget(two_unknowns_equation_5)







        screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-self.y))
        screen.add_widget(layout)
        self.b.add_widget(screen)
        self.b.add_widget(self.btn_home)

    def geometry(self, *arg):
        self.b.remove_widget(self.btna)
        self.b.remove_widget(self.btng)
        self.b.remove_widget(self.btnph)
        self.b.remove_widget(self.btnch) 

        layout = GridLayout(cols=1, spacing=10, size_hint_y=1.5)
        layout.bind(minimum_height=layout.setter('height'))
        #tang, cotang, sin2+cos2, sin90-x, cos90-x, sin180-x, cos180-x, Pifagor
        self.trig = BoxLayout()
        self.sin = BoxLayout(orientation='vertical')
        self.cos = BoxLayout(orientation='vertical')

        geometry_title = Label(text='Geometry')
        geometry_title.font_size += 20
        layout.add_widget(geometry_title)

        triglabel = Label(text='Trigonometry', font_size=30)
        layout.add_widget(triglabel)

        tang_formul = Label(text='tang(α) = sin(α) / cos(α)')
        layout.add_widget(tang_formul)

        cotang_formul = Label(text='cotang(α) = cos(α) / sin(α)')
        layout.add_widget(cotang_formul)

        sin90mx = Label(text='sin(90 - α) = cos(α)')
        layout.add_widget(sin90mx)
        cos90mx = Label(text='cos(90 - α) = sin(α)')
        layout.add_widget(cos90mx)
        tang90mx = Label(text='tang(90 - α) = cotang(α)')
        layout.add_widget(tang90mx)
        cotang90mx = Label(text='cotang(90 - α) = tang(α)')
        layout.add_widget(cotang90mx)
        sin180mx = Label(text='sin(180 - α) = sin(α)')
        layout.add_widget(sin180mx)
        cos180mx = Label(text='cos(180 - α) = -cos(α)')
        layout.add_widget(cos180mx)
        tang180mx = Label(text='tang(180 - α) = -cotang(α)')
        layout.add_widget(tang180mx)
        cotang180mx = Label(text='cotang(180 - α) = -tang(α)')
        layout.add_widget(cotang180mx)


        sin2x_plus_cos2x = Label(text='sin²(α) + cos²(α) = 1')
        layout.add_widget(sin2x_plus_cos2x)

        tangcotangformul = Label(text='tang(α) * cotang(α) = 1')
        layout.add_widget(tangcotangformul)


        sin_theorem_label = Label(text='Law of sines', font_size=30)
        layout.add_widget(sin_theorem_label)

        sin_theorem_formul = Label(text='a/sin(α) = b/sin(β) = c/sin(γ)')
        layout.add_widget(sin_theorem_formul)

        cos_theorem_label = Label(text='Law of cosines', font_size=30)
        layout.add_widget(cos_theorem_label)

        cos_theorem_formul = Label(text='a² = b² + c² - 2bc*cos(α)')
        layout.add_widget(cos_theorem_formul)

        pyt_theorem_label = Label(text='Pythagorean theorem', font_size=30)
        layout.add_widget(pyt_theorem_label)

        pyt_theorem_formul = Label(text='a² + b² = c²')
        layout.add_widget(pyt_theorem_formul)





        screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-self.y))
        screen.add_widget(layout)
        self.b.add_widget(screen)
        self.b.add_widget(self.btn_home)
    def ph(self, *arg):
        self.b.remove_widget(self.btna)
        self.b.remove_widget(self.btng)
        self.b.remove_widget(self.btnph)
        self.b.remove_widget(self.btnch)
        
        layout = GridLayout(cols=1, spacing=10, size_hint_y=2)
        layout.bind(minimum_height=layout.setter('height'))

        layout.add_widget(Widget())        
        ph_grand_title = Label(text='Physics', font_size=40)
        layout.add_widget(ph_grand_title)

        layout.add_widget(Widget())        

        values_title = Label(text='Values', font_size=30)
        layout.add_widget(values_title)

        value_volume = Label(text='V is volume')
        layout.add_widget(value_volume)
        value_speed = Label(text='v is speed')
        layout.add_widget(value_speed)
        value_square = Label(text='S is square')
        layout.add_widget(value_square)
        value_length = Label(text='s is length')
        layout.add_widget(value_length)
        value_height = Label(text='h is height')
        layout.add_widget(value_height)
        value_density = Label(text='ρ is density')
        layout.add_widget(value_density)
        value_time = Label(text='t is time')
        layout.add_widget(value_time)
        value_mass = Label(text='m is mass')
        layout.add_widget(value_mass)
        value_grav = Label(text='g is gravitational constant')        
        layout.add_widget(value_grav)
        value_pressure = Label(text='P is pressure')
        value_force = Label(text='F is force')
        layout.add_widget(value_force)
        value_work =  Label(text='A is work')
        layout.add_widget(value_work)
        value_power = Label(text='N is power')
        layout.add_widget(value_power)

        square_formulas_title = Label(text='Formulas for finding square', font_size=30)
        layout.add_widget(square_formulas_title)


        square_formula_1 = Label(text='S = h²')
        layout.add_widget(square_formula_1)

        square_formula_2 = Label(text='S = V / h')
        layout.add_widget(square_formula_2)

        square_formula_3 = Label(text='S = F / P')
        layout.add_widget(square_formula_3)

        length_formulas_title = Label(text='Formulas for finding length', font_size=30)  
        layout.add_widget(length_formulas_title)      


        length_formula_1 = Label(text='s = vt')
        layout.add_widget(length_formula_1)

        length_formula_2 = Label(text='s = A / F')
        layout.add_widget(length_formula_2)

        time_formulas_title = Label(text='Formulas for finding time', font_size=30)
        layout.add_widget(time_formulas_title)

        time_formula_1 = Label(text='t = s / v')
        layout.add_widget(time_formula_1)

        time_formula_2 = Label(text='t = A / N')
        layout.add_widget(time_formula_2)

        m_formulas_title = Label(text='Formulas for finding mass', font_size=30)
        layout.add_widget(m_formulas_title)

        m_formula_1 = Label(text='1.m = ρV')
        layout.add_widget(m_formula_1)

        m_formula_2 = Label(text='2.m = F / g')
        layout.add_widget(m_formula_2)

        heft_formula_tite = Label(text='Formula for finding heft', font_size=30)
        layout.add_widget(heft_formula_tite)

        heft_formula = Label(text='F = mg')
        layout.add_widget(heft_formula)

        speed_formulas_title = Label(text='Formulas for finding speed', font_size=30)
        layout.add_widget(speed_formulas_title)

        speed_formul_1 = Label(text='v = s / t')
        layout.add_widget(speed_formul_1)

        arch_principle = Label(text='Archimedes principle', font_size=30)
        layout.add_widget(arch_principle)

        arch_principle_example = Label(text='F = ρgV')
        layout.add_widget(arch_principle_example)

        layout.add_widget(Widget())        

        screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-self.y))
        screen.add_widget(layout)
        self.b.add_widget(screen)
        self.b.add_widget(self.btn_home)

    def ch(self, *arg):
        self.b.remove_widget(self.btna)
        self.b.remove_widget(self.btng)
        self.b.remove_widget(self.btnph)
        self.b.remove_widget(self.btnch)

        self.reading_elements_info()

    def reading_elements_info(self, *arg):
        self.b.remove_widget(self.btna)
        self.b.remove_widget(self.btng)
        self.b.remove_widget(self.btnph)
        self.b.remove_widget(self.btnch)
        self.b.remove_widget(self.btn_home)
        
        self.element_enter = TextInput(hint_text='Enter element name')
        self.read_el_info = Button(text='Read', size_hint =(.2, 1), on_press=self.el)
        self.element_box = BoxLayout()
        self.element_box.add_widget(self.element_enter)
        self.element_box.add_widget(self.read_el_info)
        self.reply = Label(text=self.text)
        self.b.add_widget(self.element_box)
        layout = GridLayout(cols=1, spacing=10, size_hint_y=.5)
        layout.bind(minimum_height=layout.setter('height'))
        layout.add_widget(self.reply)
        screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-self.y))
        screen.add_widget(layout)
        self.b.add_widget(screen)
        self.b.add_widget(self.btn_home)

    def el(self, *arg):
        self.element_get = self.element_enter.text
        if self.element_get ==  'H':
            self.reply.text += '\n                 H\nprotons: 1\nelectrons: 1\nelectronegativity: 2.20\nmass: 1\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'He':
            self.reply.text += '\n                He\nprotons: 2\nelectrons: 2\nelectronegativity: none\nmass: 4\ntype: nonmetall\n'
            self.element_enter.text = ''
        elif self.element_get == 'Li':
            self.reply.text += '\n                Li\nprotons: 3\nelectrons: 3\nelectronegativity: 0.98\nmass: 7\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Be':
            self.reply.text += '\n                Be\nprotons: 4\nelectrons: 4\nelectronegativity: 1.57\nmass: 9\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'B':
            self.reply.text += '\n                 B\nprotons: 5\nelectrons: 5\nelectronegativity: 2.04\nmass: 10\ntype: metal-like\n'
            self.element_enter.text = ''
        elif self.element_get == 'C':
            self.reply.text += '\n                 C\nprotons: 6\nelectrons: 6\nelectronegativity: 2.55\nmass: 12\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'N':
            self.reply.text += '\n                 N\nprotons: 7\nelectrons: 7\nelectronegativity: 3.04\nmass: 14\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'O':
            self.reply.text += '\n                 O\nprotons: 8\nelectrons: 8\nelectronegativity: 3.44\nmass: 16\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'F':
            self.reply.text += '\n                 F\nprotons: 9\nelectrons: 9\nelectronegativity: 3.98\nmass: 19\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Ne':
            self.reply.text += '\n                Ne\nprotons: 10\nelectrons: 10\nelectronegativity: none\nmass: 20\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Na':
            self.reply.text += '\n                Na\nprotons: 11\nelectrons: 11\nelectronegativity: 0.93\nmass: 23\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Mg':
            self.reply.text += '\n                Mg\nprotons: 12\nelectrons: 12\nelectronegativity: 1.31\nmass: 24\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Al':
            self.reply.text += '\n                Al\nprotons: 13\nelectrons: 13\nelectronegativity: 1.61\nmass: 27\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Si':
            self.reply.text += '\n                Si\nprotons: 14\nelectrons: 14\nelectronegativity: 1.90\nmass: 28\ntype: metal-like\n'
            self.element_enter.text = ''
        elif self.element_get == 'P':
            self.reply.text += '\n                 P\nprotons: 15\nelectrons: 15\nelectronegativity: 2.19\nmass: 31\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'S':
            self.reply.text += '\n                 S\nprotons: 16\nelectrons: 16\nelectronegativity: 2.58\nmass: 32\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Cl':
            self.reply.text += '\n                Cl\nprotons: 17\nelectrons: 17\nelectronegativity: 3.16\nmass: 35.5\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Ar':
            self.reply.text += '\n                Ar\nprotons: 18\nelectrons: 18\nelectronegativity: none\nmass: 40\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'K':
            self.reply.text += '\n                 K\nprotons: 19\nelectrons: 19\nelectronegativity: 0.82\nmass: 39\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Ca':
            self.reply.text += '\n                Ca\nprotons: 20\nelectrons: 20\nelectronegativity: 1.00\nmass: 40\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Sc':
            self.reply.text += '\n                Sc\nprotons: 21\nelectrons: 21\nelectronegativity: 1.36\nmass: 45\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Ti':
            self.reply.text += '\n                Ti\nprotons: 22\nelectrons: 22\nelectronegativity: 1.54\nmass: 48\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'V':
            self.reply.text += '\n                 V\nprotons: 23\nelectrons: 23\nelectronegativity: 1.63\nmass: 51\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Cr':
            self.reply.text += '\n                Cr\nprotons: 24\nelectrons: 24\nelectronegativity: 1.66\nmass: 52\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Mn':
            self.reply.text += '\n                Mn\nprotons: 25\nelectrons: 25\nelectronegativity: 1.55\nmass: 55\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Fe':
            self.reply.text += '\n                Fe\nprotons: 26\nelectrons: 26\nelectronegativity: 1.83\nmass: 56\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Co':
            self.reply.text += '\n                Co\nprotons: 27\nelectrons: 27\nelectronegativity: 1.88\nmass: 59\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Ni':
            self.reply.text += '\n                Ni\nprotons: 28\nelectrons: 28\nelectronegativity: 1.91\nmass: 59\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Cu':
            self.reply.text += '\n                Cu\nprotons: 29\nelectrons: 29\nelectronegativity: 1.90\nmass: 64\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Zn':
            self.reply.text += '\n                Zn\nprotons: 30\nelectrons: 30\nelectronegativity: 1.65\nmass: 65\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Ga':
            self.reply.text += '\n                Ga\nprotons: 31\nelectrons: 31\nelectronegativity: 1.81\nmass: 70\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Ge':
            self.reply.text += '\n                Ge\nprotons: 32\nelectrons: 32\nelectronegativity: 2.01\nmass: 73\ntype: metal-like\n'
            self.element_enter.text = ''
        elif self.element_get == 'As':
            self.reply.text += '\n                As\nprotons: 33\nelectrons: 33\nelectronegativity: 2.18\nmass: 75\ntype: metal-like\n'
            self.element_enter.text = ''
        elif self.element_get == 'Se':
            self.reply.text += '\n                Se\nprotons: 34\nelectrons: 34\nelectronegativity: 2.55\nmass: 79\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Br':
            self.reply.text += '\n                Br\nprotons: 35\nelectrons: 35\nelectronegativity: 2.96\nmass: 80\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Kr':
            self.reply.text += '\n                Kr\nprotons: 36\nelectrons: 36\nelectronegativity: none\nmass: 84\ntype: nonmetal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Rb':#                                        START
            self.reply.text += '\n                Rb\nprotons: 37\nelectrons: 37\n electronegativity: 0.82\nmass: 85\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Sr':
            self.reply.text += '\n                Sr\nprotons: 38\nelectrons: 38\n electronegativity: 0.95\nmass: 88\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Y':
            self.reply.text += '\n                 Y\nprotons: 39\nelectrons: 39\n electronegativity: 1.22\nmass: 89\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Zr':
            self.reply.text += '\n                Zr\nprotons: 40\nelectrons: 40\n electronegativity: 1.33\nmass: 91\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Nb':
            self.reply.text += '\n                Nb\nprotons: 41\nelectrons: 41\n electronegativity: 1.60\nmass: 93\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Mo':
            self.reply.text += '\n                Mo\nprotons: 42\nelectrons: 42\n electronegativity: 2.16\nmass: 96\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Tc':
            self.reply.text += '\n                Zr\nprotons: 43\nelectrons: 43\n electronegativity: 2.10\nmass: 98\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Ru':
            self.reply.text += '\n                Ru\nprotons: 44\nelectrons: 44\n electronegativity: 2.20\nmass: 101\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Rh':
            self.reply.text += '\n                Rh\nprotons: 45\nelectrons: 45\n electronegativity: 2.28\nmass: 103\ntype: metal\n'
            self.element_enter.text = ''
        elif self.element_get == 'Pd':
            self.reply.text += '\n                Pd\nprotons: 46\nelectrons: 46\n electronegativity: 2.20\nmass: 106\ntype: metal\n'
            self.element_enter.text = ''
        else:
            if  not self.element_get:
                self.element_enter.text = 'Enter element name!'
            else:
                self.element_enter.text = 'This element not found'
        

    def home(self, *args):
        self.clear_info = 1
        self.build()

if __name__ == '__main__':
    HelpOnApp().run()
