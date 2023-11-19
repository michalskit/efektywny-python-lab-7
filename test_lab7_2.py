# Testy - Zadanie 2
import unittest
import requests
from lab7_2 import BagOfWords

class TestBagOfWords(unittest.TestCase):
    def setUp(self):
        # Example text that needs to be modified to actually contain the expected word counts
        url = "http://www.gutenberg.org/cache/epub/1787/pg1787.txt"
        response = requests.get(url)
        hamlet_text = response.text
        self.bow = BagOfWords(hamlet_text)

    def test_common_words(self):
        most_common_words = sorted(self.bow.word_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        expected = [('the', 1349), ('and', 1101), ('of', 887)]
        self.assertEqual(most_common_words, expected)

    def test_hamlet_count(self):
        hamlet_count = self.bow['hamlet']
        self.assertEqual(hamlet_count, 115)

if __name__ == '__main__':
    unittest.main()
