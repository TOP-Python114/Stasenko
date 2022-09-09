class HTMLElement:
    default_indent_size = 4

    def __init__(self, name: str, value: str = '', **kwargs):
        self.name = name
        self.value = value
        self.elements: list['HTMLElement'] = []
        self.kwargs = ''.join([f' {name}='{value}'' for name, value in kwargs.items()])

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


# ручное создание элементов и связей между ними
# li1 = HTMLElement('li', 'элемент 1')
# li2 = HTMLElement('li', 'элемент 2')
# ul = HTMLElement('ul')
# ul.elements += [li1, li2]
# div = HTMLElement('div')
# div.elements += [ul]
# print(div)

# использование строителя
body = HTMLBuilder('body', style='background-color:red')
menu = body.add_child('div', id='div').add_child('ul')
menu.add_child('li', 'File')\
    .add_sibling('p', 'New')\
    .add_sibling('p', 'Open')\
    .add_sibling('p', 'Save')
menu.add_child('li', 'Edit')\
    .add_sibling('p', 'Undo')\
    .add_sibling('p', 'Redo')\
    .add_sibling('p', 'Cut')\
    .add_sibling('p', 'Copy')\
    .add_sibling('p', 'Paste')
print(body)