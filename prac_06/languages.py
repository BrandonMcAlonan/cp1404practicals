from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(str(python))

    print("The dynamically typed languages are:")
    languages = [ruby, python, visual_basic]
    for language in languages:
        dynamic_status = language.is_dynamic()
        if dynamic_status is True:
            print(language.name)


main()
