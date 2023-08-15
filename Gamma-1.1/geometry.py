from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

class Geometry(BoxLayout):
    orientation = 'vertical'
    def __init__(self, *args):
            super().__init__()
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
            
    

    
    
    
            screen = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-100))
            screen.add_widget(layout)

            self.add_widget(screen)