import re


def sort(elem):
    return elem[1]

sorted_words = []


class Processor:
    def process_text(self, text):
        for word in sorted(WordCounter(text).get_all_words().items(), key=sort):
            sorted_words.append(word[0])
        return sorted_words


class TextParser:
    """Парсер текстовых данных в некой системе."""
    def __init__(self, text: str):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def __str__(self):
        return self.text

    def get_processed_text(self, processor) -> None:
        """Вызывает метод класса обработчика.

        :param processor: экземпляр класса обработчика
        """
        result = processor.process_text(self.text)
        print(*result, sep="\n")


class WordCounter:
    """Счётчик частотности слов в тексте."""
    def __init__(self, text: str) -> None:
        """Обрабатывает переданный текст и создаёт словарь с частотой слов."""
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word: str) -> int:
        """Возвращает частоту переданного слова."""
        return self.__words.get(word, 0)

    def get_all_words(self) -> dict[str, int]:
        """Возвращает словарь с частотой слов."""
        return self.__words.copy()


sort_text = TextParser(
    " %$# жаба огурец помидор помидор %?№ жаба жаба жаба №(;*%№; огурец лампа *%;№: лампа лампа "
).get_processed_text(Processor())


# stdout:
# огурец
# помидор
# лампа
# жаба