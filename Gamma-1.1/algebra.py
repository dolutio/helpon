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
          
          layout = GridLayout(cols=1, spacing=10, size_hint_y=2.5)
          layout.bind(minimum_height=layout.setter('height'))

          layout.add_widget(alg_grand_title)

          abb_multi_formula_children_labels_list = []
          
          

          a_plus_b_in_q = Label(text=' (a+b)² = a² + 2ab + b²', halign='left', valign='middle')
          abb_multi_formula_children_labels_list.append(a_plus_b_in_q)

          a_minus_b_in_q = Label(text=' (a-b)² = a² - 2ab + b²', halign='left', valign='middle')
          abb_multi_formula_children_labels_list.append(a_minus_b_in_q)

          a2mb2 = Label(text=' (a-b)(a+b) = a² - b²', halign='left', valign='middle')
          abb_multi_formula_children_labels_list.append(a2mb2)
          

          

          a3pb3 = Label(text=' (a+b)(a²-ab+b²) = a³ + b³')
          abb_multi_formula_children_labels_list.append(a3pb3)
          

          a3mb3= Label(text=' (a-b)(a²+ab+b²) = a³ - b³')
          abb_multi_formula_children_labels_list.append(a3mb3)
          

          apb3 = Label(text='(a+b)³ = a³ + 3a²b + 3ab² + b³')
          abb_multi_formula_children_labels_list.append(apb3)
          

          amb3 = Label(text='(a - b)³ = a³ - 3a²b + 3ab² - b³')
          abb_multi_formula_children_labels_list.append(amb3)
          
          
          
          abb_multi_formula = Title('Abbreviated multiplication formula', 'Formule de multiplication abrégée', 'Сокращенная формула умножения', 'Կրճատ բազմապատկման աղյուսակ', abb_multi_formula_children_labels_list, 5)
          abb_multi_formula_layout = GridLayout(cols=1, spacing=10)
          abb_multi_formula_layout.add_widget(abb_multi_formula)
          layout.add_widget(abb_multi_formula_layout)

          discriminant = Title('Discriminant', 'Discriminant', 'Дискриминант', 'Դիսկրիմինանտ', [Label(text='D = b² - 4ac')], 1)
          discriminant_layout = GridLayout(cols=1, spacing=10)
          discriminant_layout.add_widget(discriminant)
          layout.add_widget(discriminant_layout)


          

          x1form = Label(text='x1 = (-b - √D) / 2a')
          x2form = Label(text='x2 = (-b + √D) / 2a')

          discinfo = Label('(D is discriminant)', '(D c\'est discriminant)', '(D - это дискриминант)', '(D-ն դիսկրիմինանտն է)')
          


          vtheorem = Label('Viette\'s theorem', 'Théorème de Viette', 'Теорема Виета', 'Վիետի թեորեմ')
          vtheorem.font_size += 5

          x1px2 = Label(text='x1 + x2 = -b')
          x1x2 = Label(text='x1 * x2 = c')

          
          q_e_w_a_e_s_c = Label('Quadratic equation with an even second coefficient', 'Équation quadratique avec un deuxième coefficient pair', 'Квадратное уравнение с четным вторым коэффицентом', 'Քառակուսային հավասարում զույգ երկրորդ գործակցով')
          q_e_w_a_e_s_c.font_size += 5
          
          quad_example_1 = Label(text='D = k² - ac')

          quad_example_2 = Label(text='x1 = (-k - √D) / a')

          quad_example_3 = Label(text='x2 = (-k + √D) / a')

          quadratic_equation_layout = GridLayout(cols=1, spacing=10)

          quadratic_equation_childrens_list = [x1form, x2form, discinfo, vtheorem, x1px2, x1x2, q_e_w_a_e_s_c, quad_example_1, quad_example_2, quad_example_3]

          quadrequation = Title('Quadratic equation', 'Équation quadratique', 'Квадратное уравнение', 'Քառակուսային հավասարում', quadratic_equation_childrens_list, 10)
          quadratic_equation_layout.add_widget(quadrequation)
          layout.add_widget(quadratic_equation_layout)
          
          

          probability_example = Label(text='P = m / n')

          probability_m = Label(text='m is the desired result')

          probability_n = Label(text='n is the number of possible options')

          probability_childrens_list = [probability_example, probability_m, probability_n]

          probability_layout = GridLayout(cols=1, spacing=10)
          probability_title = Title('Formula for finding the probability', 'Formule pour trouver la probabilité', 'Формула для нахождения вероятности', 'Հավանականությունը գտնելու բանաձև', probability_childrens_list, 3)
          probability_layout.add_widget(probability_title)
          layout.add_widget(probability_layout)

          

          frequency_example = Label(text='W = m / n')

          frequency_m = Label('m is the quantity of a certain result', 'm est la quantité d’un certain résultat', 'm - количество определенного результата', 'm-ը որոշակի արդյունքի թիվն է')

          frequency_n = Label(text='n is the quantity of actions')

          frequency_childrens_list = [frequency_example, frequency_m, frequency_n]
          
          frequency_layout = GridLayout(cols=1, spacing=10)
          frequency_title = Title('Formula for finding frequency', 'Formule pour trouver la fréquence', 'Формула для нахождения частоты', 'Հաճախականությունը որոշելու բանաձև', frequency_childrens_list, 3)
          frequency_layout.add_widget(frequency_title)
          layout.add_widget(frequency_layout)

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

          screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-100))
          screen.add_widget(layout)

          self.add_widget(screen)