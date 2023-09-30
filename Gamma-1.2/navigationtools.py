from json import dump

from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.uix.navigationdrawer import MDNavigationDrawer as NavigationDrawer, MDNavigationLayout as NavigationLayout
from kivymd.uix.menu import MDDropdownMenu as Menu

from kivy.core.window import Window

import uix.buttons as buttons
from uix.buttons import FeedBackButton, LanguageButton, GitHubButton
from translation import translate, translate_use_widgets_list

class NavigationDrawerContent(BoxLayout):
    orientation = 'vertical'
    def __init__(self, app):
        super().__init__()

        self.app = app
        
        self.feedback_btn = FeedBackButton()
        self.language_btn = LanguageButton(on_release=lambda *a: self.menu_open())
        self.github_btn = GitHubButton()

        self.add_widget(self.feedback_btn)
        self.add_widget(self.github_btn)
        self.add_widget(self.language_btn)
        

    def menu_open(self):
        self.menu_items = [{
            'text': f'{i}',
            'viewclass': 'OneLineListItem',
            'height': dp(56),
            'on_release': lambda language={'ENG': 'en', 'FRA': 'fr', 'РУС': 'ru', 'ՀԱՅ': 'hy'}[i]: self.language_on_release(language),
        } for i in ['ENG', 'FRA', 'РУС', 'ՀԱՅ']]
        self.menu = Menu(caller=self.language_btn, items=self.menu_items, width_mult=3)
        self.menu.open() 

    def language_on_release(self, language):
        
        data = {'language': language}
        with open('language.json', 'w') as json_data:
            dump(data, json_data)
        for i in translate_use_widgets_list:
            i.text_update()