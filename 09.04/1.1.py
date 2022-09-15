# ДОБАВИТЬ: строку документации для класса
class ClassBuilder:
    def __init__(self, class_name: str):
        self.class_name = class_name
        self.lines: list[str] = []

    # ИСПРАВИТЬ: вы добавляете атрибут, почему у вас имя add_lines (да ещё во множественном числе) — может имя add_attribute будет больше соответствовать назначению метода?
    # ДОБАВИТЬ: строку документации для метода — начинается с глагола и отвечает на вопрос "что делает?"
    def add_lines(self,
                  # ОТВЕТИТЬ: а почему произвольное количество аргументов? в самом общем случае там может быть имя атрибута, аннотация типа и значение по умолчанию — три элемента максимум; может, имеет смысл их явно перечислить в этом методе?
                  *line: str | int | bool):
        self.lines += [line]
        return self

    # ДОБАВИТЬ: строку документации для метода
    def clear(self):
        self.lines.clear()

    def __str__(self):
        if not self.lines:
            # ИСПРАВИТЬ: ключевое слово class пишется в нижнем регистре
            return f'class {self.class_name}:\n\tpass'

        # ИСПРАВИТЬ: имена функций в Python мы пишем в нижнем регистре, разделяя слова в имени символом подчёркивания — это называется змеиный_нижний_регистр (snake_lower_case)
        # ИСПРАВИТЬ: как имя meaning ("значение") соотносится с назначением этой функции (возврат имени класса)?
        # я имел ввиду, что эта функция определяет значение аргумента, который в него передаётся(слово, цифра или буллевое значение)

        # ДОБАВИТЬ: строку документации для функции
        def meaning(line):
            # ИСПОЛЬЗОВАТЬ: а ещё можно так:
            return type(line).__name__

        s_line = ', '.join(
            # ДОБАВИТЬ: значения по умолчанию для ваших атрибутов
            line[0] + f': {meaning(line[1])}'
            for line in self.lines
        )
        finished_lines = '\n\t\t'.join(
            # ИСПРАВИТЬ: преобразовывать в список не нужно, метод join() принимает и генераторные выражения тоже
             f'self.{line[0]} = ' + str(line[1])
             for line in self.lines
        )
        # ИСПРАВИТЬ: ключевое слово class пишется в нижнем регистре
        return f'class {self.class_name}:\n' \
               f'\tdef __init__(self, {s_line}):\n' \
               f'\t\t{finished_lines}'


body = ClassBuilder("CyberSport")
print(body)
print('\n')

body.add_lines("nick", 'Malibuca')\
    .add_lines("age", 17)\
    .add_lines("country", 'Serbia')
print(body)
print('\n')

body.clear()
body.add_lines("nick", 'Toose')\
    .add_lines("age", 20)\
    .add_lines("signed", False)
print(body)
