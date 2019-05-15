from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

widget_list = ["This", "Is a", "Dynamic", "App"]


class SimpleDynamicApp(App):

    def build(self):
        self.title = "Simple Dynamic App"
        self.root = Builder.load_file('simple_dynamic_app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in widget_list:
            temp_label = Label(text=name)
            self.root.ids.widgets_here.add_widget(temp_label)


SimpleDynamicApp().run()

