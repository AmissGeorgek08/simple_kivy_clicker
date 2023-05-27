#imports
from kivy.app import App
from kivy.uix.button import Button

#app class
class Unclicker(App):
    def build(self):
        self.click_count = 0
        button = Button(text="Unclick", font_size=30)
        button.bind(on_press=self.show_click_count)
        return button
    def show_click_count(self, instance):
        self.click_count -= 1
        instance.text = "Unclick ({})".format(self.click_count)

#run command
if __name__ == '__main__':
    Unclicker().run()