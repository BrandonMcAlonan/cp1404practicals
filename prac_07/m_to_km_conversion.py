from kivy.app import App
from kivy.lang import Builder

CONVERSION_VALUE = 1.609344


class ConvertMileKilometersApp(App):
    def build(self):
        self.title = "Convert Miles To Kilometers"
        self.root = Builder.load_file('m_to_km_conversion.kv')
        return self.root

    def handle_calculate(self):
        value = self.validate_input()
        km = CONVERSION_VALUE * value
        self.root.ids.output_label.text = str(km)

    def handle_increment(self, increment):
        m = self.validate_input()
        m += increment
        self.root.ids.input_number.text = str(m)
        self.handle_calculate()

    def validate_input(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMileKilometersApp().run()
