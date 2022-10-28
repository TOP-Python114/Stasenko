from random import randint


class Generator:
    @staticmethod
    def generate(count: int):
        return [randint(1, 9) for _ in range(count)]


class Splitter:
    @staticmethod
    def split(array) -> list:
        result = []

        row_count = len(array)
        col_count = len(array[0])
        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)
        # print(result)
        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []
        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])
        result.append(diag1)
        result.append(diag2)
        return result


class Verifier:
    @staticmethod
    def verify(arrays) -> bool:
        first = sum(arrays[0])
        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False
        return True


class MagicSquareGenerator:
    def __init__(self, wos: int):
        self.w = wos
        self.gen = Generator()
        self.sp = Splitter()
        self.ver = Verifier()

    # ДОБАВИТЬ: аннотацию возвращаемого значения
    def generate(self):
        # ДОБАВИТЬ: строку документации для метода
        while True:
            # ИСПРАВИТЬ: атрибуты создаются, когда некоторое значение предполагается использовать в других методах — здесь же значение res используется только в данном методе, больше нигде — поэтому не нужно создавать атрибут экземпляра, достаточно локальной переменной метода
            self.res = [self.gen.generate(self.w) for _ in range(self.w)]
            if self.ver.verify(self.sp.split(self.res)):
                return self.res


gen = MagicSquareGenerator(3)

# ИСПРАВИТЬ: если переменная цикла используется, то дайте ей нормальное имя — символ _ мы ставим только когда переменная цикла не используется ни разу
for _ in gen.generate():
    print(*_)

# stdout:
# 8 3 7
# 5 6 7
# 5 9 4


# ИТОГ: хорошо — 5/6


# СДЕЛАТЬ: не ждите, пока я проверю первую часть, делайте сразу и вторую =)
