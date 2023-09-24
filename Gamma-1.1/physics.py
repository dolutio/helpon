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
     
        ph_grand_title = Label('Physics', 'Physique', 'Физика', 'Ֆիզիկա')
        ph_grand_title.font_size += 15
        layout.add_widget(ph_grand_title)

        designation_of_volume = Label('V is volume', 'V est le volume', 'V - это объем', 'V-ն ծավալն է')
        designation_of_speed = Label('v is speed', 'v', 'v - это скорость', 'v-ն արագությունն է')
        designation_of_area = Label('S is area', 'S est la superficie', 'S - это площадь', 'S-ը մակրեսեն է')
        designation_of_length = Label('s is length', 's est la longueur', 's - это длина', 's-ը երկարությունն է')
        designation_of_height = Label('h is height', 'h est la hauteur', 'h - это высота', 'h- բարձրությունն է')
        designation_of_density = Label('ρ is density', 'ρ est la densité', 'ρ - это плотность', 'ρ-ն խտությունն է')
        designation_of_time = Label('t is time', 't est le temps', 't - это время', 't-ն ժամանակն է')
        designation_of_mass = Label('m is mass', 'm est la masse', 'm - масса', 'm-ը զանգվածն է')
        designation_of_grav = Label('g is gravitational constant', 'g est la constante gravitationnelle', 'g - это ускорение свободного падения', 'g-ն ազատ անկման արագացումն է')   
        designation_of_pressure = Label('P is pressure', 'P est la pression', 'P - это давление', 'P-ն ճնշումն է')
        designation_of_force = Label('F is force', 'F est la force', 'F - это сила', 'F-ը ուժն է')
        designation_of_work =  Label('A is work', 'A est le travail', 'A - это работа', 'A-ն աշխատանքն է')
        designation_of_power = Label('N is power', 'N est la puissance', 'N - мощность', 'N-ը հզորությունն է')

        designations_children_list = [designation_of_volume, designation_of_speed, designation_of_area, designation_of_length, designation_of_height, designation_of_density, designation_of_time, designation_of_mass, designation_of_grav, designation_of_pressure, designation_of_force, designation_of_work, designation_of_power]
        
        designations_layout = GridLayout(cols=1, spacing=10)
        designations_title = Title('Designations', 'Désignations', 'Обозначения', 'Նշանակումներ', designations_children_list)
        designations_layout.add_widget(designations_title)
        layout.add_widget(designations_layout)

        area_formula_1 = Label(text='S = h²')
        area_formula_2 = Label(text='S = V / h')
        area_formula_3 = Label(text='S = F / P')
        
        area_children_list = [area_formula_1, area_formula_2, area_formula_3]
        
        area_formula_layout = GridLayout(cols=1, spacing=10)
        area_formula_title = Title('Formula for finding area', 'Formule pour trouver l\'aire', 'Формула нахождения площади', 'Մակերեսը գտնելու բանաձևը', area_children_list)
        area_formula_layout.add_widget(area_formula_title)
        layout.add_widget(area_formula_layout)

              


        length_formula_1 = Label(text='s = vt')
        length_formula_2 = Label(text='s = A / F')

        length_children_list = [length_formula_1, length_formula_2]
        
        length_formulas_layout = GridLayout(cols=1, spacing=10)
        length_formulas_title = Title('Formulas for finding length', 'Formules pour trouver la longueur', 'Формулы нахождения длины', 'Երկարությունը գտնելու բանաձևերը', length_children_list)
        length_formulas_layout.add_widget(length_formulas_title)
        layout.add_widget(length_formulas_layout)

        

        time_formula_1 = Label(text='t = s / v')
        time_formula_2 = Label(text='t = A / N')

        time_children_list = [time_formula_1, time_formula_2]

        time_formula_layout = GridLayout(cols=1, spacing=10)
        time_formulas_title = Title('Formulas for finding time', 'Formules de découverte du temps', 'Формулы нахождения времени', 'Ժամանակը գտնելու բանաձևերը', time_children_list)
        time_formula_layout.add_widget(time_formulas_title)
        layout.add_widget(time_formula_layout)

       

        mass_formula_1 = Label(text='1.m = ρV')
        mass_formula_2 = Label(text='2.m = F / g')
        
        mass_children_list = [mass_formula_1, mass_formula_2]

        mass_formulas_layout = GridLayout(cols=1, spacing=10)
        mass_formulas_title = Title('Formulas for finding mass', 'Formules pour trouver la masse', 'Формула нахождения массы', 'Զանգվածը գտնելու բանաձևը', mass_children_list)
        mass_formulas_layout.add_widget(mass_formulas_title)
        layout.add_widget(mass_formulas_layout)

        
        
        

        heft_formula = Label(text='W = F = mg')
        
        heft_children_list = [heft_formula]
        
        heft_formula_layout = GridLayout(cols=1, spacing=10)
        heft_formula_title = Title('Formula for finding heft', 'Formule pour trouver le poids', 'Формула нахождения веса', 'Կշիռը գտնելու բանաձևը', heft_children_list, True)
        heft_formula_layout.add_widget(heft_formula_title)

        arch_principle_formula = Label(text='F = ρgV')

        arch_principle_children_list = [arch_principle_formula]

        arch_principle_layout = GridLayout(cols=1, spacing=10)
        arch_principle_title = Title('Archimedes law', 'Principe d\'Archimède', 'Закон Архимеда', 'Արքիմեդի օրենքը', arch_principle_children_list, True)
        arch_principle_layout.add_widget(arch_principle_title)
        
        force_childrens_list = [heft_formula_layout, arch_principle_layout]
        force_formulas_layout = GridLayout(cols=1, spacing=10)
        force_formulas_title = Title('Formulas for finding', 'Formules pour trouver', 'Формулы нахождения силы', 'Ուժը գտնելու բանաձևերը', force_childrens_list)
        force_formulas_layout.add_widget(force_formulas_title)
        layout.add_widget(force_formulas_layout)

        

        speed_formul_1 = Label(text='v = s / t')

        speed_formula_children_list = [speed_formul_1]

        speed_formulas_layout = GridLayout(cols=1, spacing=10)
        speed_formulas_title = Title('Formulas for finding speed', 'Formules pour trouver la vitesse', 'Формула нахождения скорости', 'Արագությունը գտնելու բանաձևը', speed_formula_children_list)
        speed_formulas_layout.add_widget(speed_formulas_title)
        layout.add_widget(speed_formulas_layout)    

        screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-100))
        screen.add_widget(layout)
        self.add_widget(screen)