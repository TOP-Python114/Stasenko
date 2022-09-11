from random import choice

# 1)
suit = ['Бубны', 'Пики', 'Черви', 'Крести']

<<<<<<< Updated upstream
<<<<<<< HEAD
loc1 = []
iter_list = iter(loc1)

for count in suit1:
=======
# ИСПРАВИТЬ: мы не используем имена встроенных функций для собственных переменных — в данном случае, например, после этой строки вы не сможете воспользоваться встроенной функцией list() для преобразования итерируемого объекта в список
list = []
iter_list = iter(list)
# КОММЕНТАРИЙ: это рабочий вариант, но можно лучше: найдите в документации встроенную функцию enumerate(), изучите, как она работает, и перепишите этот цикл, используя enumerate()
for j in suit:
>>>>>>> 187bc5b01de411c524db76327d2544f21a631ae5
=======

list = []
iter_list = iter(list)
for j in suit:
>>>>>>> Stashed changes
    for i in range(1, 14):
        list.append([i, j])
        print(iter_list.__next__())

<<<<<<< Updated upstream
<<<<<<< HEAD
# Я попробовал сделать через enumerate, но код был слишком громосткий и не особо отличался от прошлого


# 2)


loc2 = []
def random_suit(cards):
    while cards:
        rand_card = choice(cards)
        loc2.append(rand_card)
        loc1.remove(rand_card)
        if len(loc2) == 52:
            return loc2

random_set = random_suit(loc1)

for i in random_set:
    print(i, end=' --> ')









=======

# 2)
# ДОБАВИТЬ: а где, собственно, функция-генератор? напоминаю, что это задание на генераторы
print(choice(list))


# ДОБАВИТЬ: после кода под комментарием stdout закомментированный вывод примера выполнения
# stdout:


# ИТОГ: главная часть задания пропущена — 2/6


# ДОБАВИТЬ: вторую задачу из задания 2 — функцию для проверки можно использовать любую
>>>>>>> 187bc5b01de411c524db76327d2544f21a631ae5
=======
# 2)

print(choice(list))
>>>>>>> Stashed changes
