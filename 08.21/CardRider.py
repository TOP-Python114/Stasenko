from random import choice

# 1)
suit = ['Бубны', 'Пики', 'Черви', 'Крести']


list = []
iter_list = iter(list)
for j in suit:
    for i in range(1, 14):
        list.append([i, j])
        print(iter_list.__next__())

# 2)

print(choice(list))