from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from uix.labels import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

class Physics(BoxLayout):
    orientation = 'vertial'
    def __init__(self):
        super().__init__()
        layout = GridLayout(cols=1, spacing=10, size_hint_y=2.5)
        layout.bind(minimum_height=layout.setter('height'))

        layout.add_widget(Widget())        
        ph_grand_title = Label('Physics', 'Physique', 'Физика', 'Ֆիզիկա')
        ph_grand_title.font_size += 15
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

        length_formulas_title = Label(text='Formulas for finding length')
        length_formulas_title.font_size  += 10
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

        screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-100))
        screen.add_widget(layout)
        self.add_widget(screen)