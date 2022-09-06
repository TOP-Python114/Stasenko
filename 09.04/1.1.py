
class ClassBuilder:
    def __init__(self, class_name: str):
        self.class_name = class_name
        self.lines: list[str] = []



    def add_lines(self, *line: str|int|bool):
        self.lines += [line]
        return self


    def clear(self):
        self.lines.clear()


    def __str__(self):
        if not self.lines:
            return f"Class {self.class_name}:\n\tpass"
        def Meaning(line):
            if type(line) == int:
                return 'int'
            if type(line) == str:
                return 'str'
            if type(line) == bool:
                return 'bool'
        s_line =", ".join(line[0] + f': {Meaning(line[1])}' for line in self.lines)
        finished_lines = '\n\t\t'.join([f"self.{line[0]} = " + str(line[1]) for line in self.lines])
        return f"Class {self.class_name}:\n\tdef __init__(self, {s_line}):\n\t\t{finished_lines}"


body = ClassBuilder("CyberSport")
print(body)
print()
print()
body.add_lines("nick", 'Malibuca').add_lines("age", 17).add_lines("country", 'Serbia')
print(body)
print()
print()
body.clear()
body.add_lines("nick", 'Toose').add_lines("age", 20).add_lines("signed", False)
print(body)

