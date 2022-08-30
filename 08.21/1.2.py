from itertools import permutations


set = {'v','i','d','e','o','s'}

list = []


i = 0

def permutation(set):
    global i
    for p in permutations(set):
        i += 1
        list.append(''.join(p))

permutation(set)


print(list,'\n', f'Всего: {str(i)} варианта\ов')