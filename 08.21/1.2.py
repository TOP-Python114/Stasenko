from itertools import permutations

# ИСПРАВИТЬ: мы не используем имена встроенных функций для собственных переменных — set
words = {'вкусные','котлетки','с пюрешкой'}
# ИСПРАВИТЬ: мы не используем имена встроенных функций для собственных переменных — list
# ИСПРАВИТЬ: традиция и привычка диктуют нам использовать имена i, j, k только для индексов
# исправил

count = 0
def permutation(elements: set):
    global count
    for v in permutations(elements):
        count += 1
        yield ' '.join(v)

        # ИСПРАВИТЬ: зачем вам этот счётчик? вы формируете список, забив на генератор — ну дак посчитайте длину списка в конце
        # ИСПРАВИТЬ: это не механика генератора
        #исправил

conclusion = permutation(words)

# ИСПОЛЬЗОВАТЬ: при подстановке любых объектов в f-строку нет необходимости явно преобразовывать объект в строку — это происходит неявно
# не совсем понять, что вы имели в виду ^

for i in conclusion:
    print(f'Вариант: №{count}   {i}')



# ДОБАВИТЬ: после кода под комментарием stdout закомментированный вывод примера выполнения
# stdout:
# Вариант: №1   котлетки вкусные с пюрешкой
# Вариант: №2   котлетки с пюрешкой вкусные
# Вариант: №3   вкусные котлетки с пюрешкой
# Вариант: №4   вкусные с пюрешкой котлетки
# Вариант: №5   с пюрешкой котлетки вкусные
# Вариант: №6   с пюрешкой вкусные котлетки

# КОММЕНТАРИЙ: на случай, если вы ничего не поняли о генераторах: даже после лекции, чтения литературы и разбора примеров — то это хороший такой повод задать вопрос преподавателю — используйте этот повод
# ЛАЙФХАК: вопросы можно писать прямо здесь, комментарием

# вроде как всё исправленно
# ИТОГ: переписать — 1/6
