# Zadanie 2

# Uzupełnij poniższą klasę BagOfWords, tak żeby usuwała znaki interpunkcyjne i przekształcała tekst na małe litery.
# Natępnie uzupełnij hamlet_count i most_common_words, tak żeby zwracały odpowiednie wartości.

import re
import requests

class BagOfWords:
    """
    Klasa BagOfWords reprezentuje strukturę danych typu "worek słów", 
    która zlicza wystąpienia każdego słowa w podanym dokumencie (ciągu znaków) lub pliku tekstowym.
    """

    def __init__(self, source):
        """
        Inicjalizuje instancję klasy BagOfWords.
        Args:
        source (str or file-like object): Źródło tekstu, może być ciągiem znaków lub obiektem plikowym.
        """
        self.word_counts = {}
        if isinstance(source, str):
            self._process_text(source)
        elif hasattr(source, 'read'):
            self._process_text(source.read())

    def _process_text(self, text):
        """
        Prywatna metoda do przetwarzania tekstu i zliczania wystąpień słów.
        Args:
        text (str): Tekst do przetworzenia.
        """
        # Usuwamy znaki interpunkcyjne i przekształcamy tekst na małe litery
        text = ...

    
        for word in text.split():
            self.word_counts[word] = self.word_counts.get(word, 0) + 1

    def __str__(self):
        """
        Reprezentacja tekstowa worka słów.

        Returns:
        str: Ciąg znaków reprezentujący worek słów w formacie "słowo:ilość_wystąpień".
        """
        return ', '.join(f"{word}:{count}" for word, count in self.word_counts.items())

    def __contains__(self, word):
        """
        Sprawdza, czy słowo znajduje się w worku.

        Args:
        word (str): Słowo do sprawdzenia.

        Returns:
        bool: True, jeśli słowo znajduje się w worku, w przeciwnym razie False.
        """
        return word in self.word_counts

    def __iter__(self):
        """
        Iterator po słowach w worku, od najczęściej do najrzadziej występującego.

        Returns:
        iterator: Iterator po słowach.
        """
        return iter(sorted(self.word_counts, key=self.word_counts.get, reverse=True))

    def __add__(self, other):
        """
        Dodaje dwa worki słów, sumując liczbę wystąpień każdego słowa.

        Args:
        other (BagOfWords): Inny worek słów do dodania.

        Returns:
        BagOfWords: Nowy worek słów będący sumą obu worków.
        """
        new_bow = BagOfWords('')
        new_bow.word_counts = self.word_counts.copy()
        for word, count in other.word_counts.items():
            new_bow.word_counts[word] = new_bow.word_counts.get(word, 0) + count
        return new_bow

    def __getitem__(self, word):
        """
        Zwraca liczbę wystąpień słowa w worku.

        Args:
        word (str): Słowo, którego liczbę wystąpień chcemy poznać.

        Returns:
        int: Liczba wystąpień słowa.
        """
        return self.word_counts.get(word, 0)

    def __setitem__(self, word, count):
        """
        Ustawia liczbę wystąpień danego słowa w worku.

        Args:
        word (str): Słowo, którego liczbę wystąpień chcemy ustawić.
        count (int): Liczba wystąpień do ustawienia.
        """
        self.word_counts[word] = count


# Uruchomienie na tekście Hamleta
url = "http://www.gutenberg.org/cache/epub/1787/pg1787.txt"
response = requests.get(url)
hamlet_text = response.text

bow_hamlet = BagOfWords(hamlet_text)

# Zliczanie wystąpień słowa "hamlet"
hamlet_count = ...

# 3 najczęściej występujące słowa
most_common_words = ...

print(hamlet_count) # 115
print(most_common_words) # [('the', 1349), ('and', 1101), ('of', 887)]