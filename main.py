from kivy.config import Config

Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '640')

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.screen import MDScreen


class CollectionApp(MDApp):

    def __init__(self, **kwargs):
        super(CollectionApp, self).__init__(**kwargs)
        Clock.schedule_interval(lambda *_: self.update_data(), 1)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file('main.kv')

    def update_data(self):
        # stopped, status?
        pass


class MainScreen(MDScreen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


if __name__ == "__main__":
    CollectionApp().run()