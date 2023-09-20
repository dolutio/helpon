from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from uix.labels import Title, Label
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

        

        designation_of_volume = Label('V is volume', 'V est le volume', 'V - это объем', 'V-ն ծավալն է')
        designation_of_speed = Label('v is speed', 'v', 'v - это скорость', 'v-ն արագությունն է')
        designation_of_area = Label('S is area', 'S', 'S - это площадь', 'S-ը մակրեսեն է')
        designation_of_length = Label('s is length', 's', 's - это длина', 's-ը երկարությունն է')
        designation_of_height = Label('h is height', 'h', 'h - это высота', 'h- բարձրությունն է')
        designation_of_density = Label('ρ is density', 'ρ', 'ρ - это плотность', 'ρ-ն խտությունն է')
        designation_of_time = Label('t is time', 't', 't - это время', 't-ն ժամանակն է')
        designation_of_mass = Label('m is mass', 'm', 'm - масса', 'm-ը զանգվածն է')
        designation_of_grav = Label('g is gravitational constant', 'g', 'g - это ускорение свободного падения', 'g-ն ազատ անկման արագացումն է')   
        designation_of_pressure = Label('P is pressure', 'P', 'P - это давление', 'P-ն ճնշումն է')
        designation_of_force = Label('F is force', 'F', 'F - это сила', 'F-ը ուժն է')
        designation_of_work =  Label('A is work', 'A', 'A - это работа', 'A-ն աշխատանքն է')
        designation_of_power = Label('N is power', 'N', 'N - мощность', 'N-ը հզորությունն է')

        designations_children_list = [designation_of_volume, designation_of_speed, designation_of_area, designation_of_length, designation_of_height, designation_of_density, designation_of_time, designation_of_mass, designation_of_grav, designation_of_pressure, designation_of_force, designation_of_work, designation_of_power]
        
        designations_layout = GridLayout(cols=1, spacing=10)
        designations_title = Title('Designations', 'Désignations', 'Обозначения', 'Նշանակումներ', designations_children_list)
        designations_layout.add_widget(designations_title)
        layout.add_widget(designations_layout)

        area_formula_1 = Label(text='S = h²')
        area_formula_2 = Label(text='S = V / h')
        area_formula_3 = Label(text='S = F / P')
        
        area_children_list = [area_formula_1, area_formula_2, area_formula_3]
        
        area_formulas_layout = GridLayout(cols=1, spacing=10)
        area_formulas_title = Title('Formula for finding area', '', 'Формула нахождения площади', 'Մակերեսը գտնելու բանաձևը', area_children_list)
        area_formulas_layout.add_widget(area_formulas_title)
        layout.add_widget(area_formulas_layout)

              


        length_formula_1 = Label(text='s = vt')
        length_formula_2 = Label(text='s = A / F')

        length_children_list = [length_formula_1, length_formula_2]
        
        length_formulas_layout = GridLayout(cols=1, spacing=10)
        length_formulas_title = Title('Formulas for finding length', '', '', 'Երկարությունը գտնելու բանաձևը', length_children_list)
        length_formulas_layout.add_widget(length_formulas_title)
        layout.add_widget(length_formulas_layout)

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