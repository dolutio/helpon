from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivy.core.window import Window

from uix.labels import Label

class Algebra(BoxLayout):
     def __init__(self):
          super().__init__()
          self.orientation = 'vertical'

          self.build()

     def build(self):
          alg_grand_title = Label('Algebra', 'Algèbre', 'Алгебра', 'Հանրահաշիվ')
          alg_grand_title.font_size += 15
          
          layout = GridLayout(cols=1, spacing=10, size_hint_y=4)
          layout.bind(minimum_height=layout.setter('height'))

          layout.add_widget(alg_grand_title)

          abb_multi_formula_drop = DropDown()
          abb_multi_formula = Label('Abbreviated multiplication formula', 'Formule de multiplication abrégée', 'Сокращенная формула умножения', 'Կրճատ բազմապատկման աղյուսակ')
          abb_multi_formula.font_size += 10
          layout.add_widget(abb_multi_formula)

          a_plus_b_in_2 = Label(text=' (a+b)² = a² + 2ab + b²', halign='left', valign='middle')
          layout.add_widget(a_plus_b_in_2)

          a_minus_b_in_2 = Label(text=' (a-b)² = a² - 2ab + b²', halign='left', valign='middle')
          layout.add_widget(a_minus_b_in_2)

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

          discriminant = Label('Discriminant', 'Discriminant', 'Дискриминант', 'Դիսկրիմինանտ')
          discriminant.font_size += 10
          layout.add_widget(discriminant)

          discformul = Label(text='D = b² - 4ac')
          layout.add_widget(discformul)


          quadrequation = Label('Quadratic equation', 'Équation quadratique', 'Квадратное уравнение', 'Քառակուսային հավասարում')
          quadrequation.font_size += 10
          layout.add_widget(quadrequation)

          x1form = Label(text='x1 = (-b - √D) / 2a')
          x2form = Label(text='x2 = (-b + √D) / 2a')
          layout.add_widget(x1form)
          layout.add_widget(x2form)
          discinfo = Label('(D is discriminant)', '(D c\'est discriminant)', '(D - это дискриминант)', '(D-ն դիսկրիմինանտն է)')
          layout.add_widget(discinfo)



          vtheorem = Label('Viette\'s theorem', 'Théorème de Viette', 'Теорема Виета', 'Վիետի թեորեմ')
          vtheorem.font_size += 5
          layout.add_widget(vtheorem)

          x1px2 = Label(text='x1 + x2 = -b')
          layout.add_widget(x1px2)
          x1x2 = Label(text='x1 * x2 = c')
          layout.add_widget(x1x2)

          
          q_e_w_a_e_s_c = Label('Quadratic equation with an even second coefficient', 'Équation quadratique avec un deuxième coefficient pair', 'Квадратное уравнение с четным вторым коэффицентом', 'Քառակուսային հավասարում զույգ երկրորդ գործակցով')
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

          probability_m = Label(text='m is the desired result')
          layout.add_widget(probability_m)

          probability_n = Label(text='n is the number of possible options')
          layout.add_widget(probability_n)

          frequency_title = Label(text='Formula for finding frequency')
          frequency_title.font_size += 10
          layout.add_widget(frequency_title)

          frequency_example = Label(text='W = m / n')
          layout.add_widget(frequency_example)

          frequency_m = Label(text='m is desired result')
          layout.add_widget(frequency_m)

          frequency_n = Label(text='n is the number of actions')
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

          screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-100))
          screen.add_widget(layout)

          self.add_widget(screen)