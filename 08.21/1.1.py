from random import choice

# 1)
suit = ['Бубны', 'Пики', 'Черви', 'Крести']

# ИСПРАВИТЬ: мы не используем имена встроенных функций для собственных переменных — в данном случае, например, после этой строки вы не сможете воспользоваться встроенной функцией list() для преобразования итерируемого объекта в список
list = []
iter_list = iter(list)
# КОММЕНТАРИЙ: это рабочий вариант, но можно лучше: найдите в документации встроенную функцию enumerate(), изучите, как она работает, и перепишите этот цикл, используя enumerate()
for j in suit:
    for i in range(1, 14):
        list.append([i, j])
        print(iter_list.__next__())


# 2)
# ДОБАВИТЬ: а где, собственно, функция-генератор? напоминаю, что это задание на генераторы
print(choice(list))


# ДОБАВИТЬ: после кода под комментарием stdout закомментированный вывод примера выполнения
# stdout:


# ИТОГ: главная часть задания пропущена — 2/6


# ДОБАВИТЬ: вторую задачу из задания 2 — функцию для проверки можно использовать любую
