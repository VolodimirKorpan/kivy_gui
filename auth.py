from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout


class LoginApp(App):
    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation='vertical', size_hint=[None, None], size=[300, 200], spacing=5)

        bl.add_widget(Label(text='E-MAIL'))
        bl.add_widget(TextInput(multiline=False, font_size=20))
        bl.add_widget(Label(text='PASSWORD'))
        bl.add_widget(TextInput(multiline=False, font_size=20))
        bl.add_widget(Button(text='LOGIN'))

        al.add_widget(bl)
        return al


if __name__ == '__main__':
    LoginApp().run()