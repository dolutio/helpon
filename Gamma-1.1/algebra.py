from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from uix.labels import ScrollViewTitle
from kivy.uix.widget import Widget
from kivy.core.window import Window

from uix.labels import Title, Label

class Algebra(BoxLayout):
     def __init__(self):
          super().__init__()
          self.orientation = 'vertical'

          self.build()

     def build(self):
          alg_grand_title = Label('Algebra', 'Algèbre', 'Алгебра', 'Հանրահաշիվ')
          alg_grand_title.font_size += 15
          
          layout = GridLayout(cols=1, spacing=10, size_hint_y=1)
          layout.bind(minimum_height=layout.setter('height'))

          layout.add_widget(alg_grand_title)
          
          

          a_plus_b_in_q = Label(text=' (a+b)² = a² + 2ab + b²', halign='left', valign='middle')
          a_minus_b_in_q = Label(text=' (a-b)² = a² - 2ab + b²', halign='left', valign='middle')
          a_q_minus_b_in_q = Label(text=' (a-b)(a+b) = a² - b²', halign='left', valign='middle')
          a_in_cube_plus_b_in_cube = Label(text=' (a+b)(a²-ab+b²) = a³ + b³')
          a_in_cube_minus_b_in_cube = Label(text=' (a-b)(a²+ab+b²) = a³ - b³')
          a_plus_b_in_cube = Label(text='(a+b)³ = a³ + 3a²b + 3ab² + b³')
          a_minus_b_in_cube = Label(text='(a - b)³ = a³ - 3a²b + 3ab² - b³')

          abb_multi_formula_children_labels_list = [a_plus_b_in_q, a_minus_b_in_q, a_q_minus_b_in_q, a_in_cube_plus_b_in_cube, a_in_cube_minus_b_in_cube, a_plus_b_in_cube, a_minus_b_in_cube]
          
          
          
          abb_multi_formula = Title('Abbreviated multiplication formula', 'Formule de multiplication abrégée', 'Сокращенная формула умножения', 'Կրճատ բազմապատկման աղյուսակ', abb_multi_formula_children_labels_list)
          abb_multi_formula_layout = GridLayout(cols=1, spacing=10)
          abb_multi_formula_layout.add_widget(abb_multi_formula)
          layout.add_widget(abb_multi_formula_layout)

          discriminant = Title('Discriminant', 'Discriminant', 'Дискриминант', 'Դիսկրիմինանտ', [Label(text='D = b² - 4ac')])
          discriminant_layout = GridLayout(cols=1, spacing=10)
          discriminant_layout.add_widget(discriminant)
          layout.add_widget(discriminant_layout)


          

          x1form = Label(text='x₁ = (-b - √D) / 2a')
          x2form = Label(text='x₂ = (-b + √D) / 2a')

          discinfo = Label('(D is discriminant)', '(D c\'est discriminant)', '(D - это дискриминант)', '(D-ն դիսկրիմինանտն է)')
          


          vtheorem = Label('Viette\'s theorem', 'Théorème de Viette', 'Теорема Виета', 'Վիետի թեորեմ')
          vtheorem.font_size += 5

          x1px2 = Label(text='x₁ + x₂ = -b')
          x1x2 = Label(text='x₁ * x₂ = c')

          
          q_e_w_a_e_s_c = Label('Quadratic equation with an even second coefficient', 'Équation quadratique avec un deuxième coefficient pair', 'Квадратное уравнение с четным вторым коэффицентом', 'Քառակուսային հավասարում զույգ երկրորդ գործակցով')
          q_e_w_a_e_s_c.font_size += 5
          
          quad_example_1 = Label(text='D = k² - ac')

          quad_example_2 = Label(text='x₁ = (-k - √D) / a')

          quad_example_3 = Label(text='x₂ = (-k + √D) / a')

          quadratic_equation_layout = GridLayout(cols=1, spacing=10)

          quadratic_equation_childrens_list = [x1form, x2form, discinfo, vtheorem, x1px2, x1x2, q_e_w_a_e_s_c, quad_example_1, quad_example_2, quad_example_3]

          quadrequation = Title('Quadratic equation', 'Équation quadratique', 'Квадратное уравнение', 'Քառակուսային հավասարում', quadratic_equation_childrens_list)
          quadratic_equation_layout.add_widget(quadrequation)
          layout.add_widget(quadratic_equation_layout)
          
          

          probability_example = Label(text='P = m / n')

          probability_m = Label('m is the desired result', 'm est le résultat souhaité', 'm - желаемый результат', 'm-ը ցանկալի արդյունքն է')

          probability_n = Label('n is the number of possible options', 'n est le nombre d\'options possibles', 'n - количество возможных вариантов', 'n-ը հնարավոր տարբերակների քանակն է')

          probability_childrens_list = [probability_example, probability_m, probability_n]

          probability_layout = GridLayout(cols=1, spacing=10)
          probability_title = Title('Formula for finding the probability', 'Formule pour trouver la probabilité', 'Формула для нахождения вероятности', 'Հավանականությունը գտնելու բանաձև', probability_childrens_list)
          probability_layout.add_widget(probability_title)
          layout.add_widget(probability_layout)

          

          frequency_example = Label(text='W = m / n')

          frequency_m = Label('m is the quantity of a certain result', 'm est la quantité d’un certain résultat', 'm - количество определенного результата', 'm-ը որոշակի արդյունքի թիվն է')

          frequency_n = Label(text='n is the quantity of actions')

          frequency_childrens_list = [frequency_example, frequency_m, frequency_n]
          
          frequency_layout = GridLayout(cols=1, spacing=10)
          frequency_title = Title('Formula for finding frequency', 'Formule pour trouver la fréquence', 'Формула для нахождения частоты', 'Հաճախականությունը որոշելու բանաձև', frequency_childrens_list)
          frequency_layout.add_widget(frequency_title)
          layout.add_widget(frequency_layout)

          screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-100))
          screen.add_widget(layout)

          self.add_widget(screen)