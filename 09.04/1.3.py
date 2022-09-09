
class HTMLElement:
    default_indent_size = 5


    def __init__(self, name: str, value: str = '', **kwargs):
        self.name = name
        self.value = value
        self.elements: list['HTMLElement'] = []
        self.kwargs = ''.join([f' {name}="{value}"' for name, value in kwargs.items()])


    def __str__(self):
        return self.__str()


    def __str(self, indent_lvl: int = 0):
        indent = ' ' * indent_lvl * self.__class__.default_indent_size
        ret = f'{indent}<{self.name}{self.kwargs}>{self.value}'
        if self.elements:
            for element in self.elements:
                ret += '\n' + element.__str(indent_lvl+1)
            ret += f'\n{indent}</{self.name}>'
        else:
            ret += f'</{self.name}>'
        return ret


class HTMLBuilder:
    def __init__(self, root: str | HTMLElement, **kwargs):
        if isinstance(root, str):
            self.__root = HTMLElement(root, **kwargs)
        elif isinstance(root, HTMLElement):
            self.__root = root


    def add_child(self, name: str, value: str = '', **kwargs):
        self.__root.elements += [
            el := HTMLElement(name, value, **kwargs)
        ]
        return HTMLBuilder(el)


    def add_sibling(self, name: str, value: str = '', **kwargs):
        self.__root.elements += [
            HTMLElement(name, value, **kwargs)
        ]
        return self


    def __str__(self):
        return str(self.__root)


class CVBuilder:
    def __init__(self, full_name: str, age: int, occupation: str, portfolio: list[str] = None, **contacts):
        self.full_name = full_name
        self.age = age
        self.portfolio = portfolio
        self.occupation = occupation
        self.contacts: list = [contacts]
        self.education: str = ''
        self.projects: list[dict] = []


    def add_education(self, *education: str | int):
        self.education = ', '.join(map(str, education))
        return self


    def add_project(self, *project):
        self.projects += [project]
        return self


    def add_contact(self, **contact):
        self.contacts += [contact]
        return self


    def build(self):
        self.html = HTMLBuilder('html')
        self.head = self.html.add_child('head').add_sibling('title', f'Портфолио: {self.full_name}')
        self.body = self.html.add_child('body')
        self.about = self.body.add_child('div', id='About')
        self.temp1 = self.about.add_child('div', id='Main_information').add_sibling('h1', 'Обо мне')\
            .add_sibling('p', f'{self.age} лет  Род деятельности: {self.occupation}')

        if self.education:
            self.temp1.add_sibling('p', f'Образование: {self.education}')
        if self.projects:
            for project in self.projects:
                self.temp2 = self.about.add_child('div', f'{project[0]}:', id = 'Lincs')
                for link in project[1:]:
                    self.temp2.add_child('p', src=link)

        self.temp3 = self.about.add_child('div', id = 'Contacts')
        for contact in self.contacts:
            self.temp3.add_sibling('p', f'{contact}'[1:-1])


        return self.html



cv1 = CVBuilder('Миронов Ярослав Алексеевич', 17, 'Киберспортсмен', email='yarik@loh.gg') \
    .add_education('Ставропольский Строительный Техникум', 'Газовщик', f'Дата поступления: {2020} учебный год')\
    .add_contact(telegram='@yarikgg')\
    .add_project('Статистика', 'https://fortnitetracker.com/profile/all/LIL%20MANGOL')\
    .add_project('Twitch аккаунт', 'https://www.twitch.tv/yyaattii')\
    .build()

print(cv1)