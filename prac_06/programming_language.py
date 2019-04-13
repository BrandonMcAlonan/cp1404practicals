class ProgrammingLanguage:
    def __init__(self, name="", dynamic="", reflection=bool, year=int):
        self.name = name
        self.dynamic = dynamic
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.dynamic == "Dynamic":
            dynamic_status = True
        else:
            dynamic_status = False
        return dynamic_status

    def __str__(self, name="", dynamic=""):
        string = "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.dynamic, self.reflection,
                                                                             self.year)
        return string
