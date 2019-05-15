from kivy.app import App
from kivy.lang import Builder

widget_list = ["This", "Is a", "Dynamic", "App"]


class SimpleDynamicApp(App):
    def build(self):
        self.title = "Simple Dynamic App"
        self.root = Builder.load_file('simple_dynamic_app.kv')
        return self.root

    def create_dynamic_widgets(self):
        for name in self.widget_list:
            temp_label = Labe1(text=name)
            self.root.ids.widgets_here.add_widget(temp_label)


SimpleDynamicApp().run()
