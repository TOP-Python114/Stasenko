from random import choice

# 1)
suit1 = ['Бубны', 'Пики', 'Черви', 'Крести']

loc1 = []
iter_list = iter(loc1)

for count in suit1:
    for i in range(1, 14):
        loc1.append([i, count])
        print(iter_list.__next__())

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









