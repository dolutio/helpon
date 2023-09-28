from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

from uix.labels import Title, Label

class Geometry(BoxLayout):
    orientation = 'vertical'
    def __init__(self, *args):
            super().__init__()
            layout = GridLayout(cols=1, spacing=10, size_hint_y=1)
            layout.bind(minimum_height=layout.setter('height'))
            #tang, cotang, sin2+cos2, sin90-x, cos90-x, sin180-x, cos180-x, Pifagor
            self.trig = BoxLayout()
            self.sin = BoxLayout(orientation='vertical')
            self.cos = BoxLayout(orientation='vertical')
    
            geometry = Label('Geometry', 'Géométrie', 'Геометрия', 'Երկրաչափություն')
            geometry.font_size += 20
            layout.add_widget(geometry)
    
            
    
            tang_formul = Label(text='tang(α) = sin(α) / cos(α)')
    
            cotang_formul = Label(text='cotang(α) = cos(α) / sin(α)')
    
            sin90mx = Label(text='sin(90 - α) = cos(α)')

            cos90mx = Label(text='cos(90 - α) = sin(α)')

            tang90mx = Label(text='tang(90 - α) = cotang(α)')

            cotang90mx = Label(text='cotang(90 - α) = tang(α)')

            sin180mx = Label(text='sin(180 - α) = sin(α)')

            cos180mx = Label(text='cos(180 - α) = -cos(α)')

            tang180mx = Label(text='tang(180 - α) = -cotang(α)')

            cotang180mx = Label(text='cotang(180 - α) = -tang(α)')    
    
            sin2x_plus_cos2x = Label(text='sin²(α) + cos²(α) = 1')
    
            tangcotangformul = Label(text='tang(α) * cotang(α) = 1')
    
            trigonometry_childrens_list = [tang_formul, cotang_formul, sin90mx, cos90mx, tang90mx, cotang90mx, sin180mx, cos180mx, tang180mx, cotang180mx, sin2x_plus_cos2x, tangcotangformul]
            
            trigonometry_layout = GridLayout(cols=1, spacing=10)
            trigonometry = Title('Trigonometry', 'Trigonométrie', 'Тригонометрия', 'Տրիգոնոմետրիա', trigonometry_childrens_list)
            trigonometry_layout.add_widget(trigonometry)
            layout.add_widget(trigonometry_layout)

            
    
            sine_theorem_formul = Label(text='a/sin(α) = b/sin(β) = c/sin(γ)')
            sine_children_list = [sine_theorem_formul]
            
            sine_layout = GridLayout(cols=1, spacing=10)
            sine_theorem_label = Title('The theorem of sines', 'Théorème des sinus', 'Теорема синусов', 'Սինուսների թեորեմը', sine_children_list)
            sine_layout.add_widget(sine_theorem_label)
            layout.add_widget(sine_layout)
    
            
    
            cos_theorem_formul = Label(text='a² = b² + c² - 2bc*cos(α)')
            cos_children_list = [cos_theorem_formul]

            cos_theorem_layout = GridLayout(cols=1, spacing=10)
            cos_theorem_label = Title('The theorem of cosines', 'Théorème des cosinus', 'Теорема косинусов', 'Կոսինուսների թեորեմը', cos_children_list)
            cos_theorem_layout.add_widget(cos_theorem_label)
            layout.add_widget(cos_theorem_layout)
    
            
    
            pythagorean_theorem_formul = Label(text='a² + b² = c²')
            pythagorean_theorem_children_list = [pythagorean_theorem_formul]
            
            pythagorean_theorem_layout = GridLayout(cols=1, spacing=10)
            pythagorean_theorem_label = Title('Pythagorean theorem', 'Théorème de Pythagore', 'Теорема Пифагора', 'Պյութագորասի թեորեմը', pythagorean_theorem_children_list)
            pythagorean_theorem_layout.add_widget(pythagorean_theorem_label)
            layout.add_widget(pythagorean_theorem_layout)

            distance_between_two_points_formula = Label(text='s = √((x₁ - x₂)² + (y₁ - y₂)²)')

            distance_between_two_points_children_list = [distance_between_two_points_formula]

            distance_between_two_points_layout = GridLayout(cols=1, spacing=10)
            distance_between_two_points_title = Title('Distance between two points', 'Distance entre deux points', 'Расстояние между двумя точками', 'Երկու կետերի միջև հեռավորությունը', distance_between_two_points_children_list)
            distance_between_two_points_layout.add_widget(distance_between_two_points_title)
            layout.add_widget(distance_between_two_points_layout)
    
            screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-100))
            screen.add_widget(layout)

            self.add_widget(screen)